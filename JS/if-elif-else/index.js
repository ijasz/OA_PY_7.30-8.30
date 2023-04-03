// console.log("hello");

const user = Number(prompt("enter your age"));

if (user >= 18) {
  console.log("eligible for voting");
} else if (isNaN(user)) {
  console.log("invalid statement");
} else {
  console.log("not eligible for voting");
}
