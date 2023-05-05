from django.core.management.base import BaseCommand
from homeapp.models import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.filter(username="test1").delete()
        U1 = User(email="test1@example.com", username="test1")
        U1.set_password('test1')
        U1.save()


        Recipe.objects.filter(formattedJSON__exact={'title':'Spaghetti with Meatballs'}).delete()
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
        R1=Recipe(user=U1, formattedJSON=JSON1)
        R1.save()

        self.stdout.write('done.') 


        