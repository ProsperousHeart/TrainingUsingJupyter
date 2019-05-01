# Table Of Contents

1. [Introduction to JavaScript](01_Intro_to_JS.MD)
2. [JavaScript Basics](02_JS_Basics.MD) (_you are here_)
    - [Tools For JS Development](#tools-for-js-development)
    - [Intro To Browser Console](#intro-to-browser-console)
    - [Integrating JS With HTML](#integrating-js-with-html)
        - [Adding JS Inline To HTML Document](#adding-js-inline-to-html-document)
        - [Add JS To External File](#add-js-to-external-file)
        - [JS Render Blocking](#js-render-blocking)
    - [Crash Course in Writing JS](#crash-course-in-writing-js)
3. [Working With Data](03_Working_With_Data.MD)
4. [Functions & Objects](04_Functions_Objects.MD)
5. [JS & The Dom:  Changing The Elements](05_JS_Dom_ChangingElements.MD)
6. [JS & The Dom:  Events](06_JS_Dom_Events.MD)
7. [Loops](07_JS_Loops.MD)
8. [Troubleshooting, Validating, Minifying JS](08_JS_TVM.MD)
9. [Project Ideas](99_Project_Ideas.MD)
10. [Project Answers](99_Project_Ideas_ANSWERS.MD)

# Tools For JS Development

JS is the basic coding language that runs without compilation in any browser. (No fancy tools to write or test your code!)

Here's what you'll need:
- text (code) editor
- a browser with developer tools
- helper tools for debugging

## Code Editors

Can use a standard text or code editor, or use a standard IDE.

What matters is that there is proper support for your solution, including:
- code highlighting
- code hinting

Here are a few examples for editors:
- **Atom** (be sure to [check this out](README.md#how-to-code-in-javascript) if you plan on using this editor)
- Visual Studio Code
- Sublime Text

Here are a few examples for integrated development environments (IDEs):
- NetBeans
- Aptana Studio
- Eclipse

## Browser to Run JS

All modern browsers have advanced developer tools built in so you can work with your scripts in their natural environment.

Your browser choice is simply based on your preference.

Examples:
- **Chrome**
- Firefox
- Edge
- Opera
- Brave

Use one browser for development, and then test in all. That way you know they work everywhere.

# Intro To Browser Console

The natural environment for JS is the browser. Logging, testing, debugging, etc are all built into modern browsers with their development tools.

In this training, I will be focusing on using with Chrome & it's developer tools.

There are 2 ways to begin using the developer tool on Chrome:
1 - right click on a webpage and choose **inspect**
2 - use the keystrokes for your particular machine
    - Windows:  `ctrl + shift + i`
    - Mac:  `cmd + opt + i`
    
What can you do with the developer tools? Here are a few:
- inspect DOM elements
- instpect styles connected to DOM elements
- run network audits

## Console In Dev Tools

The **console** is a command line for the browser where you can write, manage, and monitor Js on the fly. (You can write JS commands in this console immediately.)

This is the 2nd tab in Chrome's dev tools. You can also access this panel by choosing:
- Windows:  `ctrl + shift + j`
- Mac:  `cmd + opt + j`

You can also open this as a "Drawer" by clicking on the 3 vertical dots and choosing **Show console drawer** from the options or by hitting the `ESC` key on your keyboard.

If at any time you wish to reuse the code in the console, just press your up arrow.

### Hello World

**Try This:**
`alert("Hello World!")`
Then hit the return key on your keyboard. You should now have a browser pop-up.

You can even do math within that alert, asking for information, etc.

To create a new line before running your code, `shift + enter` should create a new line.

Just remember:  the console is your JS playground where you can experiment and try new things

### Interacting With Alert & Logging

**Try this:**
```javascript
var date = new Date()
alert("Today is " + date)
```

Once you have created a variable, you do not need to create it again.

If you do not wish to have a pop up every time, you can also put it into the console log:

```javascript
var date = new Date()
console.log("Today is " + date)
```

### Interacting With Web Page

To be able to interact with the HTML, you need to know the structure. Your **Elements** tab can provide insight.

Let's say we're looking at this empty web page:

```html
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>An empty page</title>
</head>

<body>

</body>

</html>
```

In order to interact with the HTML document, you must:
- call the document
- use dot notation to specifically call the piece you wish to update
- use dot notation to find inner HTML and replace with something new

```javascript
document.body.innerHTML = "<h1>The date today is " + date + "</h1>"
```

You will notice that the empty HTML doc is now updated on the fly. While the **Elements** will show the change, your original document is unchanged. This update was only done inside the browser.

You can even dig further with this, as the `Date()` data has additional attributes.

```javascript
document.body.innerHTML = "<h1>The date today is " + date.getMonth() + "/" + date.getDate() + "/" + date.getFullYear() + "</h1>"
```

**NOTE:** need to be careful, since sometimes lists start with 0 instead of 1.
_What do you notice about the current date?_

You can fix it by running:

```javascript
document.body.innerHTML = "<h1>The date today is " + (date.getMonth() + 1) + "/" + date.getDate() + "/" + date.getFullYear() + "</h1>"
```

# Integrating JS With HTML

Since we cannot rely on a visitor opening the dev tools and typing their own JS, we must get the browser to load and run our JS alongside the HTML markup automatically.

There are 2 ways to do this:
1. adding inline to HTML document itself
2. add a separate file & tell browser to download said file with HTML

**REMEMBER:** JS runs as soon as the browser sees it. This means the order with which you provide your content and your JS is the order it will be rendered.

## Adding JS Inline To HTML Document

Let's say you start with this HTML doc:

```HTML
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>An empty page</title>
</head>

<body>

</body>

</html>
```

JS has a dedicated HTML tag `script` that wraps around the actual JS code. The tag and it's contents can be placed in any of these elements:
- the `head` of the HTML
- the `body` element
- after the `body` element

The placement of this code is dependent upon several factors, including but not limited to:
- when you want the script to execute
- whether render blocking matters

When talking about **inline**, you can use a simple rule of thumb.
- If you want the script to run before the contents of the page are rendered (such as a Facebook pixel) then you will add it to the `head` HTML code.
- If you want the script to run after content is rendered, it should be done after the `body` section.

Try putting this code after the `body` section of the HTML content:

```html
<script>
    var date = new Date();
    document.body.innerHTML = "<h1>The date today is " + date + "</h1>"
</script>
```

Save the HTML document and then open the browser to see the changes.

_What do you notice in the **Elements** section using the dev tools?_

_What do you think will happen if the JavaScript was put at the end of the `head` section? (Remember the page is rendered from top down.)_

Using JS inline is fine for smaller scripts or sites that only have 1 page, however for larger scripts or scripts used on many pages? This is not very effective.

## Add JS To External File

Since inline scripts are not effective for large sites or multiple pages, scripts typically live in their own JS file(s) and are referenced by the HTML document. Very much like how we interact with images and CSS files.

Let's say that you have an `index.html` file like this:

```html
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>An empty page</title>
</head>

<body>

</body>

<script>
    var date = new Date();
    document.body.innerHTML = "<h1>Today is: " + date + "</h1>";
</script>

</html>
```

Here is what you would need to do:
1. create a file called `script.js` for your JS code
2. go to your `index.html` file, grab the contents inside the `script` tags (cut)
3. paste into your `script.js` file and save
4. reference the `script.js` file within your `script` tags by adding a `src` key

You will now have files like this:

**script.js**

```javascript
var date = new Date();
document.body.innerHTML = "<h1>Today is: " + date + "</h1>";
```

**index.html**

```html
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>An empty page</title>
</head>

<body>

</body>

<script src="script.js"></script>

</html>
```

When opening this HTML file, it should appear exactly as before.

## JS Render Blocking

Because JS may change HTML or CSS on a page, any time a browser encounters a JS file reference it stops page rendering until the script file is downloaded and executed.

This can slow down site performance significantly.

The emerging protocol for the web ([HTTP/2](https://en.wikipedia.org/wiki/HTTP/2)) partially solves this issue by allowing the browser to download multiple assets in parallel. But if file is referenced in the header, render blocking will still happen - just takes less time.

This is why best practice **used to be** putting JS at the bottom of the document below the end `body` tag (even if scripts were supposed to run at top). But now? This issue is resolved.

When we call a JS file today, you can do one of these types of loading...

### Right Away Loading

`<script src="script.js"></script>`

When using this option, HTMl will parse until it encounters a reference to JS.
Then the JS file is loaded, executed, and then HTML continues it's parsing.

This is a JS render blocking.

### Asynchronous Loading

`<script src="script.js" async></script>`

When you add the `async` attribute, the Js file will be downloaded alongside the HTML.

Render blocking only kicks in when the script is executed. Then the rest of the HTML will be rendered.

This si better and useful in some situations.

### Deferred Loading

`<script src="script.js" defer></script>`

Everything is loaded first before rendering the scripts.
Loading and execution of the file (even if referenced in the head) only happens when everything else is loaded.

Therefore this option would fix the error when loading JS into the header but the rest of the HTML markdown is not loaded yet.

# Crash Course in Writing JS

Before writing, you need to know basic rules of the language so you can write (good) JS.

Regardless of your best practices, code should be readable and maintainable - by you and others!

1. JS is Case Sensitive

    Unlike in HTML & CSS, casing of a word matters. If you are not careful, you will receive a `Uncaught ReferenceError` error.

2. Use camelCase
    
    This is the agreed upon naming convention for JS. General rules:
    - start variable, function, and method names with a lowercase letter:  `var greenDuck;`
    - start class and object names with a capitalized letter:   `var date = Date();`
    - constants are all caps:   `const = CONSTANTLYUPPERCASE;`

3. Whitespace Matters (to humans)
    
    JS does not care about whitespace. But for your sanity, use it!
    
    JS instructions are written in the form of statements. Each statement is a separate instruction.
    
    If you don't do this consistently, it will be difficult for humans to read.
    
    Each statement should go on it's own line, properties within functions within multiple lines are indented, etc. 
    
    End result is easy to maintain code.

4. End Each Statement With A Semicolon `;`
    
    This is controversial since JS technically doesn't care... except for a few specific situations!
    
    Without this, your code can be very hard to read.

5. Use Comments Liberally
    
    Comments are strings of text in your code that are ignored by your browser.
    
    Single line comments:
        ```javascript
        // single line comment
        var date = new Date();
        ```
    
    Multi line comments:
        ```javascript
        /* multi line
        can span multiple lines */
        date = new Date();
        ```
    
    Use comments to:
    - leave notes to yourself
    - leave notes to anyone looking at your code