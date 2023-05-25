![Banner](WhatToCookBanner.png)


#WhatToCook program

##Intro
This is a python program which uses API-s and Webscraping to gain access to Chilean recipes,ingredients and instructions.
It creates a Ready to print PDF file with a recipe.
##Key features
Functionalities include the followings: 
-a random Chilean recipe,
-a season specific random recipe, 
-a course specific random recipe, 
-and one that does all of the above.

##Structure
|- whattocook
    |-whattocook
        |-__init__.py
        |-cocktail.py
        |-combined.py
        |-courseSpecific.py
        |-pd2.py
        |-scraper.py
        |-seasonal.py
        |-simple.py
    |-demo.ipynb
    |-LICENSE
    |-README.md
    |-setup.py
    |-WhatToCookBanner

##Used API's

Cocktail API : https://cocktails3.p.rapidapi.com/random
Month API: http://worldtimeapi.org/api/ip



##Usage

###cocktail.py
randomCocktail()    

###combined.py
special() #

###courseSpecific.py
chileanMenu()   

###pd2.py
pdfer(RecipePic,RecipeTitle,CleanRecipeIngredients,CleanRecipeSteps)    

###seasonal.py
month()     
season()    

###simple.py
recipeScraper()    







##License
This project uses an MIT license

##Contact
Name: Botond Grinacz
E-mail: botond.grinacz88@gmail.com
github: https://github.com/bot0108
