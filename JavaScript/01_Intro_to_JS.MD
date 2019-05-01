<a href='https://www.learntocodeonline.com/'><img src="https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true"></img></a>

# Table Of Contents

1. [Introduction to JavaScript](01_Intro_to_JS.MD) (_you are here_)
    - [What Is JavaScript? (REALLY)](#what-is-javascript-really)
    - [Layers Of A Web Page](#layers-of-a-web-page)
    - [How Does Accessing A Web Page Work?](#how-does-accessing-a-web-page-work)
    - [Difference Between Java & JavaScript](#difference-between-java--javascript)
    - [Navigating the JS Landscape](#navigating-the-js-landscape)
    - [Additional Libraries, Frameworks, & Platform Environments](#additional-libraries-frameworks--platform-environments)
2. [JavaScript Basics](02_JS_Basics.MD)
3. [Working With Data](03_Working_With_Data.MD)
4. [Functions & Objects](04_Functions_Objects.MD)
5. [JS & The Dom:  Changing The Elements](05_JS_Dom_ChangingElements.MD)
6. [JS & The Dom:  Events](06_JS_Dom_Events.MD)
7. [Loops](07_JS_Loops.MD)
8. [Troubleshooting, Validating, Minifying JS](08_JS_TVM.MD)
9. [Project Ideas](99_Project_Ideas.MD)
10. [Project Answers](99_Project_Ideas_ANSWERS.MD)

# What Is JavaScript? (REALLY)

## Super Technical Explanation

From [Wikipedia](https://en.wikipedia.org/wiki/JavaScript):
> ... often abbreviated as **JS**, is a high-level, interpreted programming language that conforms to the ECMAScript specification. JavaScript has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.

>   Alongside [HTML](https://en.wikipedia.org/wiki/HTML) and [CSS](https://en.wikipedia.org/wiki/CSS), JavaScript is one of the core technologies of the World Wide Web. JavaScript enables interactive web pages and is an essential part of web applications. The vast majority of websites use it, and major web browsers have a dedicated JavaScript engine to execute it.

## Short Explanation

JavaScript (JS) allows you to write small programs that:
- run in the browser
- change the HTML and CSS of the current document based on triggers/events

# Layers Of A Web Page

When you see an interactive web page, you are actually seeing the combination of 3 layers of code.

## Layer 1:  HTML Markup (Content Layer)

This is where the content lives. Without the HTML document, there is no web page.

## Layer 2:  Collection of CSS Rules (Presentation Layer)

This is the code that instructs the browser on how to display the HTML markup.

HTML & CSS work together to provide the look and feel of the whole site.

Even if you take CSS away, the content is still there.

## Layer 3:  JavaScript (Presentation Layer)

This is the interactive layer. JS is a language that **runs in the browser** and interacts with the HTMl markup and CSS rules to change what you see and are able to do.

# How Does Accessing A Web Page Work?

1. When you access web site, you first pull down the HTML and indexes it's content.
2. CSS and JS documents that are referenced will be downloaded.
3. JS is run to see if any of the HTML markup has changed.
4. Applies CSS to make everything look as it should.
5. Leaves JS running in the background in case of an interaction or event triggers additional scripts.

# Difference Between Java & JavaScript

**Java**:  a programming language used to write applications for computers and other devices

**JavaScript**:  a scripting language used to interact with content in a web browser (more recently in other places like phone apps)

The only real thing they have in common is they have **Java** in their names.

Without diving too deep into this history, after a few iterations it was determined to use _JavaScript_. The idea at the time was to make a complementary scripting language to _Java_ in order to cash in on _Java_'s popularity.

# Navigating the JS Landscape

JS conforms to the ever-evolving [ECMAScript (ES) standard](https://en.wikipedia.org/wiki/ECMAScript) - a specification created to standardize JS & foster multiple independent implementations (like [JScript](https://en.wikipedia.org/wiki/JScript) and [ActionScript](https://en.wikipedia.org/wiki/ActionScript)).

It is a specification for interpreting code and languages like JS & is commonly used for client-side scripting. It is also increasingly being used for writing server apps & services using [Node.js](https://en.wikipedia.org/wiki/Node.js).

Browsers use ECMAScript to interpret JS. So JS and EXMAScript are two sides of the same coin - meaning from a coder perspective they are the same.

## More On ECMAScript

**ECMAScript 6 (ES6)** is now known as **ECMAScript 2015**.

Browsers are slow to adopt new technology, so it takes time to catch up to ECMAScript.
- ECMAScript 5.1 (2011) is the current standard but is extremely outdated
- ECMAScript 2015 (ES6) is emerging but spotty support (not all browsers use it) so to make scripts cross-browser compatible devs must run modern JS through a transpiler like [Babel](https://babeljs.io/) to translate into old JS
- ECMAScript 2016 (ES7) is in development but no current support 

# Additional Libraries, Frameworks, & Platform Environments

## jQuery

jQuery is a library of JS functions & commands that allow us to do fancy JS things.
- introduces CSS-like syntax & several visual/UI enhancements
- done with less code
- simplifies use of JS in websites

This is an abstraction of the core language. There used to be a ton of these libraries, but now this one is most widely used.

## JS Frameworks

JS Frameworks are front-end application frameworks used to simplify the building of advanced interactive web-based applications. 

Framework examples include but are not limited to:
- AngularJS
- React
- Vue.js

Traditional technologies like PHP generate the pages on the server and send to the browser. But these frameworks run **within** the browser and pull just the data from the server.
- makes the websites that run them **really** fast
- has significant drawbacks when JS is not working

## Platform Environments

**Node.js** is one example - it is a JS platform built on browser runtime environments. This one is used to run advanced operations & applicatiosn on servers and computers using JS.

You can use this to help debug JS on your local machine!