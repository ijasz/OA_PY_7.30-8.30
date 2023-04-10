// Function Statement / Declaration
function greeting(a) {
  console.log("hello " + a);
}

greeting("anbarasan");
greeting("barath");
console.log("---");
greeting("ocean");

function showName() {
  console.log(window.document.querySelector("h1"));
  window.document.querySelector("h1").textContent = "hello anbarasan";
}
