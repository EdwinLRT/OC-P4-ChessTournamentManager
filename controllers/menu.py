from views.menu import MenuViews
from models.player import Player
from models.tournament import Tournament
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.report import ReportController


class MenuController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.player_models = Player()
        self.tournament_models = Tournament()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.report_controller = ReportController()

    def app_main_menu(self):
        """This is the main menu of the application."""
        self.menu_view.display_menu()
        choice = input("\nVotre choix :")
        if choice == "1":
            self.new_player()
        elif choice == "2":
            self.new_tournament()
        elif choice == "3":
            self.tournament_controller.start_tournament()
        elif choice == "4":
            self.report_menu()

        elif choice == "5":
            MenuViews.software_exit()
        else:
            MenuViews.invalid_input()
            self.app_main_menu()

    def report_menu(self):
        self.menu_view.display_report_menu()
        choice = input("\nVotre choix :")
        if choice == "1":
            self.report_controller.alphabetic_players_report()
        elif choice == "2":
            self.report_controller.tournament_list_report()
        elif choice == "3":
            self.report_controller.tournament_sorted_players_report()
        elif choice == "4":
            self.report_controller.tournament_sorted_players_report()
        elif choice == "5":
            self.report_controller.tournament_rounds_matches_report()
        elif choice == "6":
            self.app_main_menu()
        else:
            MenuViews.invalid_input()
            self.report_menu()

    def new_player(self):
        """Create a new player, and add it to the database"""

        player_id, player_name, player_surname, player_birthday, player_elo = (
            MenuViews.input_new_player()
        )
        new_player = [player_id,
                      player_name,
                      player_surname,
                      player_birthday,
                      player_elo]
        self.menu_view.player_info_review(new_player)
        while True:
            user_choice = MenuViews.input_user_choice()
            if user_choice == "y":
                player = Player(player_id=player_id,
                                player_name=player_name,
                                player_surname=player_surname,
                                player_birthday=player_birthday,
                                player_elo=player_elo)
                player.add_player_to_db()
                self.menu_view.player_saved_to_database()
                break
            elif user_choice == "n":
                self.menu_view.player_not_saved_to_database()
                self.app_main_menu()
                break
            else:
                MenuViews.invalid_input()
        self.app_main_menu()

    def new_tournament(self):
        """Create a new tournament, and add it to the database"""
        tournament_id, tournament_name, \
            tournament_location, tournament_start_date, \
            tournament_end_date, tournament_start_time, \
            tournament_end_time, tournament_rounds_number, \
            tournament_current_round, tournament_rounds_list, \
            tournament_players_list, tournament_description = (
                MenuViews.input_new_tournament(self)
            )
        new_tournament = [tournament_id,
                          tournament_name,
                          tournament_location,
                          tournament_start_date,
                          tournament_end_date,
                          tournament_start_time,
                          tournament_end_time,
                          tournament_rounds_number,
                          tournament_current_round,
                          tournament_rounds_list,
                          tournament_players_list,
                          tournament_description]
        self.menu_view.tournament_info_review(new_tournament,
                                              tournament_players_list)
        while True:
            user_choice = MenuViews.input_user_choice()
            if user_choice == "y":
                tournament = Tournament(
                    tournament_id=tournament_id,
                    tournament_name=tournament_name,
                    tournament_location=tournament_location,
                    tournament_start_date=tournament_start_date,
                    tournament_end_date=tournament_end_date,
                    tournament_start_time=tournament_start_time,
                    tournament_end_time=tournament_end_time,
                    tournament_rounds_number=tournament_rounds_number,
                    tournament_current_round=tournament_current_round,
                    tournament_rounds_list=tournament_rounds_list,
                    tournament_players_list=tournament_players_list,
                    tournament_description=tournament_description)
                tournament.add_tournament_to_db()
                self.menu_view.tournament_saved_to_database()
                break
            elif user_choice == "n":
                self.menu_view.tournament_not_saved_to_database()
                self.app_main_menu()
                break
            else:
                MenuViews.invalid_input()
        self.app_main_menu()
