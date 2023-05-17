function generateRecipe() {
    var personal_recipes = document.getElementById("personal_recipes");
    var cardlink = document.createElement("a");
    var recipe_preview = document.createElement("div");
    cardlink.append(recipe_preview);
    cardlink.className = "cardlink";
    recipe_preview.innerHTML = '<div class="loader"><div class="ball1"></div><div class="ball2"></div><div class="ball3"></div></div>';
    recipe_preview.className = "recipe_preview";
    personal_recipes.prepend(cardlink);

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
          recipe_preview.innerHTML = "";
          var title = document.createElement("p");
          var status = document.createElement("p");    
          title.className = "recipe_title";
          recipe_preview.appendChild(title);
          recipe_preview.appendChild(status);
          title.innerHTML = response['title'];
          //title.href = "/home/recipe/" + response['pk'];
          cardlink.href = "/home/recipe/" + response['pk'];
          status.innerHTML = 'Status: New';
          btn.disabled=false;
          btn.innerHTML="Generate a new meal!";   
        },
        error: function(error) {
          console.log(error)
        }
    });
}