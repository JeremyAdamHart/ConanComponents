Minimal project using conan with multiple components and transitive headers.

```
       test
      /    \
   bara    barb  <-- both in bar conan package
      \    /
       foo
```

`test` only links to `bara` and `barb` but gets access to `foo` headers
