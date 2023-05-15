function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
    
    
    
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