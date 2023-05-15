function generateRecipe() {

    var personal_recipes = document.getElementById("personal_recipes");
    var ticket = document.createElement("div");
    var title = document.createElement("a");
    var status = document.createElement("p");
    status.innerHTML = 'Loading...';         
    ticket.className = "recipe_preview"
    ticket.appendChild(title);
    ticket.appendChild(status);
    personal_recipes.appendChild(ticket);


    $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url: '/home/generate/',
        method: 'get',
        data: {},
        success: function(response) {
          console.log(response)
          title.innerHTML = response['title'];
          title.href = "/home/recipe/" + response['pk'];
          status.innerHTML = 'Status: New';          
        },
        error: function(error) {
          console.log(error)
        }
    });
    
}
