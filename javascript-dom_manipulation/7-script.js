const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

function fetchTitle(){
  fetch(apiUrl)
  .then(response=>{
    if(!response.ok){
      throw new Error("Error");
    }
    return response.json();
  })
  .then(data => {
    let listMovies = document.querySelector("#list_movies");
        
    data.results.forEach(film => {
      let movie = document.createElement("li");
        
      movie.innerHTML = film.title;
      listMovies.appendChild(movie);
    })
  })
  .catch(error=>{
    console.log(error);
  })
}

fetchTitle();
