from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from cocktail import randomCocktail

def pdfer(RecipePic,RecipeTitle,CleanRecipeIngredients,CleanRecipeSteps):
    #region Description
    """
    This function creates a ready to print PDF recipe from the scaped data
    Parameters:
        RecipePic,RecipeTitle,CleanRecipeIngredients,CleanRecipeSteps
    Returns:
        None
    """
    #endregion
    # create

    filename=f"{RecipeTitle}.pdf"

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Make the headings(Styles)
    title_style = styles["Title"]
    subtitle_style = styles["Heading1"]
    text_style = styles["BodyText"]

    content = []

    # Recipe Title
    title = Paragraph(RecipeTitle, title_style)
    content.append(title)

    # Recipe Image
    image = requests.get(RecipePic)
    with open("recipe_image.jpg", "wb") as i:
        i.write(image.content)
    recipe_image = Image("recipe_image.jpg", width=200, height=200)
    content.append(recipe_image)

    # Ingredients
    ingredientsTitle = Paragraph("Ingredients:", subtitle_style)
    content.append(ingredientsTitle)

    # Iterate through ingredients 
    for i in CleanRecipeIngredients:
        ingredientText = Paragraph(str(i), text_style)
        content.append(ingredientText)

    # Steps
    stepsTitle = Paragraph("Steps:", subtitle_style)
    content.append(stepsTitle)

    # Iterate through steps 
    for i in CleanRecipeSteps:
        stepText = Paragraph(str(i), text_style)
        content.append(stepText)
        content.append(Spacer(1, 12))  


    cocktailTitle = Paragraph("Cocktail pairing:", subtitle_style)
    content.append(cocktailTitle)

    # Get the data from the coctail API
    cocktailName, cocktailIngre = randomCocktail()

    EditedCoctailName = Paragraph(cocktailName.capitalize(), text_style)
    content.append(EditedCoctailName)

    # Iterate through the list of cocktail ingreds
    for i in cocktailIngre:
        text = Paragraph(str(i), text_style)
        content.append(text)

    doc.build(content)
    print("PDF Saved!")
