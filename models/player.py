from tinydb import TinyDB


class Player:
    def __init__(self,
                 player_id: int = 0,
                 player_name: str = "",
                 player_surname: str = "",
                 player_birthday: str = "",
                 player_elo: int = 0):

        self.player_id = player_id
        self.player_name = player_name
        self.player_surname = player_surname
        self.player_birthday = player_birthday
        self.player_elo = player_elo
        self.player_score = 0.0
        self.player_opponents = []

        self.player_db = TinyDB('./database/player_db.json')

    def player_format(self):
        """Return player infos in a dict"""
        return {
            "chess_id": self.player_id,
            "name": self.player_name,
            "surname": self.player_surname,
            "birth_date": self.player_birthday,
            "elo": self.player_elo,
            "score": self.player_score,
            "opponents": self.player_opponents
        }

    def add_player_to_db(self):
        """Add tournament to database"""
        new_player_data = self.player_format()
        if self.player_db.contains(doc_id=self.player_id):
            self.player_db.update(new_player_data, doc_ids=[self.player_id])
        else:
            self.player_db.insert(new_player_data)

    def get_all_players(self):
        all_players = self.table.all()
        players_list = []
        for player in all_players:
            players_list.append(player)
        return players_list
