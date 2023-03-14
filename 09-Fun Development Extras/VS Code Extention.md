# Yoeman, The Scaffolding tool

- Use **yoeman** to create a Project, yoeman is a scaffolding tool (like Create React App) that creates a boilerplate project for you to start creating extentions.

- **vscode** is an API provided to us which help us to manipulate vscode from code, we can registercommand, executecommand and can create different views for our extention. It is the only way to communicate with vscode.

# VSCODE Extention creation

- Registering a command in our extention:

  - In the main file setup the command(give it a name and assign it a callback) and dispose it.
  - In the package.json's contribute section register the command so that vscode know the command exist.
  - Finally in the package.json's activation section activate the command so it work when clicked.

- When we register any command or view for our extention we need it to be disposed as well so that it will get away from memory when it's done. `context.subscriptions.push()` does the disposing task.

- NOTE:

  - **Activation Event**: Activates the command when the user select the registered command. These are events upon which your extension becomes active.
  - **Contribution Point** make the command available in the Command Palette, and bind it to a command ID.
  - **VS Code API** to bind a function to the registered command ID.

- Contribution points are static declarations you make in the package.json Extension Manifest to extend VS Code such as adding commands, menus, or keybindings to your extension.

- The main file exports two functions, `activate` and `deactivate`. activate is executed when your registered Activation Event happens. deactivate gives you a chance to clean up before your extension becomes deactivated(when VS Code is shutting down or the extension is disabled or uninstalled).

- Both the activate and deactive are only going to be called once when the Extention loads and disabled respectively, so we can do things which we want to happen at the start(initilizations) or end of the API once, like loading any json data from the network(start) or cleaning the memory(end).

# How things work

- Creating a VS code extention is just like creating any other app, we can use anything that spits out js, everything we have is a webview, we might have a backend or we can have an API to fetch the data, sometimes we might need authorization and authentication as well.
- The src will have the main files where we register commands and views for our extentions, as vscode is written in electron.js so it's all html, css, js.
- We will create a different folder for our webviews and can use anything that is going to create js file at the end. TS, sveltte etc.
- A folder called media that is going to contain all our assets like css files, images etc.

# Sharing information

- vscode API is not available in webviews by default so we need a way to send information from VSC to webviews and vice versa.
- To enable the vscode api in webview, basically HTML, then we need to store `acquireVsCodeApi()` in a variable that help us to send message from webview to VSC.

# Resource

- https://github.com/microsoft/vscode-extension-samples, this is the source from where one can learn stuffs about vscode entention creation.
