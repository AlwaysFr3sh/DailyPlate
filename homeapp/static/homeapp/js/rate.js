    const starwrapper = document.querySelector(".stars");
    const stars = document.querySelectorAll(".stars a");
    stars.forEach((star, clickedidx) => {
      star.addEventListener("click", () => {
        var rating = clickedidx+1
        if(confirm("Rate this recipe " + rating + " stars?")){
          //disable stars
          stars.forEach((otherstar, otheridx) => {
            if (otheridx <= clickedidx){
              otherstar.classList.add("active");
            }
          });
          //

          $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: '/home/rate/',
            method: 'post',
            data: {
              recipeID: recipeID,
              newRating: rating
            },
            success: function(response) {
              console.log(response)
              starwrapper.classList.add("disabled");
              document.getElementById("rate_message").innerHTML = "Thanks for your feedback!";
            },
            error: function(error) {
              
              console.log(error)
            }
          });
        }        
      });
    });