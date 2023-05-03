from views.menu import MenuViews
from views.round import RoundViews
from models.player import Player


class PlayerController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.round_views = RoundViews()
        self.player_model = Player()

    @staticmethod
    def display_all_players(self):
        all_players = self.player_model.get_all_players()
        players_list = []
        i = 0
        for player in all_players:
            players_list.append(player)
            print(f"[{i + 1}]  |"
                  f"  {player['chess_id']} |"
                  f" {player['name']} {player['surname']}")
            i += 1
        return players_list
