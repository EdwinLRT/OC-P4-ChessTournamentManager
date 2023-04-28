from tinydb import TinyDB


class MenuViews:
    def __init__(self):
        pass

    @staticmethod
    def display_menu_title():
        print("-------------Chess Tournament  Manager-------------")
        print("Bienvenue dans le gestionnaire de tournois d'échecs")

    @staticmethod
    def display_menu():
        print("\n----- Menu principal -----\n")
        print("Saisissez un chiffre pour naviguer dans le menu.\n")
        print("[1] Nouvel utilisateur")
        print("[2] Nouveau tournoi")
        print("[3] Lancer un tournoi")
        print("[4] Rapports")
        print("[5] Quitter")

    @staticmethod
    def display_report_menu():
        print("\n----- Générer un rapport -----\n")
        print("[1] Tous les joueurs")
        print("[2] Tous les tournois")
        print("[3] Informations sur un tournoi")
        print("[4] Liste des joueurs d'un tournoi")
        print("[5] Liste des tours d'un tournoi et des matchs associés")
        print("[6] Retour au menu principal")

    @staticmethod
    def display_new_user_title():
        print("\n\n--- Créer un nouvel utilisateur ---\n")

    @staticmethod
    def display_new_tournament_title():
        print("\n\n--- Créer un nouveau tournoi ---\n")

    @staticmethod
    def input_new_player():
        player_id = input("ID du joueur/joueuse :") or "000000"
        player_name = input("Nom :") or "Non renseigne"
        player_surname = input("Prénom :") or "Non renseigne"
        player_birthday = input(
            "Date de naissance: (JJMMAAA):") or\
            "Non renseigne"
        player_elo = input("Niveau Elo (<3000):") or "Non renseigne"
        return player_id, player_name, player_surname, \
            player_birthday, player_elo

    @staticmethod
    def input_user_choice():
        user_choice = input("\nVotre choix (Y/N):").lower()
        return user_choice

    @staticmethod
    def player_info_review(new_player):
        """"Review tournament information before saving to database"""
        print("\n\n----- Résumé des informations du tournoi -----\n")
        print(f"Identifiant national: {new_player[0]}")
        print(f"Nom: {new_player[1]}")
        print(f"Prénom: {new_player[2]}")
        print(f"Date de naissance: {new_player[3]}")
        print(f"Elo: {new_player[4]}")
        print("\n\nSouhaitez-vous ajouter ces données"
              " à la base de donnée du joueur/joueuse ? (Y/N):")

    @staticmethod
    def player_saved_to_database():
        print(
            "\nLe joueur/la joueuse a été ajouté"
            " avec succès à la base de données.")

    @staticmethod
    def player_not_saved_to_database():
        print(
            "\nLe joueur/la joueuse n'a pas été ajouté à la base de données.")

    @staticmethod
    def invalid_input():
        print("\nVeuillez saisir une entrée valide.")

    @staticmethod
    def input_new_tournament(self):
        tournament_id = 0
        tournament_name = input("Nom du tournoi :") or "Non renseigne"
        tournament_location = input("Lieu du tournoi :") or "Non renseigne"
        tournament_start_date = input(
            "Date de début du tournoi : (JJMMAAA):") or "Non renseigne"
        tournament_end_date = input(
            "Date de fin du tournoi : (JJMMAAA):") or "Non renseigne"
        tournament_start_time = "Non renseigne"
        tournament_end_time = "Non renseigne"
        tournament_rounds_number = int(input("Nombre de tours :") or 4)
        tournament_players_number = (tournament_rounds_number * 2)
        tournament_current_round = 1
        tournament_rounds_list = []
        tournament_players_list = self.tournament_controller.players_selection(
            tournament_players_number)
        tournament_description = input(
            "Description du tournoi (Notes du directeur de tournoi) :"
        ) or "Non renseigne"
        return tournament_id, tournament_name,\
            tournament_location, tournament_start_date,\
            tournament_end_date, tournament_start_time,\
            tournament_end_time, tournament_rounds_number,\
            tournament_current_round, tournament_rounds_list,\
            tournament_players_list, tournament_description

    @staticmethod
    def tournament_info_review(new_tournament, tournament_players_list):
        """"Review tournament information before saving to database"""
        print("\n\n----- Résumé des informations du tournoi -----\n")
        print(f"Nom du tournoi : {new_tournament[1]}")
        print(f"Lieu : {new_tournament[2]}")
        print(f"Date de début : {new_tournament[3]}")
        print(f"Date de fin : {new_tournament[4]}")
        print(f"Nombre de tours : {new_tournament[7]}")
        player_names = [f"{p['name']} {p['surname']}" for p in
                        tournament_players_list]
        print(f"Liste des participants : {', '.join(player_names)}")
        print(f"Commentaire du directeur de tournoi : {new_tournament[11]}")
        print(
            "\n\nSouhaitez-vous ajouter ces données"
            " à la base de donnée de tournois ? (Y/N):")

    @staticmethod
    def tournament_saved_to_database():
        print("\nLe tournoi a été ajouté avec succès à la base de données.")

    @staticmethod
    def tournament_not_saved_to_database():
        print("\nLe tournoi n'a pas été ajouté à la base de données.")

    @staticmethod
    def display_all_tournaments(self):
        tournament_db = TinyDB('./database/tournament_db.json')
        table = tournament_db.table('_default')
        all_tournaments = table.all()
        tournaments_list = []
        i = 0
        for tournament in all_tournaments:
            tournaments_list.append(tournament)
            print(
                f"[{i + 1}]  |"
                f"  {tournament['tournament_id']} |"
                f" {tournament['tournament_name']} "
                f"{tournament['tournament_location']}")
            i += 1
        return tournaments_list

    @staticmethod
    def software_exit():
        print("\n\nMerci d'avoir utilisé Chess Tournament Manager !\n\n")
        exit()
