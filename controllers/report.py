from views.menu import MenuViews
from views.report import ReportViews
from controllers.tournament import TournamentController
from tinydb import TinyDB, Query


class ReportController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.report_view = ReportViews()
        self.tournament_controller = TournamentController()

    def alphabetic_players_report(self):
        """Player report (sorted by last name)
        """
        player_db = TinyDB('./database/player_db.json')
        Player = Query()
        players_list = (sorted(player_db.search(Player.name.exists()),
                               key=lambda p: p['name']))
        players_report = ReportViews.display_alphabetically_sorted_players(
            players_list)
        TournamentController.return_to_main_menu()
        return players_report

    def tournament_list_report(self):
        """All tournaments report"""
        tournament_db = TinyDB('./database/tournament_db.json')
        Tournament = Query()
        tournaments_list = tournament_db.search(
            Tournament.tournament_name.exists())
        tournaments_report = \
            ReportViews.display_tournaments_list(self,
                                                 tournaments_list)
        TournamentController.return_to_main_menu()
        return tournaments_report

    def tournament_sorted_players_report(self):
        """Players in a tournament report
        Select tournament to display players
        """
        selected_tournament, players_list = \
            TournamentController().tournament_selection()

        sorted_players_list = sorted(players_list, key=lambda p: p['name'])
        tournament_sorted_players = \
            ReportViews.display_tournament_sorted_players(
                self, selected_tournament,
                sorted_players_list)
        TournamentController.return_to_main_menu()
        return tournament_sorted_players

    def tournament_rounds_matches_report(self):
        """All rounds from a tournament"""
        selected_tournament = TournamentController().tournament_selection()
        tournament_rounds_list = selected_tournament[0][
            'tournament_rounds_list']
        tournament_rounds = \
            ReportViews.display_tournament_rounds_matches(
                self,
                selected_tournament,
                tournament_rounds_list)
        TournamentController.return_to_main_menu()
        return tournament_rounds
