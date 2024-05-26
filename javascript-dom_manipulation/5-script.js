let header = document.querySelector("header");
let update_header = document.querySelector("#update_header");

update_header.addEventListener("click", () => {
  header.innerText = "New Header!!!";
});