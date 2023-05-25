import requests

def randomCocktail():
    #region Description
    """
    This function uses an API to get a random cocktail
    Parameters:
        None
    Returns:
        Name of the cocktail
        Ingredients of the cocktail
    """
    #endregion
    url = "https://cocktails3.p.rapidapi.com/random"

    headers = {
        "X-RapidAPI-Key": "b61c97c152msha4bac7cc11fb7dap157146jsne431981a9d17",
        "X-RapidAPI-Host": "cocktails3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    name = data['body'][0]['name']
    ingredients = data['body'][0]['ingredients']
    return(name,ingredients)


