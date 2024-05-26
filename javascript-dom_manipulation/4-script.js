let item = document.querySelector("#add_item");
let list = document.querySelector(".my_list");

item.addEventListener("click", () => {
  let li = document.createElement("li");
  
  li.innerText = "Item";
  list.appendChild(li)
});