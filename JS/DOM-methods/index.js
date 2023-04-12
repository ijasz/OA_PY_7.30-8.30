console.log(window.document.head);
console.log(window.document.body);

// For Accessing HTML element

console.log(document.getElementsByTagName("h1")); //returns array
console.log(document.getElementsByClassName("heading")); //returns array
console.log(document.getElementById("h"));
console.log(document.getElementsByName("heading1")); //returns array
console.log(document.querySelector("body > .heading")); //returns array
console.log(document.querySelectorAll("body > .heading")); //returns array

// best practice

const doc = document;

const h1 = doc.querySelector("body > .heading");
const h1Style = doc.querySelector("body > .heading").style;

// style
// property - camelCase

h1Style.color = "white";
h1Style.fontSize = "50px";
h1Style.backgroundColor = "black";
h1Style.textAlign = "center";
