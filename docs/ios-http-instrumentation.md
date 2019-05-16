---
id: ios-http-instrumentation
title: HTTP Instrumentation
sidebar_label: HTTP Instrumentation
---

To integrate logs and exceptions from services your integration tests interact with over HTTP, you must append some headers to your outgoing requests that identify the test and context from where those request were made. The following changes must be done on the client application side in order for this to work:

1. Link your application or framework target with `ScopeAgent`, if not already done in previous steps

   **For Cocoapods:** 

   By adding the pod to your `Podfile` and running `pod install`. For example:

   ```
   target 'MyApp' do
     pod 'ScopeAgent'
   end
   ```

    or

   ```
   target 'MyFramework' do
     pod 'ScopeAgent'
   end
   ```

   **For Carthage:**

   Add the `ScopeAgent` dependency to your Cartfile and run `cart update`:

   ```
   binary "https://releases.undefinedlabs.com/scope/agents/ios/ScopeAgent.json"
   ```

   In your Application or framework targets, add `ScopeAgent.framework` located in `Carthage/Build/iOS` to the *Linked frameworks and Libraries* in General target settings or to the *Link Binaries With Libraries* build phase. 

2. Use the `SAURLSessionObserver.adapt(_:)` method to modify your `URLRequest` objects. The interface of `SAURLSessionObserver.adapt(_:)` is as follows:

   ```swift
   class SAURLSessionObserver {
       public class func adapt(_: URLRequest?) -> URLRequest
   }
   ```

   You need to call `SAURLSessionObserver.adapt(_:)` with your original request as a parameter and will return a new copy of your request with the required HTTP headers added to it.



For Alamofire users the easiest approach is using a helper class that implements `RequestAdapter` protocol, and using this class session instead of Alamofire default one.

```swift
class AlamofireTracing: RequestAdapter {
    static var session: SessionManager {
        let sessionManager = Alamofire.SessionManager.default
        sessionManager.adapter = AlamofireTracing()
        return sessionManager
    }
    func adapt(_ urlRequest: URLRequest) throws -> URLRequest {
        let urlRequest = SAURLSessionObserver.adapt(urlRequest)
        return urlRequest
    }
}

// Usage:
let url = URL(string: myURLString)!
AlamofireTracing.session.request(url).responseJSON { response in
  ...
}
```

Another approach for Alamofire users is by using the method in each request independently:

```swift
let url = URL(string: myURLString)!
var urlRequest = URLRequest(url: url)
// Add following line to modify the request
urlRequest = SAURLSessionObserver.adapt(urlRequest)

Alamofire.request(urlRequest).responseJSON { response in
  ...
}
```

Fur URLSession users the calling method for each request is needed:

```swift
let url = URL(string: myURLString)!
var urlRequest = URLRequest(url: url)
// Add following line to modify the request
urlRequest = SAURLSessionObserver.adapt(urlRequest)

let task = URLSession.shared.dataTask(with: urlRequest) { data,response,error  in
   ...
 }
```