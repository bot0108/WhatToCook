import requests
from bs4 import BeautifulSoup
import random
from pd2 import pdfer

def recipeScraper():
    #region Description
    """
    This function accesses a random chilean recipe an scrapes the title,image,ingredients and preparation.
    Parameters: None
    Returns: Whole recipe

    """
    #endregion
    try:
        #Accessing the main site with all of the recipes
        response=requests.get("https://www.allrecipes.com/recipes/1277/world-cuisine/latin-american/south-american/chilean/")
        soup=BeautifulSoup(response.text, "html.parser")
        s=soup.find_all('a',class_='comp mntl-card-list-items mntl-document-card mntl-card card card--no-image')

        #Storing the links to the recipes
        siteLinks=[]
        for i in s:
            siteLinks.append(i["href"])

        #Accessing the specific recipe
        recipeURL=random.choice(siteLinks)
        recipeResponse=requests.get(recipeURL)
        recipeSoup=BeautifulSoup(recipeResponse.text, "html.parser")


        #Gaining the necessary info from the recipes
        RecipeTitle=recipeSoup.find('h1').text.strip()
        RecipePic=recipeSoup.find('img')["src"]
        RecipeIngredients=recipeSoup.find('ul',class_="mntl-structured-ingredients__list").text.strip().split("\n\n\n")
        CleanRecipeIngredients=[]
        for j in RecipeIngredients:
            j=j.lstrip("\n").rstrip("\n").strip()
            CleanRecipeIngredients.append(j)
        #Cleaning the steps into a list
        RecipeSteps=recipeSoup.find('ol').text.strip().split(".")
        CleanRecipeSteps=[]
        for i in RecipeSteps:
            i=i.lstrip("\n").rstrip("\n").strip()
            CleanRecipeSteps.append(i)

        #Making the PDF of the recipe
        pdfer(RecipePic,RecipeTitle,CleanRecipeIngredients,CleanRecipeSteps)

    except:
        print("Wrong input!")

def main():
    recipeScraper()

if __name__ == "__main__":
     main()
    
    
