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

## querySelector vs querySelectorAll

### querySelector

`document.querySelector(".masthead")` will return the document node **header** with the class `.masthead`

You will use a `.` to signify _class_ and a `#` to signify an _id_. This is because it is a CSS selector and we are just opening it in a JS.

`document` gives the entire document, where `querySelector` gives the first instance of any item that matches the request.

### querySelectorAll

If you want an element that is used several times, what do you use?

Let's say you wanted all anchors of the entire document - then you would use:  `document.querySelectorAll("a")`

This returns an HTML collection (node tree) with every single instance of the `a` element within the document & can sort through like a regular array.

### Comparison

`querySelector` will provide the first instance within the document.

If you need any other instance (or a group of it) then `querySelectorAll` would be used.

## Deeper Dive

`document.querySelector(".menu .has-children a")"` gives us the first link inside of an element with the class `.has-children` inside the element with the class `.menu`.

`document.querySelectorAll(".social-nav a[href*='linkedin.com']")` will give any linked pointing to LinkedIn inside the element with a class **social-nav**.  

You can also make multiple selections as long as the requests are separated by a comma.
`document.querySelectorAll(".menu li a, .social-nav li a")`

For more on these functions, [check this out](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors).

For full rundown of these methods, [click here](https://developer.mozilla.org/en-US/docs/Web/API/document).

# Accessing & Changing Elements

The purpose of targeting an element within the DOM using JS is to do something with it. This could include but is not limited to:
- change a class name
- update ID
- changes to the HTML as a whole

Each of the elements is it's own DOM node (effectively an object) with a long list of properties & methods with which to interact with it. The [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) page gives a full breakdown of all available properties and methods for Elements. Including but not limited to:
- tag name
- attributes
- inner HTML

Will also provide information about the attributes of each element such as:
- meta information
- scroll top (number of pixels form top of document the element is placed)

Most of these are read only but some crucial ones allow you to write directly to them.

For example - you might have an element called `.main-title` and you want the text within it. You might run:  `document.querySelector(".main-title").innerHTML`

If you wanted the whole code (including outer HTML) you would run:  `document.querySelector(".main-title").outerHTML`

# Accessing & Changing Classes

Read-only attributes generally have their own methods with which you can interact with them - such as [classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList).

# Accessing & Changing Attributes

Just like `classList` the `attributes` property is read-only and have teh additional complication of often appearing in attribute value pairs. (e.g.:  href always has a URL value)

While you can access the attributes, you still need methods to interact with them.

From [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) documentation, here are the 4 methods to choose from:
- `hasAttribute`
- `getAttribute`
- `setAttribute` (adds if none is present, otherwise changes the attribute)
- `removeAttribute`

Here is an example of what you might do to add to the link attribute of class `.cta`:

```javascript
const CTAELEMENT = document.querySelector(".cta a");

if (CTAELEMENT.hasAttribute("target")) {
    console.log(CTAELEMENT.getAttribute("target"))
} else {
    CTAELEMENT.setAttribute("target", "_blank")
}

console.log(CTAELEMENT.attributes)
```

Regardless of the attribute you are working with, this process is basically the same for confirming an attribute exists and for making a change.

# Adding DOM Elements

ADding new DOM elements can technically be done with a combination of inner and outer HTML properties, but they are crude tools for the job.

Here is a better way to do it:
1. create the element (as outlined [here](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement))
2. create the text node that goes inside the element (as outlined [here](https://developer.mozilla.org/en-US/docs/Web/API/Document/createTextNode))
3. add text node to the element
4. add element to the DOM tree (as outlined [here](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild))

This avoids breaking your document and unwanted changes.