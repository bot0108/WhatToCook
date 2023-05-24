import requests
import random
from bs4 import BeautifulSoup
from pd2 import pdfer
from seasonal import month

def special():
        #region Description
        """
            This function takes a recipe according to the season and the chosen course
            Parameters:
                None
            Returns:
                None
        """
        #endregion
        course=input("Enter a course!")
        try:
            course=course.capitalize()
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
            
            chosenlinks2=[]
            #Choosing wich month to run aka wich sites to access based on the month
            if month()=="March" or month()=="April" or month()=="May":
                if course=="Lunch" or course=="Dinner":
                    chosenlinks2=[siteLinks[i] for i in [11, 12, 16]]
                if course=="Snack":
                    chosenlinks2=[siteLinks[i] for i in [0, 1, 2]]
                if course=="Breakfast":
                    chosenlinks2=[siteLinks[i] for i in [ 1, 6, 5]]
            if month()=="June" or month()=="July" or month()=="August":
                if course=="Lunch" or course=="Dinner":
                    chosenlinks2=[siteLinks[i] for i in [11, 12, 16]]
                if course=="Snack":
                    chosenlinks2=[siteLinks[i] for i in [15, 14, 8]]
                if course=="Breakfast":
                    chosenlinks2=[siteLinks[i] for i in [ 13, 10, 9]]
            if month()=="September" or month()=="October" or month()=="November":
                if course=="Lunch" or course=="Dinner":
                    chosenlinks2=[siteLinks[i] for i in [19, 20, 23]]
                if course=="Snack":
                    chosenlinks2=[siteLinks[i] for i in [ 17, 18]]
                if course=="Breakfast":
                    chosenlinks2=[siteLinks[i] for i in [ 21, 22]]
            if month()=="December" or month()=="January" or month()=="February":
                if course=="Lunch" or course=="Dinner":
                    chosenlinks2=[siteLinks[i] for i in [28,27,32]]
                if course=="Snack":
                    chosenlinks2=[siteLinks[i] for i in [30, 26, 29]]
                if course=="Breakfast":
                    chosenlinks2=[siteLinks[i] for i in [ 31, 24, 25]]
            #Gaining the info from the sites
            recipeURL=random.choice(chosenlinks2)
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
            print("An error occured please try again!")
        
def main():

    
    special()

if __name__ == "__main__":
     main()