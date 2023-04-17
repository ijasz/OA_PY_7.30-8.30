const doc = document;

function counter(c) {
  const value = doc.querySelector("h1");
  if (c === "increament") value.innerText = Number(value.innerText) + 1;
  else if (c === "decreament" && Number(value.innerText) > 0)
    value.innerText = Number(value.innerText) - 1;
  else value.innerText = 0;
}
