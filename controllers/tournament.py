from datetime import datetime
from views.menu import MenuViews
from views.round import RoundViews
from models.round import Round
from controllers.player import PlayerController
from tinydb import TinyDB, Query
from views.tournament import TournamentViews
import random


class TournamentController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.round_views = RoundViews()
        self.player_controller = PlayerController()
        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tournament_views = TournamentViews()

    @staticmethod
    def return_to_main_menu():
        """Return to main menu"""
        from controllers.menu import MenuController
        menu_controller = MenuController()
        menu_controller.app_main_menu()

    def players_selection(self, tournament_players_number):
        """Select the players for the tournament
            tournament_players_number:
                number of players for the tournament(int)
            Also defines the number of rounds for the tournament
            ( 2 players = 1 round, 4 players = 2 rounds, etc.)
            """
        players_list = self.player_controller.display_all_players()
        selected_players = []
        for player in range(tournament_players_number):
            while True:
                player_selection = \
                    TournamentViews.input_player_selection(
                        player,
                        players_list)
                if player_selection.isnumeric() \
                        and 1 <= int(player_selection) <= len(players_list):
                    selected_player = players_list[int(player_selection) - 1]
                    if selected_player in selected_players:
                        TournamentViews.already_selected_player()
                    else:
                        selected_player["score"] = 0
                        selected_player["opponents"] = []
                        selected_players.append(selected_player)
                        break
                else:
                    TournamentViews.invalid_input()
        self.tournament_views.display_tournament_selected_players(
            player, selected_players)
        return selected_players

    @staticmethod
    def tournament_selection():
        """Select a tournament from the database
        """
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        all_tournaments = table.all()
        tournaments_list = []
        i = 0
        TournamentViews.display_title_select_tournament()
        for tournament in all_tournaments:
            tournaments_list.append(tournament)
            TournamentViews.display_tournament_indexed_list(i, tournament)
            i += 1
        while True:
            tournament_selection = TournamentViews.input_tournament_selection(
                tournaments_list)
            if tournament_selection.isnumeric() \
                    and 1 <= int(tournament_selection) \
                    <= len(tournaments_list):
                selected_tournament = tournaments_list[
                    int(tournament_selection) - 1]
                TournamentViews.display_tournament_name_location(
                    selected_tournament)
                while True:
                    user_input = TournamentViews.display_players_or_continue()
                    if user_input == '1':
                        TournamentViews.display_tournament_players(
                            selected_tournament)
                        pass
                    elif user_input == '2':
                        return selected_tournament, selected_tournament[
                            "tournament_players_list"]
                    elif user_input == '3':
                        TournamentController.return_to_main_menu()
                    else:
                        TournamentViews.invalid_input()
            else:
                TournamentViews.invalid_input()

    @staticmethod
    def shuffle_tournament_players_list(players_list):
        """" Shuffle the players list for the tournament
        players_list: list of players for the tournament (list)
        """
        shuffled_players_list = players_list.copy()
        random.shuffle(shuffled_players_list)
        return shuffled_players_list

    @staticmethod
    def tournament_start_time(selected_tournament):
        """" Defines the start time of the tournament
            selected_tournament: tournament selected by the user (dict)"""
        TournamentViews.input_tournament_start_time()
        tournament_start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected_tournament["tournament_start_time"] = tournament_start_time
        TournamentViews.display_tournament_start_time(selected_tournament)
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        table.update(selected_tournament,
                     Query().tournament_id == selected_tournament[
                         "tournament_id"])
        return tournament_start_time

    @staticmethod
    def round_start_time(selected_tournament):
        """" Defines the start time of the round
            selected_tournament: tournament selected by the user (dict)"""
        TournamentViews.input_round_start_time()
        round_start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected_tournament["round_start_time"] = round_start_time
        TournamentViews.display_round_start_time(selected_tournament)
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        table.update(selected_tournament, (
                Query().tournament_id == selected_tournament[
                                            "tournament_id"]))
        return round_start_time

    @staticmethod
    def round_end_time(selected_tournament):
        """" Defines the end time of the round
            selected_tournament: tournament selected by the user (dict)"""
        TournamentViews.input_round_end_time()
        round_end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected_tournament["round_end_time"] = round_end_time
        TournamentViews.display_round_end_time(selected_tournament)
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        table.update(selected_tournament,
                     Query().tournament_id == selected_tournament[
                         "tournament_id"])
        return round_end_time

    @staticmethod
    def tournament_end_time(selected_tournament):
        """" Defines the end time of the tournament
            selected_tournament: tournament selected by the user (dict)"""
        TournamentViews.input_tournament_end_time()
        tournament_end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected_tournament["tournament_end_time"] = tournament_end_time
        TournamentViews.display_tournament_end_time(selected_tournament)
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        table.update(selected_tournament,
                     Query().tournament_id == selected_tournament[
                         "tournament_id"])
        return tournament_end_time

    def paired_players(self, players_list):
        """Pair the players for the tournament (Used for the first round only)
        players_list: list of players for the tournament (list)
        """
        paired_players = []
        shuffled_players_list = self.shuffle_tournament_players_list(
            players_list)
        for player in range(len(shuffled_players_list) // 2):
            pair = (
                shuffled_players_list[player],
                shuffled_players_list[-player - 1])
            paired_players.append(pair)
        return paired_players

    @staticmethod
    def pair_players_by_score(selected_tournament, players_list):
        """Create pairs of players based on their score"""
        players_list = selected_tournament["tournament_players_list"]
        sorted_players = sorted(players_list, key=lambda x: x["score"],
                                reverse=True)
        paired_players = []
        num_players = len(sorted_players)
        paired_ids = []
        for i in range(num_players // 2):
            if i + 1 < len(sorted_players):
                player1 = sorted_players[i]
                player2 = next((p for p in sorted_players[i + 1:] if
                                p["chess_id"] not in paired_ids), None)
                if player2:
                    paired_players.append([player1, player2])
                    paired_ids.extend(
                        [player1["chess_id"], player2["chess_id"]])
                    sorted_players.remove(player2)
        return paired_players

    def tournament_players_scores_update(selected_tournament, match,
                                         match_result):
        """ Update the players scores after each round
        """
        # Get player IDs from match variable
        player1_id = match[0]["Player 1"][0]
        player2_id = match[1]["Player 2"][0]

        # Retrieve the tournament and players information from the database
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        tournament_id = selected_tournament["tournament_id"]
        players_list = selected_tournament["tournament_players_list"]
        player1 = next((player for player in players_list if
                        player["chess_id"] == player1_id), None)
        player2 = next((player for player in players_list if
                        player["chess_id"] == player2_id), None)

        # Add the opponents of each player to the player's opponents list
        player1['opponents'].append(player2_id)
        player2['opponents'].append(player1_id)

        with TinyDB('db.json') as db:
            table = db.table('_default')
            if match_result == '1':
                match[0]["Player 1"][3] += 1
                player1["score"] += 1
                table.update({'tournament_players_list': players_list},
                             Query().tournament_id == tournament_id)

            elif match_result == '2':
                match[1]["Player 2"][3] += 1
                player2["score"] += 1
                table.update({'tournament_players_list': players_list},
                             Query().tournament_id == tournament_id)

            elif match_result == '0':
                match[0]["Player 1"][3] += 0.5
                match[1]["Player 2"][3] += 0.5
                player1["score"] += 0.5
                player2["score"] += 0.5
                table.update({'tournament_players_list': players_list},
                             Query().tournament_id == tournament_id)

    def tournament_matchs_update(selected_tournament, round):
        """ Update the matchs list after each round
        """
        # Retrieve the tournament and players information from the database
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        tournament_id = selected_tournament["tournament_id"]
        matchs_list = selected_tournament["tournament_rounds_list"]
        # Add the match to the tournament's matchs list
        matchs_list.append(round)
        table.update({'tournament_rounds_list': matchs_list},
                     Query().tournament_id == tournament_id)

    def match_results_input(selected_tournament, match):
        """
        Input match results
        """
        match_result = TournamentViews.input_match_result(match)
        while match_result not in ["1", "2", "0"]:
            match_result = TournamentViews.input_match_result(match)
        TournamentController.tournament_players_scores_update(
            selected_tournament, match, match_result)
        return match_result

    def tournament_first_round(self, selected_tournament, players_list,
                               round_matchs):
        """First round of the tournament
            Pairing of the players
            set the round and save it to DB"""

        shuffled_players_list = self.shuffle_tournament_players_list(
            players_list)
        paired_players = self.paired_players(shuffled_players_list)

        self.tournament_start_time(selected_tournament)
        TournamentViews.display_round_title(1)
        current_round = []
        TournamentViews.display_match_in_round_title()
        for pair in paired_players:
            matchs = []
            TournamentViews.display_match_in_round(pair)
            player1 = {'Player 1': [pair[0]['chess_id'], pair[0]['name'],
                                    pair[0]['surname'], pair[0]['score']]}
            player2 = {'Player 2': [pair[1]['chess_id'], pair[1]['name'],
                                    pair[1]['surname'], pair[1]['score']]}
            result = {'Result': 'Match not played yet'}
            matchs.append(player1)
            matchs.append(player2)
            matchs.append(result)
            current_round.append(matchs)
            round_matchs.append(pair)
        round_start = self.round_start_time(selected_tournament)
        for match in current_round:
            match_result = TournamentController.match_results_input(
                selected_tournament, match)
            match[2]['Result'] = match_result

        round_end = self.round_end_time(selected_tournament)
        round_1 = ('Round_1', round_start, current_round, round_end)
        TournamentController.tournament_matchs_update(selected_tournament,
                                                      round_1)
        selected_tournament["tournament_rounds_list"].append(round_1)

    def tournament_next_rounds(self, selected_tournament, players_list,
                               round_matchs):
        """"Next rounds of the tournament
            Pairing of the players by score
            set the round and save it to DB"""

        round_number = selected_tournament["tournament_current_round"]
        round = Round("Round " + str(round_number),
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                      "Not finished yet")
        TournamentViews.display_round_title(round_number)
        paired_players = self.pair_players_by_score(selected_tournament,
                                                    players_list)
        current_round = []
        TournamentViews.display_match_in_round_title()
        for pair in paired_players:
            matchs = []
            TournamentViews.display_match_in_round(pair)
            player1 = {'Player 1': [pair[0]['chess_id'], pair[0]['name'],
                                    pair[0]['surname'], pair[0]['score']]}
            player2 = {'Player 2': [pair[1]['chess_id'], pair[1]['name'],
                                    pair[1]['surname'], pair[1]['score']]}
            result = {'Result': 'Match not played yet'}
            matchs.append(player1)
            matchs.append(player2)
            matchs.append(result)
            current_round.append(matchs)
            round_matchs.append(pair)
        round_start = self.round_start_time(selected_tournament)
        for match in current_round:
            match_result = TournamentController.match_results_input(
                selected_tournament, match)
            match[2]['Result'] = match_result

        round_end = self.round_end_time(selected_tournament)
        round = (
            'Round_' + str(round_number), round_start, current_round,
            round_end)
        TournamentController.tournament_matchs_update(selected_tournament,
                                                      round)
        selected_tournament["tournament_rounds_list"].append(round)

    @staticmethod
    def increment_tournament_current_round(tournament_id):
        """Increment the tournament_current_round
         value in TinyDB for a given tournament_id"""
        db = TinyDB('./database/tournament_db.json')
        Tournament = Query()
        tournaments_table = db.table('_default')
        tournament = tournaments_table.get(
            Tournament.tournament_id == tournament_id)
        current_round = tournament["tournament_current_round"]
        updated_tournament = tournaments_table.update(
            {"tournament_current_round": current_round + 1},
            Tournament.tournament_id == tournament_id)
        # get updated tournament from DB
        updated_tournament = tournaments_table.get(
            Tournament.tournament_id == tournament_id)
        db.close()
        return updated_tournament

    @staticmethod
    def tournament_final_scores(players_list):
        sorted_players = sorted(players_list, key=lambda p: p['score'],
                                reverse=True)
        TournamentViews.display_final_scores(sorted_players)

    def start_tournament(self):

        """Start a new tournament"""
        db = TinyDB('./database/tournament_db.json')
        Tournament = Query()
        tournaments_table = db.table('_default')
        selected_tournament, players_list = self.tournament_selection()
        tournament_id = selected_tournament["tournament_id"]
        print(players_list)

        if selected_tournament["tournament_current_round"] == 1:
            while True:
                if selected_tournament["tournament_current_round"] == 1:
                    round_matchs = []
                    self.tournament_first_round(selected_tournament,
                                                players_list, round_matchs)
                    TournamentController.increment_tournament_current_round(
                        tournament_id)
                    selected_tournament = tournaments_table.get(
                        Tournament.tournament_id == tournament_id)
                elif 1 < selected_tournament["tournament_current_round"] <= \
                        selected_tournament["tournament_rounds_number"]:
                    round_matchs = []
                    self.tournament_next_rounds(selected_tournament,
                                                players_list, round_matchs)
                    TournamentController.increment_tournament_current_round(
                        tournament_id)
                    selected_tournament = tournaments_table.get(
                        Tournament.tournament_id == tournament_id)
                elif selected_tournament["tournament_current_round"] > \
                        selected_tournament["tournament_rounds_number"]:
                    if selected_tournament[
                            "tournament_end_time"] == "Non renseigne":
                        self.tournament_end_time(selected_tournament)
                        selected_tournament = tournaments_table.get(
                            Tournament.tournament_id == tournament_id)
                        break
                    else:
                        TournamentViews.display_tournament_already_ended(
                            selected_tournament)
                        break

        elif 1 < selected_tournament["tournament_current_round"] <= \
                selected_tournament["tournament_rounds_number"]:
            while True:
                if 1 < selected_tournament["tournament_current_round"] <= \
                        selected_tournament["tournament_rounds_number"]:
                    round_matchs = []
                    self.tournament_next_rounds(selected_tournament,
                                                players_list, round_matchs)
                    TournamentController.increment_tournament_current_round(
                        tournament_id)
                    selected_tournament = tournaments_table.get(
                        Tournament.tournament_id == tournament_id)
                elif selected_tournament["tournament_current_round"] > \
                        selected_tournament["tournament_rounds_number"]:
                    if selected_tournament[
                            "tournament_end_time"] == "Non renseigne":
                        self.tournament_end_time(selected_tournament)
                        selected_tournament = tournaments_table.get(
                            Tournament.tournament_id == tournament_id)
                        break
                    else:
                        TournamentViews.display_tournament_already_ended(
                            selected_tournament)
                        break
        elif selected_tournament["tournament_current_round"] > \
                selected_tournament["tournament_rounds_number"]:
            if selected_tournament["tournament_end_time"] == "Non renseigne":
                TournamentViews.input_tournament_end_time()
                self.tournament_end_time(selected_tournament)
                TournamentViews.display_tournament_end_time()
                selected_tournament = tournaments_table.get(
                    Tournament.tournament_id == tournament_id)
            else:
                TournamentViews.display_tournament_already_ended()
                self.tournament_final_scores(players_list)
                self.return_to_main_menu()
