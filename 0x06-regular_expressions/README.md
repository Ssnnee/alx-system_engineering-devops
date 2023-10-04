# Regular expression


## Description
This directory is about regex.
#### What is regeular expression ?
A regular expression, often referred to as regex or regexp, is a pattern that specifies a set of strings. It's a powerful tool used in computer science and programming for searching, matching, and manipulating text based on patterns.

Here an example of a simple regex :

```
/ex/
```
Yes, that's my `ex`uberant `ex`pression
This will basically match with the highlighted letters.

Here a simple Javascript way to use regex. You can paste in your console
```
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

const email1 = "example@email.com";
const email2 = "invalid-email";

console.log(emailRegex.test(email1)); // true
console.log(emailRegex.test(email2)); // false
```
