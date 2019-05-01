<a href='https://www.learntocodeonline.com/'>![Learn To Code Online By Clicking Here](..\IMGs\learn-to-code-online.png?raw=true "Learn To Code Online")</a>

# Table Of Contents

1. [Introduction to JavaScript](01_Intro_to_JS.MD)
2. [JavaScript Basics](02_JS_Basics.MD)
3. [Working With Data](03_Working_With_Data.MD) (_you are here_)
    - [Variables](#variables)
    - [Data Types](#data-types)
    - [Operators](#operators)
    - [Working With Strings & Numbers](#working-with-strings--numbers)
    - [Logic And Conditional Statements](#logic-and-conditional-statements)
    - [Arrays](#arrays)
4. [Functions & Objects](04_Functions_Objects.MD)
5. [JS & The Dom:  Changing The Elements](05_JS_Dom_ChangingElements.MD)
6. [JS & The Dom:  Events](06_JS_Dom_Events.MD)
7. [Loops](07_JS_Loops.MD)
8. [Troubleshooting, Validating, Minifying JS](08_JS_TVM.MD)
9. [Project Ideas](99_Project_Ideas.MD)
10. [Project Answers](99_Project_Ideas_ANSWERS.MD)

# Variables

The power of programming lies in our ability to perform the same operation on many different objects... Or change that object over and over.

We create "storage containers" (variables) that hold these objects until we need them. This "container" holds whatever data we put into it.

You create a variable with this format:  `var varName;`

The variable name can be **anything** as long as it's written with:
- letters
- numbers
- underscores
- a dollar sign
- no spaces

Remember that it is case sensitive and **must** start with a letter!

By default, a variable (container) is empty or undefined. You must then assign something to it.

**Assignment Option 1**

```javascript
var a;
a = 4;
```

**Assignment Option 2**

```javascript
var b = 5;
```

**Assignment Option 3**

You can create and assign multiple variables at once.

```javascript
var a = 4, b = 5;
```

## Things To Remember About Variables

You could potentially not declare a variable before assigning it, however this can cause issues later on with scope. Without the `var` prefix, then the new variable is given a **global** scope and can be accessed by any function.

**Rule Of Thumb:** any time you create a variable, always declare it to avoid global scope.

JS is a weakly-typed language. Therefore, you do not have to declare a type of data that will go into a variable.

# Data Types

There are 6 primitive (built in) data types that can be stored in a variable.

If you wish to determine the type of data a variable holds, you can use the `typeof` operator to find out.

```javascript
var tempStr = "this is temporary";
console.log(typeof tempStr);
```

1. numeric

    Handles numbers, whether positive, negative, whole, or float.
    
    There is a limit to how big the number can be, but it is CRAZY high.
    
2. string

    Handles concurrent letters and symbols as a "string" type - or words and sentences.
    
    These are wrapped in straight quotation marks (single or double) like:
    - `"This is a string."`
    - `'This is also a string.'`
    
    If you wish to use the same quotes within the same string, you need to use a `\` to escape it.
    - `"Here is an example where I wish to provide a quote in a string. \"Watch me.\""`
    - `'Here is another example where I wish to provide a quote in a string. \'Watch me.\''`

3. boolean

    This handles the boolean of **true** or **false**.
    
    ```javascript
    var theSunIsWarm = true;
    var theMoonIsMadeOfCheese = false;
    ```

4. null (used occasionally)

    This data type is the intentional absence of an object value. This allows a variable to be empty but not `undefined`.
    
    `var emptyInside = null;`

5. undefined (fallback)

    This is when you create a variable but don't assign anything to it.
    
    `var testVar;`

6. symbol (introduced in ECMA2015)

# Operators

Operators take some data, do something with it, and then put results back. These operators look familiar but don't always do what you might expect.

1. Assignment Operator:  `=`

    When you see this, you can read `var a = 4;` as:    _variable 'a' is assigned the value of 4_

2. Arithmetic Operators

    - `=`
    - `+`
    - `-`
    - `*`
    - `/`
    
    These are used like typical math operators.
    
    JS follows typical Algebra rules, so be sure to follow operator precedence.

3. Shorthand Math

    This allows for calculation and assignment.
    
    - `+=`
    - `-=`
    - `*=`
    - `/=`
    
    For example:
    ```javascript
    var a = 4;
    a += 4;
    // a will now be 8
    ```
    
    You can also use **unary operators** to increase or decrease by 1.
    ```javascript
    var a = 5;
    a = a + 1; // long form version
    a++; // short hand unary increase
    a = a - 1; // long form version
    a--; // short hand unary decrease
    ```
    
    You could do `++varName` instead of `varName++` to get the same result, but in a different order.
    
    ```javascript
    var a = 1;
    console.log(++a); // will print out 2 but will not assign to a
    console.log(a++); // will print out 2 and assign to a
    console.log(a); // will print out 2 because it was assigned the 2nd time
    ```

# Working With Strings & Numbers

If you try to combine a string with an integer, JS automatically assumes it needs to concatenate 2 strings.

```javascript
var a = 4;
var b = "5";
var sum = a + b; // this will assign "45" to sum
```

Therefore a number will be converted to a string when attempting to "add" or concatenate a string and numbers.

JS is a bit tricky in this. If you use `-` it will work as long as the string is a number. Otherwise a `NaN` error will occur to indicate that it is not a number.

# Logic And Conditional Statements

A lot of programming is about testing for conditions. Once some logic is met, it runs a particular code block.

1. Conditional **if** Statement

    ```javascript
    if (some condition) {
        Do something.
    }
    ```
    
    The piece inside the parenthesis are the condition block, which must evaluate to `true` to enter the code block within the curly braces.
    
    Need additional conditions? No problem.
    
    ```javascript
    if (some condition) {
        Do something.
    } else {
        Do something else.
    }
    ```

2. Conditional Operators

    These operators are what is used to evaluate the expression for a condition.
    
    One to keep in mind is equality `==` since a single `=` will assign the data to a variable. And anything non 0 or non null is seen as `true`.
    
    If you want to restrict comparison so that the contents are exactly the same, you will use `===` instead.
    
    ```javascript
    var a = 5;
    var b = "5";
    var theNumbersMatch;
    if (a === b) {
        theNumbersMatch = true;
    } else {
        theNumbersMatch = false;
    }
    console.log("The numbers match:  " + theNumbersMatch);
    // returns false because not both number 5
    // would return true if a == b
    ```
    
    You generally would like ot give JS some wiggle room so `==` is preferred, however there may be reasons to require the `===` comparison.

3. Less Than or Greater Than

    Less than `<` or Greater Than `>` also can be `<=` or `>=` if you wish to see if it also is equivalent.

4. Not

    `!` is the logic condition where a value is **not** something ...
    
    For example:
    ```javascript
    if (a != b) {
        Do something.
    } else {
        Do something else.
    }
    ```

5. Testing Boolean Values

    ```javascript
    if (varName == true) {} // long hand
    if (varName) {} // short hand
    ```
    
    ```javascript
    if (varName == false) {} // long hand
    if (varName != true) {} // reverse psychology
    if (!varName) {} // short hand - literally "not varName"
    ```

## Advanced Logic And Conditional Statements

1. AND vs OR

    There may be times where you wish to string multiple operators together. This is where you would use `AND` as well as `OR` to do so.
    
    ```javascript
    if (a ==b && c == d) {}; // true if both are true
    if (a==b || c==d) {}; // true if at least one is true
    ```
    
2. XOR (which would be one or the other but not both)
    
    This does not exist in JS. Therefore you would need to create it manually by nesting a conditional within a conditional statement.
    
    ```javascript
    if ( (a == b || c == d) && ( (a==b) != (c==d)) {}
    ```

3. Ternary Operator

    ```javascript
    a == b ? console.log("Match" : console.log("No match.");
    ```
    
    - The part before the `?` is the condition:   `a == b`
    - After the `?` and before the `:` this is what is meant to happen if condition is true.
    - After the `:` and before the `;` this is what is meant to happen if condition is false.
    
    This takes up a lot less space than doing the long form. They are not immediately obvious so could make for difficult reading of your code. So if used, be sure to use comments to explain what's going on.

# Arrays

Regular variables are great for storing default data types and single items. But in order to store multiple values or different types of data, you will need to store inside of an `array`.

You can create an array very similar to how you would make a list in python.

```javascript
var pens = ["red", "blue", "orange"];
var mixed = new Array("red", "blue", 5);
```

You can also have arrays within arrays - just like in python.

Each element in the array is given a 0-based index, meaning the 1st item is at index 0. You then call for the element just like in python.

```javascript
var pens = ["red", "blue", "orange"];
var fourthPen = pens[3];
console.log(fourthPen);
```

And just like in python, you can reassign an element in an array:  `pens[0] = "black";`

## Array Properties & Methods

All objects have properties and methods.

**Property** - maintains information about an object we can retrieve and use.

**Method** - function that belongs to an object.

For a full list of array methods, be sure to checkout [this from javascript.info](https://javascript.info/array-methods) or even [this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) from Mozilla developer site.

You can also check out the MDN documentation for arrays [here](https://goo.gl/G4cTqk) (very much like the first link).