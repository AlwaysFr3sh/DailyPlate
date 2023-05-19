from django.test import TestCase

from homeapp.api_call_functions.edamam import get_nutritional_info
from homeapp.api_call_functions.openaiapi import gpt_query
from homeapp.utilities import construct_prompt, calculate_bmi
from homeapp.models import *


class TestUtilityFunctions(TestCase):

    def test_openai(self):
        prompt = construct_prompt("dailyplate/prompts/prompt5.txt",)
        system_prompt = "You are a helpful assistant"
        api_key = "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"
        result = gpt_query(prompt, system_prompt, api_key, temperature=1.0)
        self.assertEqual(type(result),list)
    def test_bmiCalculater(self):
        height = 180
        weight = 80
        test_bmi = round(weight / (height * height), 2)
        bmi = calculate_bmi(height,weight)
        self.assertEqual(bmi,test_bmi)
        self.assertEqual(type(bmi) , float)

    def test_edamam_normalresponse(self):
        x = get_nutritional_info("banana 200g")
        self.assertEqual(type(x),dict)

    def test_edamam_badinput(self):
        x = get_nutritional_info("21")
        self.assertEqual(x['calories'],0)

class TestUser(TestCase):
    def setUp(self) -> None:
        pass

    def test_user(self):
        User.objects.filter(username="test1").delete()
        U1 = User(email="test1@example.com", username="test1")
        U1.set_password('test1')
        with self.assertRaises(Exception): 
            self.assertTrue(User.objects.filter(username="test1").exists())
        U1.save()
        self.assertTrue(User.objects.filter(username="test1").exists())

    def test_repeated_user(self):
        User.objects.filter(username="test1").delete()
        U1 = User(email="test1@example.com", username="test1")
        U1.set_password('test1')
        U1.save()
        UserSettings(user=U1).save()

        U2 = User(email="test1@example.com", username="test1")
        U2.set_password('test1')
        with self.assertRaises(Exception):
            U2.save()


class TestUserSettings(TestCase):
    def setUp(self):

        U1 = User(email="test1@example.com", username="test1")
        U1.set_password('test1')
        U1.save()
        self.settings = UserSettings.objects.create(user=U1)

    def test_add_disliked_food(self):
        self.settings.addDislikedFood('Pizza')
        disliked_foods = self.settings.getDislikedFoods()
        self.assertIn('Pizza', disliked_foods)

    # def test_remove_disliked_food(self):  ## fix thi somehow
    #     self.settings.addDislikedFood('Pizza')
    #     self.settings.addDislikedFood('Burger')
    #     self.settings.removeDislikedFood('Pizza')
    #     disliked_foods = self.settings.getDislikedFoods()
    #     self.assertNotIn('Pizza', disliked_foods)
    #     self.assertIn('Burger', disliked_foods)

    def test_update_height(self):
        new_height = 185.5
        self.settings.updateHeight(new_height)
        self.assertEqual(self.settings.height, new_height)

    def test_update_weight(self):
        new_weight = 75.5
        self.settings.updateWeight(new_weight)
        self.assertEqual(self.settings.weight, new_weight)

    def test_get_bmi(self):
        height = 180
        weight = 80
        self.settings.updateHeight(height)
        self.settings.updateWeight(weight)
        bmi = self.settings.getBMI()
        self.assertAlmostEqual(bmi, calculate_bmi(height,weight), places=2)

    def test_str_representation(self):
        expected_str = f"Height: {self.settings.height}cm Weight: {self.settings.weight}kg Disliked Foods: {self.settings.getDislikedFoods()}"
        self.assertEqual(str(self.settings), expected_str)

class TestSharedDetails(TestCase):
    def setUp(self):
        self.details = sharedDetails.objects.create()

    def test_update_rating(self):
        self.assertEqual(self.details.numRatings, 0)
        self.assertEqual(self.details.currentRating, 0.0)
        new_rating = 4.5
        self.details.updateRating(new_rating)

        self.assertEqual(self.details.numRatings, 1)
        self.assertEqual(self.details.currentRating, new_rating)
        updated_rating = 3.0
        self.details.updateRating(updated_rating)

        self.assertEqual(self.details.numRatings, 2)
        self.assertAlmostEqual(self.details.currentRating, (new_rating + updated_rating) / 2, places=2)

    def test_str_representation(self):
        expected_str = "pk:" + str(self.details.pk) + ", numRatings:" + str(self.details.numRatings) + ", Rating:" + str(self.details.currentRating)
        self.assertEqual(str(self.details), expected_str)

