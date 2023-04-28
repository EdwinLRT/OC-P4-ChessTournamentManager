from controllers.menu import MenuController
from views.menu import MenuViews
import os


def create_database():
    """
    Create the "database" folder and the "player_db.json" and
    "tournament_db.json" files inside it
    if they do not exist.
    """
    if not os.path.exists("database"):
        os.makedirs("database")

    if not os.path.exists("database/player_db.json"):
        with open("database/player_db.json", "w") as f:
            f.write("[]")

    if not os.path.exists("database/tournament_db.json"):
        with open("database/tournament_db.json", "w") as f:
            f.write("[]")


def main():
    create_database()
    MenuViews().display_menu_title()
    MenuController().app_main_menu()


if __name__ == '__main__':
    main()
