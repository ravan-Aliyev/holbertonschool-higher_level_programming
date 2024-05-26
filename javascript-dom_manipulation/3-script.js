let header = document.querySelector("header");
let toggle = document.querySelector("#toggle_header");

function toggleColor(first, second) {
    header.classList.remove(first);
    header.classList.add(second);
}

toggle.addEventListener("click", function(){
    header.classList.contains("green") ? 
    toggleColor("green", "red") : 
    toggleColor("red", "green")
});