class TestRecipe(TestCase):
    def setUp(self):
        self.user = User(email="test1@example.com", username="test1")
        self.user.set_password('test1')
        self.user.save()

        self.shared_details = sharedDetails(numRatings=1, currentRating=4)
        self.shared_details.save()

        self.settings = UserSettings.objects.create(user=self.user)
        height = 180
        weight = 80
        self.settings.updateHeight(height)
        self.settings.updateWeight(weight)

        JSON1 = {        
            "title": "Spaghetti with Meatballs",
            "ingredients": {
                "spaghetti": {
                    "amount": 500,
                    "unit": "grams",
                    "price": 1.2
                },
                "ground beef": {
                    "amount": 500,
                    "unit": "grams",
                    "price": 4.5
                },
                "bread crumbs": {
                    "amount": 50,
                    "unit": "grams",
                    "price": 0.3
                },
                "milk": {
                    "amount": 50,
                    "unit": "millilitres",
                    "price": 0.2
                },
                "parmesan cheese": {
                    "amount": 50,
                    "unit": "grams",
                    "price": 0.8
                },
                "egg": {
                    "amount": 1,
                    "unit": "quantity",
                    "price": 0.2
                },
                "garlic": {
                    "amount": 2,
                    "unit": "teaspoons",
                    "price": 0.1
                },
                "salt": {
                    "amount": 1,
                    "unit": "teaspoon",
                    "price": 0.05
                },
                "pepper": {
                    "amount": 0.5,
                    "unit": "teaspoon",
                    "price": 0.05
                },
                "olive oil": {
                    "amount": 50,
                    "unit": "millilitres",
                    "price": 0.3
                }
            },
            "instructions": [
                "Cook the spaghetti according to package instructions.",
                "Combine ground beef, bread crumbs, milk, parmesan cheese, egg, garlic, salt, and pepper in a large bowl.",
                "Form mixture into meatballs.",
                "Heat olive oil in a large skillet over medium-high heat.",
                "Add meatballs and cook, turning occasionally, until browned on all sides and cooked through, about 8-10 minutes.",
                "Serve meatballs on top of cooked spaghetti."
            ]
        }
        self.recipe=recipe(user=self.user, recipeJSON=JSON1, sharedDetails=self.shared_details)
        self.recipe.save()


    def test_shared(self):
        self.assertTrue(self.recipe.shared())

        self.recipe.sharedDetails = None
        self.recipe.save()

        self.assertFalse(self.recipe.shared())

    def test_share(self):
        self.assertFalse(self.recipe.share())  # Already shared, should return False

        self.recipe.sharedDetails = None
        self.recipe.save()

        self.assertTrue(self.recipe.share())
        self.assertIsNotNone(self.recipe.sharedDetails)

    def test_rate(self):
        self.assertEqual(self.recipe.sharedDetails.currentRating, 4)

        new_rating = 4.5
        self.recipe.rate(self.user, new_rating)

        self.assertAlmostEqual(self.recipe.sharedDetails.currentRating, (new_rating+4)/2,2)

        # Try rating again with the same user, should return False
        self.assertFalse(self.recipe.rate(self.user, 3.0))

    def test_get_title(self):
        self.assertEqual(self.recipe.getTitle(), 'Spaghetti with Meatballs')

    def test_rated_by_user(self):
        self.assertFalse(self.recipe.ratedByUser(self.user))

        # Rate the recipe with the user
        self.recipe.rate(self.user, 4.0)
        self.assertTrue(self.recipe.ratedByUser(self.user))

    def test_given_rating(self):
        self.assertEqual(self.recipe.givenRating(self.user), -1)

        # Rate the recipe with the user
        self.recipe.rate(self.user, 4.0)
        self.assertEqual(self.recipe.givenRating(self.user), 4.0)

    def test_estimate_price(self):
        self.assertAlmostEqual(round(self.recipe.estimatePrice(),2), 7.7)
        self.recipe.recipeJSON['ingredients'] = {
            'ingredient1': {'price': 2.5},
            'ingredient2': {'price': 3.5},
            'ingredient3': {'price': None},
        }
        self.recipe.save()

        self.assertEqual(self.recipe.estimatePrice(), 6.0)

    def test_str_representation(self):
        expected_str = "pk:" + str(self.recipe.pk) + ", Title:Spaghetti with Meatballs, User:test1, sharedDetails: (" + self.shared_details.__str__() + ")"
        self.assertEqual(str(self.recipe), expected_str)
