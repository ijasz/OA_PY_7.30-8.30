// Destructuring

const a = [1, 2, 3, 4];
const b = [5, 6];
const c = [0, ...a, -5, ...b, 7, 8];

const [value1, , value3, ...r] = a;

console.log(value1);
console.log(value3);
console.log(r);
