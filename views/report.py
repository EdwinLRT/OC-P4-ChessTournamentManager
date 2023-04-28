from prettytable import PrettyTable


class ReportViews:
    @staticmethod
    def display_alphabetically_sorted_players(players_list):
        table = PrettyTable()
        table.clear()
        table.field_names = ["Chess ID", "Nom", "Prénom", "Date de naissance",
                             "Elo"]
        # extract infos from players_list
        table.align = "l"
        for player in players_list:
            table.add_row([
                player["chess_id"],
                player["name"],
                player["surname"],
                player["birth_date"],
                player["elo"],
            ])
        print("\nListe des joueurs enregistrés, par ordre alphabétique :\n")
        print(table)

    @staticmethod
    def display_tournaments_list(self, tournaments_list):
        table = PrettyTable()
        table.clear()
        table.field_names = ["ID", "Nom", "Lieu", "Date de début",
                             "Date de fin", "Nombre de tours"]
        table.align = "l"
        for tournament in tournaments_list:
            table.add_row([
                tournament["tournament_id"],
                tournament["tournament_name"],
                tournament["tournament_location"],
                tournament["tournament_start_date"],
                tournament["tournament_end_date"],
                tournament["tournament_rounds_number"],
            ])
        print("\nListe des tournois enregistrés :\n")
        print(table)

    @staticmethod
    def display_tournament_sorted_players(self, selected_tournament,
                                          sorted_players_list):
        table = PrettyTable()
        table.clear()
        table.field_names = ["Chess ID", "Nom", "Prénom", "Date de naissance",
                             "Elo"]
        # extract infos from players_list
        table.align = "l"
        for player in sorted_players_list:
            table.add_row([
                player["chess_id"],
                player["name"],
                player["surname"],
                player["birth_date"],
                player["elo"],
            ])
        print(
            f"\nListe des joueurs du {selected_tournament['tournament_name']}"
            f" par ordre alphabétique:\n")
        print(table)

    @staticmethod
    def display_tournament_rounds_matches(self, selected_tournament,
                                          tournament_rounds_list):
        table = PrettyTable()
        table.clear()
        table.field_names = ["Tour", "Joueur 1", "Résultat", "Joueur 2"]
        # extract infos from players_list
        table.align = "l"
        for tournament_round in tournament_rounds_list:
            round_name = tournament_round[0]
            for match in tournament_round[2]:
                player1_id, player1_last_name,\
                    player1_first_name, player1_score = \
                    match[0]["Player 1"]
                player2_id, player2_last_name,\
                    player2_first_name, player2_score = \
                    match[1]["Player 2"]
                result = match[2]["Result"]
                table.add_row(
                    [round_name, f"{player1_last_name} {player1_first_name}",
                     result,
                     f"{player2_last_name} {player2_first_name}"])
        print(table)
