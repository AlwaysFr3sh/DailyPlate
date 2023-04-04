# utilities.py

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
def construct_prompt(prompt_template_path:str, liked_meals:list, num_meals=7) -> str:
  with open(prompt_template_path) as f:
    prompt = "".join(f.readlines())

  return prompt

