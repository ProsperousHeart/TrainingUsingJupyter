<a href='https://www.learntocodeonline.com/'><img src="https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true"></img></a>

# Table Of Contents

1. [Introduction to JavaScript](01_Intro_to_JS.MD)
2. [JavaScript Basics](02_JS_Basics.MD)
3. [Working With Data](03_Working_With_Data.MD)
4. [Functions & Objects](04_Functions_Objects.MD) (_you are here_)
    - [Functions](#functions)
    - [Basic Functions](#basic-functions)
    - [Function Arguments](#function-arguments)
    - [Returning Values From A Function](#returning-values-from-a-function)
    - [Working With Anonymous Functions](#working-with-anonymous-functions)
    - [Immediately Invoking Functional Expressions](#immediately-invoking-functional-expressions)
    - [Variable Scope](#variable-scope)
    - [ES2015:  let and const](#es2015--let-and-const)
    - [Objects In JS](#objects-in-js)
5. [JS & The Dom:  Changing The Elements](05_JS_Dom_ChangingElements.MD)
6. [JS & The Dom:  Events](06_JS_Dom_Events.MD)
7. [Loops](07_JS_Loops.MD)
8. [Troubleshooting, Validating, Minifying JS](08_JS_TVM.MD)
9. [Project Ideas](99_Project_Ideas.MD)
10. [Project Answers](99_Project_Ideas_ANSWERS.MD)

# Functions

Scripts can be hundreds if not thousands of lines of code. And especially for the more intricate scripts, you need to be able to organize your code in such a way that you can reuse portions of it.

When you structure your code and make common operations reusable, you care functions and objects.

**Functions** - mini programs within your script. Can be used to:
- segment off sections of code to make it easier to manage
- run repeated operations
- all of the above

Functions wrap around code blocks. These **code blocks** are the actual statements to be run and include some combination of:
- variable assignments
- operations & conditions

Functions will either:
1. create a result immediately (like change the webpage)
2. provide an answer or output to be used by other functions (return value)

## Types of Functions

1. named functions (executed when called by name)
2. anonymous functions (typically run once triggered by a specific event)
3. immediately invoked function expressions (run the moment browsers encounter them)

## Function Structure

### Named Functions

You declare a function by starting with the word:  `function`

This is followed by the **name** of the function, open/close parenthesis (with possible inputs inside), and then a set of `{}` that wraps around the code block.

**For Example:**

```javascript
function multiply(a, b) {
    var answer = a*b;
    console.log(answer);
    return answer
}
var multiplied = multiply(4,5);
```

Technically it doesn't matter where the function sits (since the JS will be loaded first and then run), but for human readability it is best practice to call the function after it is created.

### Anonymous Functions

**Anonymous functions** don't have a name, so the `()` appears right after the function to trigger the function.

```javascript
var divided = function(a, b) {
    var answer = a / b;
    console.log(a + " divided by " + b + " is:  " + answer);
}
divided(3, 4);
```

# Basic functions

If you start out with an empty index.html file like so:

```HTML
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>An empty page</title>
    <script src="script.js" defer></script>
</head>

<body>

</body>



</html>
```

And then have a `script.js` script, you can then utilize Atom;s atom-live-server to begin playing around.

Things to remember:
- even if you have no assigned variables, you can still have them in the function since it is just being stored in memory
- as long as you define the variables before calling the function it should work fine

```javascript
function findBiggestFraction() {
  // console.log("The function is running!");
  a > b ? console.log("a:  ", a) : console.log("b:  ", b);
}
var a = 3/4;
var b = 5/7;
findBiggestFraction();
```

# Function Arguments

The prior code does not allow for multiple reuse of the function. Therefore, it is wise to implement arguments.

It is very simple and can be done like this:

```javascript
function findBiggestFraction(a, b) {
  // console.log("The function is running!");
  a > b ? console.log("a:  ", a) : console.log("b:  ", b);
}
var fraction1 = 3/4;
var fraction2 = 5/7;
findBiggestFraction(fraction1, fraction2);
findBiggestFraction(3/8, 7/16);
```

You now have a reusable function. This makes your code leaner and easier to maintain.

# Returning Values From A Function

There are many instances where you need data calculated and then returned.

1. setup a variable in your function that will store the data you want to return
2. do your calculations and assign what needs to be returned to said variable
3. return the variable
4. use the returned data as you need

Here is an example of what this may look like:

```javascript
function findBiggestFraction(a, b) {
    // console.log("The function is running!");
    //a > b ? console.log("a:  ", a) : console.log("b:  ", b);
    var result;
    a>b ? result = ['firstFraction', a] : result = ['firstFraction', b];
    return result
}
var fraction1 = 3/4;
var fraction2 = 5/7;
var fracResult = findBiggestFraction(fraction1,fraction2);
console.log(fracResult)
```

Or to make this a bit easier to see what's happening ...

```javascript
function findBiggestFraction(a, b) {
    // console.log("The function is running!");
    //a > b ? console.log("a:  ", a) : console.log("b:  ", b);
    var result;
    a>b ? result = ['firstFraction', a] : result = ['firstFraction', b];
    return result
}
var fraction1 = 3/4;
var fraction2 = 5/7;
var fracResult = findBiggestFraction(fraction1,fraction2);
// console.log(fracResult);
console.log('1st fraction result:  ' + fraction1);
console.log('2nd fraction result:  ' + fraction2);
console.log("Fraction " + fracResult[0] + " with a value of " + fracResult[1] + " is the biggest!");
```

# Working With Anonymous Functions

Unlike named functions, there is no name with which to refer to this function. Therefore they need to be tied to something such as a variable or event.

Using the same need as above, we will re-write this for an anonymous function.

```javascript
var frac1 = 5/7;
var frac2 = 18/25;

// where we hold the anonymous function
var theBiggest = function() {
    var result;
    frac1 > frac2 ? result = ['firstFraction', frac1] : result = ['secondFraction', frac2];
    // console.log(result);
    return result
}

// call teh anonymous function
// theBiggest();
console.log(theBiggest());
```

If you are looking to use arguments in your anonymous function, it's basically the same as before.

```javascript
var frac1 = 5/7;
var frac2 = 18/25;

// where we hold the anonymous function
var theBiggest = function(frac1, frac2) {
    var result;
    frac1 > frac2 ? result = ['firstFraction', frac1] : result = ['secondFraction', frac2];
    // console.log(result);
    return result
}

// call teh anonymous function
// theBiggest();
console.log(theBiggest(frac1, frac2));
console.log(theBiggest(7/9, 13/25));
```

# Immediately Invoking Functional Expressions

What happens is you were to run:

```javascript
var theBiggest = function(a,b) {
    var result;
    a>b ? result = ["a", a] : result = ["b", b];
    return result;
}

console.log(theBiggest);
```

There will be times when you will want to hookup anonymous functions to events. In that instance, you will want the function returned - not the result of it.

How do you populate a variable with the result of an anonymous function?
By running an immediately invoked function expression that runs as soon as the browser encounters it.

How to change an anonymous function to an invoked expression:
1. wrap the function in parenthesis
2. take the inputs from original function call and put in parenthesis following the function

The way the computer now sees this is:
- I have a variable
- Variable is assigned an immediately invoked function expression
- I will run the function now with the arguments at the end
- Return result back into variable

```javascript
var theBiggest = (function(a,b) {
    var result;
    a>b ? result = ["a", a] : result = ["b", b];
    return result;
})(7/9,13/25)

console.log(theBiggest);
```

One of the drawbacks to this is that if you want to use variables instead of hard coded data for the inputs, they must be declared before the immediately invoked function expression.

Test it out with this code:

```javascript
var theBiggest = (function(a,b) {
    var result;
    a>b ? result = ["a", a] : result = ["b", b];
    return result;
})(item1, item2)

var item1 = 7/9;
var item2 = 13/25;

console.log(theBiggest);
```

What are the benefits to using an immediately invoked function expression?
- runs immediately where located in code & produces a direct output
- unaffected by code further down the script
- great for quickly populating a variable or argument in a larger function or property in an object
- often hooked to event listeners for an immediate output

But will need to ensure you are aware of how to structure your script, as it could cause unintended results.

# Variable Scope

Your scope is what determines where in your code that your variable is available for use. The location of your declaration is what decides where it can be used.

When you declare a variable in the root of your script independently outside of a function, this is referred to as **global** scope. You can access this from anywhere in the script. If you make a change to that variable in some function, it changes it for everything that uses the variable.

When you declare a variable within a function, this is your **local** scope. It is only available within that function.

In this example, you will get an error because `result` is a local variable to the function.

```javascript
function findBiggestFraction(a,b) {
    console.log("Fraction a: ", firstFraction);
    console.log("Fraction b: ", secondFraction);

    var result;

	a>b ? result = ["a",a] : result = ["b",b];
    return result;
}

var firstFraction = 7/16;
var secondFraction = 13/25;

var fractionResult = findBiggestFraction(firstFraction,secondFraction);
console.log("Fraction " + fractionResult[0] + " with a value of " + fractionResult[1] + " is the biggest.");

console.log(result);
```

## Why Not Make All Variables Global?

This makes a variable far less useful and introduces opportunity for incorrect results and bugs.

Local variables are basically temporary containers of data. They exist only as long as the function runs. Therefore, they are not just sitting there taking up space when not needed.

Local variables also allow for you to reuse the names again without fear of causing a negative impact, like it would for globals.

**NOTE:** if you do not include `var` when creating a variable within a function, JavaScript will denote it as a **global** variable. Thsi can cause a lot of confusion, so be sure to declare your variables properly!

# ES2015:  let and const

2 new declarations were introduced with ECMAScript 2015.

1. `const` is a constant declaration, so a variable cannot be changed once defined. Can be useful when performing math equations or if you have some value you need to stay the same. (Regardless of what happens in your script.)
    
    If you try to change a constant, your script breaks.

    ```javascript
    // example of what happens when you try to change a constant
    const MYCONSTANT = 5;
    console.log(MYCONSTANT);
    MYCONSTANT = 6;
    ```
    
    **NOTE:** for consistency, ensure that your constant variable names are in all caps.

2. `let` is a block scope variable (smaller scope than just `var`)
    
    Before using let ...
    ```javascript
    // this does not create a new var in the nested if
    function logScope() {
        var localVar = 2;
        if (localVar) {
            var localVar = "I'm different!"
            console.log("nested localVar:  ", localVar)
        }
        console.log("logScope localVar:  ", localVar)
    }
    logScope();
    ```
    
    When using let ...
    ```javascript
    // this creates a new var in the nested if with same name as outer variable
    function logScope() {
        // var localVar = 2;
        let localVar = 2;
        if (localVar) {
            // var localVar = "I'm different!"
            let localVar = "I'm different!"
            console.log("nested localVar:  ", localVar)
        }
        console.log("logScope localVar:  ", localVar)
    }
    logScope();
    ```
    
    This will also work if you have the initial outer function variable be `var` with the nested being `let` ...
    
    ```javascript
    function logScope() {
        var localVar = 2;
        // let localVar = 2;
        if (localVar) {
            // var localVar = "I'm different!"
            let localVar = "I'm different!"
            console.log("nested localVar:  ", localVar)
        }
        console.log("logScope localVar:  ", localVar)
    }
    logScope();
    ```
    
    However if you try to use `let` at the beginning and then the nested variable be declared as `var` you will receive an error.
    
    ```javascript
    function logScope() {
        // var localVar = 2;
        let localVar = 2;
        if (localVar) {
            var localVar = "I'm different!"
            // let localVar = "I'm different!"
            console.log("nested localVar:  ", localVar)
        }
        console.log("logScope localVar:  ", localVar)
    }
    logScope();
    ```
    
    So to wrap this up, `let` allows you to limit the scope of a variable to a particular code block.

# Objects In JS

JS is an OOL (object oriented language) but is considered "sloppy" by most other languages' standards. This is not a bug.

Objects are used when we want to create a cluster of related data for something and perform some actions or operations on that data.

Objects are data models that allow us to combine properties and methods for a specific data set in a structured way.

Using an object, you can setup a model and then create custom methods to be used on any defined sub-object for it.

## Creating An Object & Accessing It's Properties

1. declare a new object:  `var varName = new Object();`
2. setup the object properties (variables associated with object) using dot notation

Here is an example of "long hand":
```javascript
var car = Object();

car.color = "red";
car.wheelDrive = "auto";
car.make = "Toyota";
car.model = "Corolla";
car.yearMade = 2015;
car.yearBought = 2018;

console.log(car);
```

Here is an example of "short hand":
```javascript
var car = {
    color: "red",
    wheelDrive: "auto",
    make: "Toyota",
    model: "Corolla",
    yearMade: 2015,
    yearBought: 2018,
}

console.log(car);
```

You can then specify a specific property by using dot notation such as:  `console.log(car.make)`

## Object Methods

Objects can also contain methods, or functions taht use the change of data in the object properties.

```javascript
var car = {
    color: "red",
    wheelDrive: "auto",
    make: "Toyota",
    model: "Corolla",
    yearMade: 2015,
    yearBought: 2018,
    milesDriven: 42,
    updateMiles:  function(miles) {
        car.milesDriven += miles;
        return car.milesDriven;
    }
}

console.log(car);
console.log(car.milesDriven)
car.updateMiles(102);
console.log(car.milesDriven);
```

## Object Constructors

In the above code, we had to explicitly define every property and method within an object. This is not efficient nor effective if you want several objects. **Object constructors** allow you to fix this.

**Object constructors** are templates for creating objects. They are defined ONCE and can then be called (instantiated) multiple times.

Here is the process to create an **object constructor**:
1. define a function for your object and name it starting with a capital letter
2. add the names of the attributes as the "inputs"
3. set the default of the attributes using `this`
4. functions are setup the same way

```javascript
function Car(color,wheelDrive,make,model,yearMade,yearBought,milesDriven) {
    this.color = color;
    this.wheelDrive = wheelDrive;
    this.make = make;
    this.model = model;
    this.yearMade = yearMade;
    this.yearBought = yearBought;
    this.milesDriven = milesDriven;
    this.updateMiles = function(miles) {
        this.milesDriven += miles;
        return this.milesDriven;
    }
}

var car1 = new Car("red","auto","Toyota","Corolla",2015,2018,42)

console.log(car1);
console.log(car1.milesDriven)
car1.updateMiles(102);
console.log(car1.milesDriven);

var car2 = new Car("white","auto","Honda","Fit",2015,2016,42)
console.log(car2);
```

Once you have created the constructor you are now able to have multiple unique instances of the class object.

And you can then populate an array of said objects!

```javascript
function Car(color,wheelDrive,make,model,yearMade,yearBought,milesDriven) {
    this.color = color;
    this.wheelDrive = wheelDrive;
    this.make = make;
    this.model = model;
    this.yearMade = yearMade;
    this.yearBought = yearBought;
    this.milesDriven = milesDriven;
    this.updateMiles = function(miles) {
        this.milesDriven += miles;
        return this.milesDriven;
    }
}

var cars = [
    new Car("red","auto","Toyota","Corolla",2015,2018,42),
    new Car("white","auto","Honda","Fit",2015,2016,42),
]
console.log(cars);
console.log(cars[1].make + " " + cars[1].model)
```

## Dot Notation & Bracket Notation

**dot notation** is where you have `objectName.property` to get the property within an object.

**bracket notation** is similar to **dot notation** but the structure is:  `objectName["property"]`

The reason to know the different is because something the properties may have strange characters within them. Using **bracket notation** would ensure that you don't run into any issues that **dot notation** would cause with that example. (It is entirely possible that when parsing JS thinks you are trying to do something else.)

_What do you think would happen if there was a property like this:  **WP:image**_

## Closures

A **closure** is a function within a function that relies on variables in the outside function to work.

Take for example this bit of code:
```javascript
function doSomeMath() {
    var a = 5;
    var b = 4;
    var sum = a + b;

    return sum;
}

var theResult = doSomeMath();

console.log("The result: ", theResult);
```

Let's change it so that we have a **closure** for multiplication.

```javascript
function doSomeMath() {
    var a = 5;
    var b = 4;
    // var sum = a + b;
    // return sum;

    function multiply() {
        var result = a*b;
        return result;
    }
    return multiply; // this returns the function
}

var theResult = doSomeMath();

console.log("The returned function: ", theResult);
console.log("The result: ", theResult());
```

What do you see from the outcome?

**NOTE:** There is a lot more to **closures** than this, so be sure to [check this out](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).