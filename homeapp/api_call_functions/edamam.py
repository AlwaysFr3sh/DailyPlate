import requests
import json
import logging
import exceptions as e1
logger = logging.getLogger("edamam")

class edamam(object):
    app_id= "7528744b"
    app_key= "9d0aeab544b738d42bfa62125a86a94b"
    def __init__(self,
                 recipes_appkey=None,
                 food_appid="7528744b",
                 food_appkey="9d0aeab544b738d42bfa62125a86a94b"
                 
                 ):
        self.food_appid = food_appid
        self.food_appkey = food_appkey
    def search_food(self, query="pizza"):
        url = "https://api.edamam.com/api/food-database/v2/parser" \
              '-type=logging&ingr={query}&app_id={id}&app_key={key}' \
            .format(id=self.food_appid, key=self.food_appkey, query=query)

        r = requests.get(url)
        if r.status_code == 401:
            logger.error("invalid food api key")
            raise e1.InvalidFoodApiKey

        r = r.json()
        if r.get("status") == "error":
            error = r.get("message")
            if not error:
                error = "Api request failed"
            logger.error(error)
            raise e1.APIError 
        return r