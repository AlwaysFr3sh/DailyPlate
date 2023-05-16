import requests
import json
import logging

logger = logging.getLogger("edamam")
##url -X GET --header "Accept: application/json" "https://api.edamam.com/api/nutrition-data?app_id=28946ca6&app_key=461321ba662873bae755da28b1c67945&nutrition-type=cooking&ingr=carrot"

app_id= "7528744b"
app_key= "9d0aeab544b738d42bfa62125a86a94b"
    
def get_nutritional_info(food_item):
    base_url = 'https://api.edamam.com/api/nutrition-data'
    params = {
    'app_id': "28946ca6",
    'app_key': "21f380c94135357b124aa67bf7d6db84",
    'nutrition-type':"logging",
    'ingr': food_item
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        
        print(data)
            
        return None
    # result = get_nutritional_info(ingredient)

    # if result:
    #     print("Nutritional Information:")
    #     print("Calories:", result['calories'])
    #     print("Protein:", result['totalNutrients']['PROCNT']['quantity'], result['totalNutrients']['PROCNT']['unit'])
    #     print("Carbohydrates:", result['totalNutrients']['CHOCDF']['quantity'], result['totalNutrients']['CHOCDF']['unit'])
    #     print("Fat:", result['totalNutrients']['FAT']['quantity'], result['totalNutrients']['FAT']['unit'])
    # else:
    #     print("Failed to retrieve nutritional information.")