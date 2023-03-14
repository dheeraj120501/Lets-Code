Since the introduction of Go in 2009, there have been several changes in how Go developers organize their code and their dependencies. Because of this churn, there’s lots of conflicting advice, and most of it is obsolete. For modern Go development, the rule is simple: **you are free to organize your projects as you see fit**.

Out of the box, Go ships with many development tools. You access these tools via the go command.

- They include a compiler, code formatter, linter, dependency manager, test runner, and more.

# Packages

Every Go program is made up of packages.

Programs start running in package main.

By convention, the package name is the same as the last element of the import path.

- For instance, the "math/rand" package comprises files that begin with the statement package rand.

# Imports

Factored imports

```go
import (
    "fmt"
	"math"
)
```

Multiple imports

```go
import "fmt"
import "math"
```

It is good style to use the factored import statement.

# Exported names

In Go, a name is exported if it begins with a capital letter.

- For example, Pi is an exported name, which is exported from the math package.

When importing a package, you can refer only to its exported names.

Any "unexported" names are not accessible from outside the package.

# Functions

A function can take zero or more arguments and can return any number of results.

```go
func swap(x, y string) (string, string) {
	return y, x
}
```

`The type comes after the variable name. Go’s declarations read left to right. It’s been pointed out that C’s read in a spiral clockwise manner!`

When two or more consecutive named function parameters share a type, you can omit the type from all but the last.

```go
func add(x, y int) int {
	return x + y
}
```

Go's return values may be named. If so, they are treated as variables defined at the top of the function. These names should be used to document the meaning of the return values.

A return statement without arguments returns the named return values. This is known as a "naked" return.

Naked return statements should be used only in short functions, as they can harm readability in longer functions.

```go
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```

# Variables
