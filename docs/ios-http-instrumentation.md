---
id: ios-http-instrumentation
title: Scope iOS Agent HTTP Instrumentation
sidebar_label: HTTP Instrumentation
---

To integrate logs and exceptions from services your integration tests interact with over HTTP, 
you must append some headers to your outgoing requests that identify the test and context from where those request were made. 
The following changes must be done on the client application side in order for this to work:

## Installation

Link your application or framework target with `ScopeAgent`

<!--DOCUSAURUS_CODE_TABS-->
<!--Cocoapods-->
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

<!--Carthage-->
Add the `ScopeAgent` dependency to your `Cartfile` if not already done in previous steps, and run `cart update`

```
binary "https://releases.undefinedlabs.com/scope/agents/ios/ScopeAgent.json"
```

In your application or framework targets, add `ScopeAgent.framework` located in `Carthage/Build/iOS` to the
*Linked frameworks and Libraries* in General target settings or to the *Link Binaries With Libraries* build phase. 

<!--END_DOCUSAURUS_CODE_TABS-->

## 



### Using the thin client library

If linking the full `ScopeAgent` library to your main application is not an option, we provide a thin client package called `ScopeAgentClient` that provides the same API described below and communicates with the full `ScopeAgent` library if it is present. With this approach, you link your main application with `ScopeAgentClient` and the tests target with `ScopeAgent`, and the information will be collected during your tests, with minimal impact to your distributable application.
with `ScopeAgent`.

Install this dependency to your test targets by adding:

<!--DOCUSAURUS_CODE_TABS-->
<!--Cocoapods-->

```
target 'MyTests' do
 pod 'ScopeAgentClient'
end
```

<!--Carthage-->

```
binary "https://releases.undefinedlabs.com/scope/agents/ios/ScopeAgentClient.json"
```

<!--END_DOCUSAURUS_CODE_TABS-->


## Usage

If you use the ScopeAgent framework you can use  `SAURLSessionObserver.adapt(_:)` or `SAURLSessionObserver.adaptConfiguration(_:)` methods to modify your `URLRequest` or `URLSessionConfiguration` objects. The interface of `SAURLSessionObserver.adapt(_:)` is as follows:

```swift
class SAURLSessionObserver {
   public class func adapt(_: URLRequest?) -> URLRequest
   public class func adaptConfiguration(_: URLSessionConfiguration) -> URLSessionConfiguration
}
```

If you use the ScopeAgentClient framework, use the `SAURLSessionObserverClient` class to modify your `URLRequest` objects. The interface is as follows:

```swift
class SAURLSessionObserverClient {
   public class func adapt(_: URLRequest?) -> URLRequest
   public class func adaptConfiguration(_: URLSessionConfiguration) -> URLSessionConfiguration
}
```

> Both libraries work in the same way. In the following examples, `SAURLSessionObserver` has been used, but can be replaced by `SAURLSessionObserverClient` with the same behaviour.

#### Adding intrumention to URLSessionConfiguration

If your application creates its own `URLSession` or Alamofire `SessionManager` by using a `URLSessionConfiguration`, you can simply call `SAURLSessionObserver.adaptConfiguration(_:)` with the configuration before constructing the `URLSession` with it. It will instrument all requests performed in the `URLSession` just created.

<!--DOCUSAURUS_CODE_TABS-->
<!--Alamofire-->

```swift
let configuration = URLSessionConfiguration.default
SAURLSessionObserver.adaptConfiguration(configuration);
let sessionManager = Alamofire.SessionManager(configuration: configuration)
```

<!--URLSession-->

```swift
let configuration = URLSessionConfiguration.default
SAURLSessionObserver.adaptConfiguration(configuration);
let session = URLSession(configuration: configuration)
```

<!--END_DOCUSAURUS_CODE_TABS-->

#### Adding intrumention to URLRequest

You can also use an approach based on the individual requests by calling `SAURLSessionObserver.adapt(_:)` with your original request as a parameter:

<!--DOCUSAURUS_CODE_TABS-->
<!--Alamofire-->

```swift
let url = URL(string: myURLString)!
var urlRequest = URLRequest(url: url)
// Add following line to modify the request
urlRequest = SAURLSessionObserver.adapt(urlRequest)

Alamofire.request(urlRequest).responseJSON { response in
  ...
}
```

<!--URLSession-->

```swift
let url = URL(string: myURLString)!
var urlRequest = URLRequest(url: url)
// Add following line to modify the request
urlRequest = SAURLSessionObserver.adapt(urlRequest)

let task = URLSession.shared.dataTask(with: urlRequest) { data,response,error  in
  ...
}
```

<!--END_DOCUSAURUS_CODE_TABS-->

## 

If you use Alamofire, you can also use a helper class that implements the `RequestAdapter` protocol, and use this class session instead of Alamofire's default one.

```swift
class AlamofireTracing: RequestAdapter {
    static var session: SessionManager {
        let sessionManager = Alamofire.SessionManager.default
        sessionManager.adapter = AlamofireTracing()
        return sessionManager
    }
    func adapt(_ urlRequest: URLRequest) throws -> URLRequest {
        let urlRequest = SAURLSessionObserverClient.adapt(urlRequest)
        return urlRequest
    }
}

// Usage:
let url = URL(string: myURLString)!
AlamofireTracing.session.request(url).responseJSON { response in
  ...
}
```

