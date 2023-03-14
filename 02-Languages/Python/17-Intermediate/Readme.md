# Type Annotations

Type Annotations allow to add type hints to variables.
They are used to inform someone reading the code what the type of a variable should be.
This brings a sense of statically typed control to the dynamically typed Python. This is accomplished by adding : <type> after initializing/declaring a variable.

- eg. `age: int = 5`

NOTE: Type annotations do not affect the runtime of the program in any way. These hints are ignored by the interpreter and are used solely to increase the readability for other programmers and yourself. They are not enforced at runtime.

Function Annotation
eg.

```py
def mystery_combine(a: str, b: str, times: int) -> str:
    return (a + b) * times
```

For anything more than a primitive in Python, use the typing class. It describes types to type annotate any variable of any type. It comes preloaded with type annotations such as Dict, Tuple, List, Set etc.
eg.

```py
from typing import List
def print_names(names: List[str]) -> None:
for student in names:
print(student)
```

eg. `Dict[str, float]`

Use Optional when the value will be be either of a certain type or None, exclusively. Use Union when the value can take on more specific types.

- For more examples, check out the official Python documentation for the typing module.
