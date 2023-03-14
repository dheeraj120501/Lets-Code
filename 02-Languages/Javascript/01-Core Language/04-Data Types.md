## 0
- Objects are **heavier** than primitives.
- JavaScript allows us to work with primitives as if they were objects, but primitives are not objects.
  - Primitives are still primitive. A single value, as desired.
  - The language allows access to methods and properties of strings, numbers, booleans and symbols.
  - In order for that to work, a special `object wrapper` that provides the extra functionality is created, and then is destroyed.
  - The “object wrappers” are different for each primitive type and are called: `String`, `Number`, `Boolean` and `Symbol`.
    - eg. str.toUpperCase() The string str is a primitive. So in the moment of accessing its property, a special object is created that knows the value of the string, and has useful methods, like toUpperCase().
    - That method runs and returns a new string (shown by alert).
    - The special object is destroyed, leaving the primitive str alone.
  - JavaScript engines are well tuned to optimize that internally, so they are not expensive to call.
- Objects are always `truthy` in `if`.
- null/undefined have no methods, they are the most primitive type.
- We can also create the wrapper using Object constuctor, but this is highly unrecommended.
  ```js
  alert( typeof 0 ); // "number"
  alert( typeof new Number(0) ); // "object"
  ```
  - NOTE: Using functions `String()`, `Number()`, `Boolean()` without `new` is a useful thing, as they do explicit type conversion.
