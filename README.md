# DailyPlate
Meal plan generator with nutritional and budgeting information

# API Functions


### generate meal plan
```python
generate_mealplan(preferences='no preferences', num_meals=7) -> dict:
```
Preferences: str - The prompt to feed to chatgpt \n
Num_meals: int - the number of meals to return \n
*returns* meals: Dict - a dictionary/ json object containing the meal data
  
### construct prompt

```python
construct_prompt(template_path: int, liked_meals: list 
```

template_paths: str - the path to the text file containg a template prompt to sent to chatgpt \n
liked_meals: list - a list of titles referring to meals liked by the user \n
*returns* prompt: str - string prompt that we use to ask for meals/recipes


