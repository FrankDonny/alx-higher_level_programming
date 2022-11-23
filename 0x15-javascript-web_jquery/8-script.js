const url = "https://swapi-api.hbtn.io/api/films/?format=json"
fetch(url).then(response => response.json())
  .then(data => {
    let dat = data['results']
    for (let i = 0; i < dat.length; i++){
      $("UL#list_movies").append(`<li>${dat[i]['title']}</li>`)
    }
  })