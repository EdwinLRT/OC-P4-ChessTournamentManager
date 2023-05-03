from tinydb import TinyDB
from views.menu import MenuViews
from views.round import RoundViews


class PlayerController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.round_views = RoundViews()

    @staticmethod
    def display_all_players():
        player_db = TinyDB('./database/player_db.json')
        table = player_db.table('_default')
        all_players = table.all()
        players_list = []
        i = 0
        for player in all_players:
            players_list.append(player)
            print(f"[{i + 1}]  |"
                  f"  {player['chess_id']} |"
                  f" {player['name']} {player['surname']}")
            i += 1
        return players_list
