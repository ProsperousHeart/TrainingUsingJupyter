<a href='https://www.learntocodeonline.com/'><img src="https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true"></img></a>

# Table Of Contents

1. [Introduction to JavaScript](01_Intro_to_JS.MD)
2. [JavaScript Basics](02_JS_Basics.MD)
3. [Working With Data](03_Working_With_Data.MD)
4. [Functions & Objects](04_Functions_Objects.MD)
5. [JS & The Dom:  Changing The Elements](05_JS_Dom_ChangingElements.MD) (_you are here_)
    - [Intro To DOM Elements](#intro-to-dom-elements)
    - [Targeting Node Elements In The Dom](#targeting-node-elements-in-the-dom)
6. [JS & The Dom:  Events](06_JS_Dom_Events.MD)
7. [Loops](07_JS_Loops.MD)
8. [Troubleshooting, Validating, Minifying JS](08_JS_TVM.MD)
9. [Project Ideas](99_Project_Ideas.MD)
10. [Project Answers](99_Project_Ideas_ANSWERS.MD)

# Intro To DOM Elements

The browser with which you are manipulating is an object.
The document it displays is an object.

Each object has a list of objects related to it as well. In the browser, it includes but is not limited to:
- the browser window
- document inside the window
- navigation buttons
- location or URL

These objects are modelled by what is known as **Browser Object Model** (BOM).

Since they are all objects, you can interact with them using JS.

**window** is the top-level object in the BOM. It has a ton of properties & methods you can use to interact with the browser itself as well as what it displays. To learn more about what is possible with your browser window, [check this out](https://developer.mozilla.org/en-US/docs/Web/API/Window).

You will interact with some of the BOM objects, but the majority of them are mainly left alone due to them being standard behavior.

The exception? [Document](https://developer.mozilla.org/en-US/docs/Web/API/Window/document). This is a property in the **window** object that contains the current HTML markup.

Generally you would call `window.document` but since JS lives inside the window, you can simply call it with `document` directly.

This `document` has it's own object model:  Document Object Model (DOM)

It is the model of the document (like `head` or `body`) that forms the current webpage.

In HTMl, every content piece is wrapped between tags to create each HTML element. Each element is a **DOM node** and the browser handles them the same way it would handle an object.

When a document is loaded into the browser, it is loaded into the document object of the BOM. From there a DOM is created for the instance. The browser then creates a node tree that models the relationships between the different nodes.

There are 2 main nodes in an HTML document node tree:
1. head
    - holds invisible objects (title, Facebook pixel, link, meta, script, etc)
2. body
    - holds all visible nodes
    
The nodes live in strict hierarchical relationships depending on how they are nested in the HTML.

You can see the code version of the DOM if you are in the **Elements** section of Developer Tools.

# Targeting Node Elements In The Dom

The document is one giant object, and each element in said document are nodes of that object.

You can see additional DOM properties [here](https://developer.mozilla.org/en-US/docs/Web/API/document) like:
- document.body
- document.title
- document.URL

To get to a node, element, or group of nodes inside the body? You'll use methods available for `document`. Traditionally will use:
- `document.getElementById("some-ID")` returns the element with the specific ID
- `document.getElementsByClassName("classname")` returns collections or node lists of all related elements
- `document.getElementsByTagName("HTML tag")` returns collections or node lists of all related elements

These are OK but can get clunky to work with. However [querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) and [querySelectorAll()](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) have since come out. The "selectors" are one or more comma separated CSS selectors.