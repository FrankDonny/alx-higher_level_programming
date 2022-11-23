// const cors = require("cors")
$(document).ready(function (){
  const url = "https://fourtonfish.com/hellosalut/?lang=fr"
  fetch(url).then(response => response.json()).then(data => {
    $("#hello").append(`<p>${data.hello}</p>`)
  })
})