import sqlite3
from recipesData import recipes


def create_database():
    conn = sqlite3.connect("meal_planner.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS recipes
                 (id INTEGER PRIMARY KEY, 
                  name TEXT, 
                  ingredients TEXT, 
                  dietary_type TEXT)"""
    )

    for recipe in recipes:
        try:
            c.execute(
                "INSERT OR REPLACE INTO recipes (name, ingredients, dietary_type) VALUES (?, ?, ?)",
                recipe,
            )
        except sqlite3.IntegrityError:
            print(f"Duplicate recipe name: {recipe[0]}. Skipping.")

    conn.commit()
    conn.close()


def get_recipes(dietary_type):
    conn = sqlite3.connect("meal_planner.db")
    c = conn.cursor()

    query = "SELECT name, ingredients, dietary_type FROM recipes WHERE dietary_type = ?"
    c.execute(query, (dietary_type,))

    recipes = c.fetchall()
    conn.close()

    return recipes


def get_all_recipes():
    conn = sqlite3.connect("meal_planner.db")
    c = conn.cursor()

    query = "SELECT name, ingredients, dietary_type FROM recipes"
    c.execute(query)

    recipes = c.fetchall()
    conn.close()

    return recipes
