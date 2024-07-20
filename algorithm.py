from database import get_recipes, get_all_recipes
import random


def ingredient_match(user_ingredients, meal_ingredients):
    user_ing_set = set(ing.strip().lower() for ing in user_ingredients)
    meal_ing_set = set(ing.strip().lower() for ing in meal_ingredients.split(","))

    for user_ing in user_ing_set:
        if any(user_ing in meal_ing for meal_ing in meal_ing_set):
            return True
    return False


def generate_meal_plan(dietary_type, allergies, user_ingredients):
    suitable_meals = get_recipes(dietary_type)

    filtered_meals = []
    for meal in suitable_meals:
        meal_name, meal_ingredients, _ = meal

        if any(
            allergy.lower() in meal_name.lower()
            or allergy.lower() in meal_ingredients.lower()
            for allergy in allergies
        ):
            continue

        if ingredient_match(user_ingredients, meal_ingredients):
            filtered_meals.append(meal)

    if len(filtered_meals) < 7:
        all_meals = get_all_recipes()
        for meal in all_meals:
            if meal in filtered_meals:
                continue

            meal_name, meal_ingredients, _ = meal

            if any(
                allergy.lower() in meal_name.lower()
                or allergy.lower() in meal_ingredients.lower()
                for allergy in allergies
            ):
                continue

            if ingredient_match(user_ingredients, meal_ingredients):
                filtered_meals.append(meal)

            if len(filtered_meals) >= 7:
                break

    # Ensure no repetition
    unique_meals = list(set(filtered_meals))  # Remove any duplicates

    if len(unique_meals) >= 7:
        return random.sample(unique_meals, 7)
    else:
        # If we have less than 7 unique meals, return all available unique meals
        return unique_meals
