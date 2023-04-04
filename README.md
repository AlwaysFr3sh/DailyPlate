# DailyPlate
Meal plan generator with nutritional and budgeting information

# API Functions

### generate meal plan
```python
def generate_mealplan(prompt='food please') -> dict:
```
Preferences: str -> The prompt to feed to chatgpt

*returns* meals: Dict -> a dictionary/ json object containing the meal data
  
### nutritional_information
```python
def nutritional_information(ingredients: list) ->  dict:
```
ingredients - list of ingredients to fetch nutritional information on (prolly just joules and calories or something like that

### get_ingredient_prices
```python
def get_ingredient_prices(ingredients: list) -> dict:
```
ingredients: list -> list of ingredients to retrieve prices for

*returns* prices: dict -> {ingredient : price} where ingredient is a string describing the ingredient and prices is a float representing gpb's

# Utility Functions

### calculate_BMI
```python 
def calculate_BMI(height: float, weight: float) -> float: # frick the imperial system (we use kg and cms)
```

### calculate_ingredient_proportions
```python
calculate_ingredient_proportions(bmi: float, ingredients: list) -> dict:
```
bmi: float -> bmi value

ingredients: list -> list of ingredients: str

**returns** Dictionary of ingredient proportions {ingredient : {proportion : Unit of Measure}}

### construct prompt
```python
def construct_prompt(template_path: int, liked_meals: list, num_meals=7) -> str:
```
template_paths: str - the path to the text file containg a template prompt to sent to chatgpt 

liked_meals: list - a list of titles referring to meals liked by the user

Num_meals: int - the number of meals to return

*returns* prompt: str - string prompt that we use to ask for meals/recipes


