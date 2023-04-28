class TournamentViews:
    def __init__(self):
        pass

    @staticmethod
    def display_tournament_title():
        print("\n\n--- Créer un nouveau tournoi ---\n")

    @staticmethod
    def tournament_info_review(new_tournament, tournament_players_list):
        """"Review tournament information before saving to database"""
        print("\n\n----- Résumé des informations du tournoi -----\n")
        print(f"Nom du tournoi : {new_tournament[1]}")
        print(f"Lieu : {new_tournament[2]}")
        print(f"Date de début : {new_tournament[3]}")
        print(f"Date de fin : {new_tournament[4]}")
        print(f"Nombre de tours : {new_tournament[7]}")
        player_names = [f"{p['name']} {p['surname']}" for p
                        in tournament_players_list]
        print(f"Liste des participants : {', '.join(player_names)}")
        print(f"Commentaire du directeur de tournoi : {new_tournament[11]}")
        print("\n\nSouhaitez-vous ajouter ces données"
              " à la base de donnée de tournois ? (Y/N):")

    @staticmethod
    def tournament_saved_to_database():
        print("\nLe tournoi a été ajouté avec succès à la base de données.")

    @staticmethod
    def tournament_not_saved_to_database():
        print("\nLe tournoi n'a pas été ajouté à la base de données.")

    @staticmethod
    def display_tournament_list_title():
        print("\n\n--- Liste des tournois ---\n")

    @staticmethod
    def display_tournament_list():
        print("\n\n----- Liste des tournois -----\n")

    @staticmethod
    def display_tournament_selected_players(player, selected_players):
        print("Vous avez choisi les joueurs suivants :")
        i = 0
        for player in selected_players:
            print(f"[{i + 1}]  |"
                  f"  {player['chess_id']} |"
                  f" {player['name']} {player['surname']}")
            i += 1

    @staticmethod
    def display_tournament_players(selected_tournament):
        print("Les joueurs inscrits au tournoi sont :")
        i = 1
        for player in selected_tournament["tournament_players_list"]:
            print(f"[{i}] {player['surname']} {player['name']} ")
            i += 1

    @staticmethod
    def display_tournament_name_location(selected_tournament):
        print("\nVous avez choisi le tournoi suivant :")
        print(f" Nom  | {selected_tournament['tournament_name']}")
        print(f" Lieu | {selected_tournament['tournament_location']}")
        print(
            f" Round actuel |"
            f" {selected_tournament['tournament_current_round']} "
            f"sur {selected_tournament['tournament_rounds_number']}")

    @staticmethod
    def input_player_selection(player, players_list):
        player_selection = input(f"Choisissez le joueur"
                                 f" {player + 1} (1-{len(players_list)}): ")
        return player_selection

    @staticmethod
    def already_selected_player():
        print("Ce joueur a déjà été sélectionné."
              " Veuillez en choisir un autre.")

    @staticmethod
    def invalid_input():
        print("\nEntrée invalide. Veuillez entrer un nombre valide"
              " dans la plage spécifiée.")

    @staticmethod
    def display_title_select_tournament():
        print("\n\n--- Sélectionner un tournoi ---\n")

    @staticmethod
    def display_tournament_indexed_list(i, tournament):
        print(f"[{i + 1}]  |"
              f"  {tournament['tournament_name']} |"
              f" {tournament['tournament_location']}")

    @staticmethod
    def input_tournament_selection(tournaments_list):
        tournament_selection = input(f"Choisissez un tournoi"
                                     f" (1-{len(tournaments_list)}): ")
        return tournament_selection

    @staticmethod
    def display_players_or_continue():
        print("\n\nSéléctionnez une des options suivantes :\n")
        user_input = input("[1] Afficher la liste des participants\n"
                           "[2] Continuer\n"
                           "[3] Retour au menu principal\n"
                           "Votre choix : ")
        return user_input

    @staticmethod
    def input_tournament_start_time():
        tournament_start_time = input(
            "\nAppuyez sur entrée pour commencer le tournoi"
            " (La date et l'heure de début"
            " seront enregistrées automatiquement) : ")
        return tournament_start_time

    @staticmethod
    def display_tournament_start_time(selected_tournament):
        print(f"\n[TIME] Date et heure de début |"
              f" {selected_tournament['tournament_start_time']}")

    @staticmethod
    def input_tournament_end_time():
        tournament_end_time = input(
            "\nAppuyez sur entrée pour terminer le tournoi"
            " (La date et l'heure de fin"
            " seront enregistrées automatiquement) : ")
        return tournament_end_time

    @staticmethod
    def display_tournament_end_time(selected_tournament):
        print(f"\n[TIME] Date et heure de fin |"
              f" {selected_tournament['tournament_end_time']}")
        print("\n\nLe tournoi est terminé."
              " Vous pouvez maintenant consulter les résultats.")

    @staticmethod
    def input_round_start_time():
        tournament_start_round = input(
            "\nAppuyez sur entrée pour commencer le round "
            "(La date et l'heure de début"
            " seront enregistrées automatiquement) : ")
        return tournament_start_round

    @staticmethod
    def display_round_start_time(selected_tournament):
        print(f"\n[TIME] Date et heure de début de round |"
              f" {selected_tournament['round_start_time']}")

    @staticmethod
    def input_round_end_time():
        tournament_end_round = input(
            "\nAppuyez sur entrée pour terminer le round"
            " (La date et l'heure de fin"
            " seront enregistrées automatiquement) : ")
        return tournament_end_round

    @staticmethod
    def display_round_end_time(selected_tournament):
        print(f"\n[TIME] Date et heure de fin de round |"
              f" {selected_tournament['round_end_time']}")

    @staticmethod
    def input_match_result(match):
        match_result = input(
            f"\nVictoire du joueur 1 : 1,"
            f" Victoire du joueur 2 : 2,"
            f" Match nul : 0 "
            f"\nEntrez le résultat du match entre"
            f" {match[0]['Player 1'][2]} {match[0]['Player 1'][1]}"
            f" et {match[1]['Player 2'][2]} {match[1]['Player 2'][1]} :")
        return match_result

    @staticmethod
    def display_match_in_round_title():
        print("--- Matchs du round ---\n")

    @staticmethod
    def display_match_in_round(pair):
        print('[1]-', pair[0]['surname'] + ' '
              + pair[0]['name'], "-vs-", '[2]-',
              pair[1]['surname'] + ' ' + pair[1]['name'])

    @staticmethod
    def display_round_title(round_number='1'):
        print(f"\n\n--- Round {round_number} ---\n")

    @staticmethod
    def display_tournament_already_ended():
        print("\nLe tournoi est déjà terminé. Vous ne pouvez plus le modifier."
              "Vous pouvez le consulter en générant le rapport du tournoi.")

    @staticmethod
    def display_final_scores(sorted_players):
        print("\n\n--- Scores finaux ---\n")
        for i, player in enumerate(sorted_players):
            print(f"{i + 1}. "
                  f"{player['name']}"
                  f" {player['surname']}"
                  f" ({player['chess_id']})"
                  f" - score: {player['score']}")
