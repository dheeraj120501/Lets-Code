# INDRODUCTION

## 0
- JavaScript was initially created to `make web pages alive`.
- The programs in this language are called `scripts`.
- When JavaScript was created, it initially had another name: `LiveScript`. But Java was very popular at that time, so it was decided that positioning a new language as a “younger brother” of Java would help.
- JavaScript became a fully independent language with its own specification called `ECMAScript`, and now it has no relation to Java at all.
- Nowadays JavaScript can execute not only in the browser, but also on the server, or actually on any device that has a special program called the `JavaScript engine`.
  - The browser has an embedded engine sometimes called a `JavaScript virtual machine`.
    - **V8** – in Chrome and Opera.
    - **SpiderMonkey** – in Firefox.
    - **Chakra** for IE.
    - **JavaScriptCore**, **Nitro** and **SquirrelFish** for Safari.

## 1
- Engines are complicated. But the basics are easy.
  - The engine (embedded if it’s a browser) reads *parses* the script.
  - Then it converts (“compiles”) the script to the machine language.
  - And then the machine code runs, pretty fast.
 - The engine applies optimizations at each step of the process. It even watches the compiled script as it runs, analyzes the data that flows through it, and further optimizes the machine code based on that knowledge, this is called `just-in-time-compilation (JIT)`

- Modern JavaScript is a “safe” programming language. It does not provide low-level access to memory or CPU, because it was initially created for browsers which do not require it.
- JavaScript’s capabilities greatly depend on the environment it’s running in.
  - Node.js supports functions that allow JavaScript to read/write arbitrary files, perform network requests, etc.
  - In-browser JavaScript can do everything related to webpage manipulation, interaction with the user, and the webserver.

## 2
- JavaScript’s abilities in the browser are limited for the sake of the user’s safety, to prevent webpage from accessing private information or harming the user’s data.
  - JavaScript on a webpage may not read/write arbitrary files on the hard disk, copy them or execute programs. It has no direct access to OS functions. (Requires user access).
  - JavaScript from one page may not access the other if they come from different sites (from a different domain, protocol or port) `Same Origin Policy`.
	- JavaScript can easily communicate over the net to the server where the current page came from. But its ability to receive data from other sites/domains is crippled. Though possible, it requires explicit agreement (expressed in HTTP headers) from the remote side.
	- A page from `http://anysite.com` which a user has opened must not be able to access another browser tab with the URL `http://gmail.com` and steal information from there.
	
- Such limits do not exist if JavaScript is used outside of the browser, for example on a server. Modern browsers also allow plugin/extensions which may ask for extended permissions.

- A plethora of new languages appeared, which are `transpiled` (converted) to JavaScript before they run in the browser, modern tools make the transpilation very fast and transparent, actually allowing developers to code in another language and  *auto-converting it “under the hood”*.
  - CoffeeScript 
  - TypeScript
  - Flow
  - Dart
  - Kotlin
	
## 3
- What makes JS unique is:
	- Full integration with HTML/CSS.
	- Simple things are done simply.
	- Support by all major browsers and enabled by default.
