import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime
from pd2 import pdfer

def month():
    #region Description

    """
        Getting the current month using an API
        Parameters:
            None
        Returns:
            Name of the current month
    """
    #endregion
    try:
        url = "http://worldtimeapi.org/api/ip"

        response = requests.get(url)
        data = response.json()

        currentMonth = int(data["datetime"][5:7])
        monthName = datetime.strptime(str(currentMonth), "%m").strftime("%B")
        return(monthName)
    except:
        return("Something went wrong!")



def season():
    #region Description
    """
        Based on the current month, a recipe is provided by PDF
        Parameters:
            None
        Returns:
            None
    """
    #endregion
    try:
        #Accesing the site where the seasonal menu is located
        response=requests.get("https://www.chileanfoodandgarden.com/chilean-menus-ideas/")
        soup=BeautifulSoup(response.text, "html.parser")
        s=soup.find("div",class_='entry-content entry-content-single')
        s2=s.find_all('a')

        #Storing the links to the recipes
        siteLinks=[]
        for i in s2:
            siteLinks.append(i["href"])
        del siteLinks[:4]
        #Categorizing the recipes
        spring=siteLinks[:8]
        summer=siteLinks[8:17]
        fall=siteLinks[17:24]
        winter=siteLinks[24:]
        chosenlinks=[]
        #Choosing wich month to run aka wich sites to access based on the month
        if month()=="March" or month()=="April" or month()=="May":
            chosenlinks=spring
        if month()=="June" or month()=="July" or month()=="August":
            chosenlinks=summer
        if month()=="September" or month()=="October" or month()=="November":
            chosenlinks=fall
        if month()=="December" or month()=="January" or month()=="February":
            chosenlinks=winter

        #Gaining the info from the sites
        recipeURL=random.choice(chosenlinks)
        recipeResponse=requests.get(recipeURL)
        recipeSoup=BeautifulSoup(recipeResponse.text, "html.parser")

        #Extracting the useful info
        RecipeTitle=recipeSoup.find('h1',class_="entry-title entry-title-single").text.strip()
        s3=recipeSoup.find('div',class_="site-inner")
        RecipePic=s3.find('img')["src"]
        s4=recipeSoup.find('div',class_="tasty-recipes-ingredients")
        #Listing the ingredients
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
        print("An error occured, please try again!")

def main():
    season()

if __name__ == "__main__":
     main()
