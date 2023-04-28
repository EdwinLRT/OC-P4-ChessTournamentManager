from controllers.menu import MenuController
from views.menu import MenuViews
def main():
    MenuViews().display_menu_title()
    MenuController().app_main_menu()

if __name__ == '__main__':
    main()