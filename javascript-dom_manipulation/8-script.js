const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

function fetchLang(){
  fetch(apiUrl)
  .then(response=>{
    if(!response.ok){
      throw new Error("Error");
    }
    return response.json();
  })
  .then(data => {
    let text = document.querySelector("#hello");
    
    text.innerHTML = data.hello;
  })

  .catch(error=>{
    console.log(error);
  })
}

fetchLang();
