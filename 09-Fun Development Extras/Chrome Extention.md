# Chrome Extention

Extensions are small software programs that customize the browsing experience. Google Chrome Extensions are applications that run inside the Chrome browser and provide additional functionality, integration with third party websites or services, and customized browsing experiences.

Extensions are made of different, but cohesive, components that can include background scripts, content scripts, an options page, UI elements and various logic files. An extension's components will depend on its functionality and may not require every option.

Extensions are built on web technologies such as HTML, JavaScript, and CSS. They run in a separate, sandboxed execution environment and interact with the Chrome browser.

Extensions let you "extend" the browser by using APIs to modify browser behavior and access web content. Extensions operate by means of an `end-user UI` and a `developer API`:

- The extensions user interface provides a consistent way for users to manage their extensions.

- Extensions APIs allow the extension's code to access features of the browser itself: activating tabs, modifying net requests, and so on.

To create an extension, you assemble some resources -- a manifest, JavaScript and HTML files, images, and others -- that constitute the extension.

A theme is a special kind of extension that changes the way the browser looks. Themes are packaged like regular extensions, but they don't contain JavaScript or HTML code.

# Some Facts about Chrome Extentions

Extensions are downloaded by the Chrome browser upon install, and are subsequently run off of the local disk in order to speed up performance. However, if a new version of the extension is pushed online, it will be automatically downloaded in the background to any users who have the extension installed. Extensions may also make requests for remote content at any time, in order to interact with a web service or pull new content from the web.

Extensions are capable of making cross-domain Ajax requests, so they can call remote APIs directly.

Extensions may communicate with each other by passing messages to each other.

# Manifest file

Extensions start with their manifest which is a json file. Every extension requires a manifest, though most extensions will not do much with just the manifest.

It gives the browser information about the extension, such as the most important files and the capabilities the extension might use.

The directory holding the manifest file can be added as an extension in developer mode in its current state.

Manifest file contains all the meta data about the extention.

Registering a `background` script in the manifest tells the extension which file to reference, and how that file should behave.

    ```json
    "background": {
        "service_worker": "background.js"
    }
    ```

Most APIs, must be registered under the `permissions` field in the manifest for the extension to use them.

Extensions can have many forms of a user interface like popup which can be registered in the `action` of manifest file. Designation for toolbar icons is also included under action in the `default_icon` field.

Extensions also display images on the extension management page, the permissions warning, and favicon. These images are designated in the manifest under `icons`.

Extensions can not inject content scripts on internal Chrome pages like "chrome://extensions".

# Resource

To learn more about chrome extentions on can refer to the sample examples provided at [extension samples](https://github.com/GoogleChrome/chrome-extensions-samples).
