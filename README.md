# DailyPlate
Meal plan generator with nutritional and budgeting information

# API Functions


```python
generate_mealplan(preferences='no preferences', num_meals=7) -> dict:
```
Preferences: str - The prompt to feed to chatgpt
Num_meals: int - the number of meals to return
returns
  meals: Dict - a dictionary/ json object containing the meal data
