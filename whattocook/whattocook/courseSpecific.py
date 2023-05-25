import requests
import random
from bs4 import BeautifulSoup
from pd2 import pdfer

def chileanMenu(course):
    #region Description
    """
    This function give a PDF file which includes a random Chilean recipe from a given course.
    Parameters:
        None
    Returns:
        None
    
    """
    #endregion
    try:
        course=course.capitalize()
        #Gaining the links of the recipes by srcaping a site, and choosing the meal type
        siteLinks=[]
        if course=="Breakfast":
            response=requests.get("https://www.chileanfoodandgarden.com/chilean-breakfast/")
        elif course=="Snack":
            response=requests.get("https://www.chileanfoodandgarden.com/chilean-desserts/")
        elif course=="Lunch":
            response=requests.get("https://www.chileanfoodandgarden.com/chilean-meat/")
        elif course=="Dinner":
            response=requests.get("https://www.chileanfoodandgarden.com/chilean-pasta-rice-potatoes/")

        soup=BeautifulSoup(response.text, "html.parser")
        s=soup.find('div',class_="gb-post-grid-items is-grid columns-3")
        s2=s.find_all('a')
        for i in s2:
            siteLinks.append(i["href"])

        #Opening the recipe
        recipeURL=random.choice(siteLinks)
        recipeResponse=requests.get(recipeURL)
        recipeSoup=BeautifulSoup(recipeResponse.text, "html.parser")

        #Locating the useful info
        RecipeTitle=recipeSoup.find('h1',class_="entry-title entry-title-single").text.strip()
        s3=recipeSoup.find('div',class_="site-inner")
        RecipePic=s3.find('img')["src"]

        #Getting the ingredients
        s4=recipeSoup.find('div',class_="tasty-recipes-ingredients")
        RecipeIngredients=s4.find('ul').text.split("\n")
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
    course=input("Enter a course:")
    chileanMenu(course)

if __name__ == "__main__":
     main()