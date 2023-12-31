# utilities.py
import svgwrite

# height is metres and weight is kg, returns bmi to 2 decimal places
def calculate_bmi(height:float, weight:float) -> float:
  return round(weight / (height * height), 2)

def calculate_ingredient_proportions(bmi:float, ingredients:dict) -> dict:
  raise NotImplementedError("idk how this ones supposed to work lmao")

# Construct a prompt to feed to the beast
# TODO: num_meals might be useless if we can't engineer a prompt to get output in a reliable format
#       structure, if that is the case we will have to get multiple meals by making the openai
#       api call x times. 
# TODO: edit prompt to provide preference information in the form of meals that the user likes
#       we will need to limit the maximum number of liked meals we provide. 
def construct_prompt(prompt_template_path:str, disliked_ingredients:list[str]=[], meal_history:list[str]=[], bmi:float=22.9) -> str:
  with open(prompt_template_path) as f:
    prompt = "".join(f.readlines())

  prompt = prompt.replace("<prev_meals>", ", ".join(meal_history))
  prompt = prompt.replace("<disliked_ingredients>", ", ".join(disliked_ingredients))
  prompt = prompt.replace("<user_bmi>", str(bmi))

  return prompt

def read_file(path):
  with open(path) as f: text = f.readlines()
  return "".join(text).replace("\n", "") 

import svgwrite

def generate_profile_picture(username, size=200, initials_font_size=80):
    # Create a new SVG drawing
    dwg = svgwrite.Drawing(filename="profile_picture.svg", size=(size, size))

    # Set the background color of the SVG
    dwg.add(dwg.rect(insert=(0, 0), size=(size, size), fill='lightgray'))

    # Calculate the position of the initials
    initials_x = size / 2
    initials_y = size / 2

    # Create the text element for the initials
    initials = username[0].upper()  # Take the first two characters as initials
    dwg.add(dwg.text(initials, insert=(initials_x, initials_y),
                     text_anchor="middle", font_size=initials_font_size, fill='white'))

    # Save the SVG to a file
    dwg.save()



  

if __name__ == "__main__":
  #disliked_ingredients = ["peas", "corn"]
  #meal_history = ["spaghetti", "tortellini"]
  #print(construct_prompt("../dailyplate/prompts/prompt5.txt", disliked_ingredients=disliked_ingredients, meal_history=meal_history))

  # Example usage
  username = "JohnDoe"
  generate_profile_picture(username)