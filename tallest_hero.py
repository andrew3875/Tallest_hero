import requests


API_URL = "https://akabab.github.io/superhero-api/api/all.json"


def get_tallest_hero(gender, has_job):
    response = requests.get(API_URL)
    heroes = response.json()
    filtered_heroes = []

    for hero in heroes:
        if hero["appearance"]["gender"] != gender:
            continue

        occupation = hero["work"]["occupation"]
        
        if occupation != "-":
            hero_has_job = True
        else:
            hero_has_job = False

        if hero_has_job != has_job:
            continue

        filtered_heroes.append(hero)

    for hero in filtered_heroes:
        height = hero["appearance"]["height"][1]

        if "cm" in height:
            hero_height = float(height.replace(" cm", ""))
        elif "meters" in height:
            hero_height = float(height.replace(" meters", "")) * 100
        else:
            hero_height = 0

        hero["height_cm"] = hero_height

    tallest_hero = max(filtered_heroes, key=lambda hero: hero["height_cm"])

    return tallest_hero