from django.core.management.base import BaseCommand
from homeapp.models import *
class Command(BaseCommand):
    def handle(self, *args, **options):

        #clear tables
        recipe.objects.all().delete()
        sharedDetails.objects.all().delete()
        ratingHistory.objects.all().delete()
        UserSettings.objects.all().delete()

        #test users
        User.objects.filter(username="test1").delete()
        U1 = User(email="test1@example.com", username="test1")
        U1.set_password('test1')
        U1.save()
        UserSettings(user=U1).save()

        User.objects.filter(username="test2").delete()
        U2 = User(email="test2@example.com", username="test2")
        U2.set_password('test2')
        U2.save()
        UserSettings(user=U2, height=69.0, weight=69.0).save()

        #R1 is a global recipe
        SD1=sharedDetails(numRatings=2, currentRating=4)
        SD1.save()
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
        R1=recipe(user=U1, recipeJSON=JSON1, sharedDetails=SD1)
        R1.save()


        JSON2 = {
            "title" : "Chocolate Chip Cookies",
            "ingredients" : {
                "butter" : {
                "amount" : 200,
                "unit" : "grams",
                "price" : 2.5
                },
                "sugar" : {
                "amount" : 150,
                "unit" : "grams",
                "price" : 1.2
                },
                "flour" : {
                "amount" : 250,
                "unit" : "grams",
                "price" : 1.8
                },
                "chocolate chips" : {
                "amount" : 200,
                "unit" : "grams",
                "price" : 3.4
                },
                "eggs" : {
                "amount" : 2,
                "unit" : "quantity",
                "price" : 0.6
                },
                "vanilla extract" : {
                "amount" : 1,
                "unit" : "teaspoon",
                "price" : 0.8
                },
                "baking soda" : {
                "amount" : 1,
                "unit" : "teaspoon",
                "price" : 0.5
                },
                "salt" : {
                "amount" : 0.5,
                "unit" : "teaspoon",
                "price" : 0.3
                }
            },
            "instructions" : [
                "Preheat the oven to 180°C (350°F).",
                "In a large mixing bowl, cream together the butter and sugar until light and fluffy.",
                "Add the eggs and vanilla extract, and mix well.",
                "In a separate bowl, combine the flour, baking soda, and salt.",
                "Gradually add the dry ingredients to the butter mixture, mixing until just combined.",
                "Stir in the chocolate chips.",
                "Drop rounded tablespoons of dough onto a greased baking sheet.",
                "Bake for 10-12 minutes or until lightly golden brown.",
                "Allow the cookies to cool on the baking sheet for a few minutes, then transfer to a wire rack to cool completely."
            ]
        }
        R2=recipe(user=U1, recipeJSON=JSON2)
        R2.save()





        #R3 is global recipe
        SD3=sharedDetails(numRatings=1, currentRating=7)
        SD3.save()
        JSON3 = {
            "title": "Spaghetti Bolognese",
            "ingredients": {
                "spaghetti": {
                "amount": 200,
                "unit": "grams",
                "price": 1.5
                },
                "ground beef": {
                "amount": 300,
                "unit": "grams",
                "price": 4.75
                },
                "onion": {
                "amount": 1,
                "unit": "quantity",
                "price": 0.5
                },
                "garlic cloves": {
                "amount": 2,
                "unit": "quantity",
                "price": 0.3
                },
                "tomato sauce": {
                "amount": 400,
                "unit": "millilitres",
                "price": 1.2
                },
                "tomato paste": {
                "amount": 2,
                "unit": "tablespoons",
                "price": 0.7
                },
                "dried oregano": {
                "amount": 1,
                "unit": "teaspoon",
                "price": 0.4
                },
                "dried basil": {
                "amount": 1,
                "unit": "teaspoon",
                "price": 0.4
                },
                "olive oil": {
                "amount": 2,
                "unit": "tablespoons",
                "price": 0.6
                },
                "salt": {
                "amount": 1,
                "unit": "teaspoon",
                "price": 0.2
                },
                "black pepper": {
                "amount": 0.5,
                "unit": "teaspoon",
                "price": 0.3
                }
            },
            "instructions": [
                "Heat olive oil in a large skillet over medium heat.",
                "Add chopped onion and minced garlic, and sauté until translucent.",
                "Add ground beef and cook until browned, breaking it up with a wooden spoon.",
                "Drain excess fat from the skillet.",
                "Stir in tomato sauce, tomato paste, dried oregano, dried basil, salt, and black pepper.",
                "Simmer the sauce for 20-30 minutes, stirring occasionally.",
                "While the sauce is simmering, cook the spaghetti according to the package instructions until al dente.",
                "Serve the Bolognese sauce over the cooked spaghetti.",
                "Garnish with grated Parmesan cheese, if desired."
            ]
        }
        R3=recipe(user=U2, recipeJSON=JSON3, sharedDetails=SD3)
        R3.save()
        



        JSON4 = {
            "title": "Mushroom Risotto",
            "ingredients": {
                "arborio rice": {
                "amount": 200,
                "unit": "grams",
                "price": 1.8
                },
                "mushrooms": {
                "amount": 250,
                "unit": "grams",
                "price": 2.5
                },
                "onion": {
                "amount": 1,
                "unit": "quantity",
                "price": 0.6
                },
                "vegetable broth": {
                "amount": 500,
                "unit": "millilitres",
                "price": 1.2
                },
                "butter": {
                "amount": 2,
                "unit": "tablespoons",
                "price": 0.4
                },
                "parmesan cheese": {
                "amount": 50,
                "unit": "grams",
                "price": 1.1
                },
                "white wine": {
                "amount": 125,
                "unit": "millilitres",
                "price": 1.5
                },
                "olive oil": {
                "amount": 2,
                "unit": "tablespoons",
                "price": 0.6
                },
                "garlic cloves": {
                "amount": 2,
                "unit": "quantity",
                "price": 0.3
                },
                "salt": {
                "amount": 1,
                "unit": "teaspoon",
                "price": 0.2
                },
                "black pepper": {
                "amount": 0.5,
                "unit": "teaspoon",
                "price": 0.3
                },
                "fresh parsley": {
                "amount": 1,
                "unit": "tablespoon",
                "price": 0.3
                }
            },
            "instructions": [
                "In a large skillet, heat the olive oil over medium heat.",
                "Add chopped onion and minced garlic, and sauté until the onion is translucent.",
                "Add sliced mushrooms and cook until they release their moisture and become tender.",
                "Remove the mushrooms from the skillet and set aside.",
                "In the same skillet, melt the butter and add the arborio rice. Stir for a couple of minutes until the rice grains are coated with butter.",
                "Pour in the white wine and cook until it is absorbed by the rice.",
                "Add a ladleful of vegetable broth to the skillet and cook, stirring frequently, until the broth is absorbed. Repeat this process, adding more broth each time, until the rice is creamy and al dente. This will take approximately 20 minutes.",
                "Stir in the cooked mushrooms, grated Parmesan cheese, salt, and black pepper. Cook for an additional 2-3 minutes.",
                "Remove from heat and let the risotto rest for a few minutes.",
                "Serve the mushroom risotto garnished with fresh parsley."
            ]
        }
        R4=recipe(user=U2, recipeJSON=JSON4)
        R4.save()

        #saving some rating history records
        H1=ratingHistory(ratingGiven=7, user=U2, sharedRecipe=SD3)
        H1.save()
        H2=ratingHistory(ratingGiven=3, user=U1, sharedRecipe=SD1)
        H2.save()
        H3=ratingHistory(ratingGiven=5, user=U2, sharedRecipe=SD1)
        H3.save()

        self.stdout.write('done.') 


        