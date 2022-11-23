$(function (){
  $("#add_item").click(function () {
    const newItem = "<li>Item</li>"
    $("UL.my_list").append(newItem)
  })

  $('#remove_item').click(function () {
    let list = $('ul.my_list li');
    if (list.length > 0) {
      list[list.length - 1].remove();
    }
  });

  $("#clear_list").click(function (){
    $("UL.my_list li").remove()
  })
})


// document.addEventListener("DOMContentLoaded", function (){
//   const add = document.querySelector("#add_item")
//   add.addEventListener("click", function (){
//     const li = document.createElement("li")
//     li.innerText = "Item1"
//     const appending = document.querySelector("UL.my_list")
//     appending.appendChild(li)
//   })
//   const remove = document.querySelector("#remove_item")
//   remove.addEventListener("click", function (){
//     const ul = document.querySelector("UL.my_list li")
//     ul.remove()
//   })
//
//   const clear = document.querySelector("#clear_list")
//   clear.addEventListener("click", function (){
//     const ul = document.querySelector("UL.my_list")
//     ul.remove()
//   })
// })