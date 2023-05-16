function generateRecipe() {
    var personal_recipes = document.getElementById("personal_recipes");
    var ticket = document.createElement("div");


    ticket.innerHTML =   '<div class="loader"><div class="ball1"></div><div class="ball2"></div><div class="ball3"></div></div>';
    ticket.className = "recipe_preview"
    personal_recipes.appendChild(ticket);


    var btn = document.getElementById("generate_recipe_btn");
    btn.disabled=true;
    btn.innerHTML="Loading...";   



    $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url: '/home/generate/',
        method: 'get',
        data: {},
        success: function(response) {
          console.log(response)
          ticket.innerHTML = "";
          var title = document.createElement("a");
          var status = document.createElement("p");    
          ticket.appendChild(title);
          ticket.appendChild(status);
          title.innerHTML = response['title'];
          title.href = "/home/recipe/" + response['pk'];
          status.innerHTML = 'Status: New';
          btn.disabled=false;
          btn.innerHTML="Generate a new meal!";   
        },
        error: function(error) {
          console.log(error)
        }
    });
}