---
id: dotnet-benchmark-instrumentation
title: Scope .NET Agent benchmarks instrumentation
sidebar_label: Benchmarks instrumentation
---

The Scope agent supports benchmark tests instrumentation using a [BenchmarkDotNet](https://benchmarkdotnet.org/) exporter.

To use the exporter you need to add the [`ScopeAgent.Extensions.BenchmarkDotNet`](https://www.nuget.org/packages/ScopeAgent.Extensions.BenchmarkDotNet/) package to the [BenchmarkDotNet](https://benchmarkdotnet.org/) project, you can do it using:

```bash
dotnet add package ScopeAgent.Extensions.BenchmarkDotNet
```

Then you need to add the exporter to the classes containing the benchmarks using the `[ScopeExporter]` attribute, for example:

```csharp
[ScopeExporter]
[MemoryDiagnoser]
[SimpleJob]
public class Sample
{
    [Params(100)]
    public int N { get; set; }
        
    [Benchmark(Baseline = true, Description = "My description")]
    public void FirstTest()
    {
        for (var i = 0; i < M; i++)
            Thread.Yield();
    }
    [Benchmark]
    public void SecondTest()
    {
        for (var i = 0; i < N; i++)
            Thread.Sleep(0);
    }
}
```

You can also instrument all classes using the `BenchmarkSwitcher` in your `Program.Main` method:

```csharp
public class Program
{
    public static void Main(string[] args)
    {
        BenchmarkSwitcher.FromAssembly(typeof(Program).Assembly).Run(args, DefaultConfig.Instance.With(new ScopeExporter()));
    }
}
```
