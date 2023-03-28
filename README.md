# DailyPlate
Meal plan generator with nutritional and budgeting information

# API Functions


### generate meal plan
```python
def generate_mealplan(preferences='no preferences', num_meals=7) -> dict:
```
Preferences: str - The prompt to feed to chatgpt \n
Num_meals: int - the number of meals to return \n
*returns* meals: Dict - a dictionary/ json object containing the meal data
  
### construct prompt

```python
def construct_prompt(template_path: int, liked_meals: list) -> str:
```

template_paths: str - the path to the text file containg a template prompt to sent to chatgpt \n
liked_meals: list - a list of titles referring to meals liked by the user \n
*returns* prompt: str - string prompt that we use to ask for meals/recipes

### nutritional_information

```python
def nutritional_information(items: list) ->  dict:
```
items - list of ingredients to fetch nutritional information on (prolly just joules and calories or something like that

### calculate_BMI

```python 
def calculate_BMI(height: float, weight: float) -> float: # frick the imperial system (we use kg and cms)
```



