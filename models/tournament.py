from tinydb import TinyDB


class Tournament:
    def __init__(self,
                 tournament_id: int = 0,
                 tournament_name: str = "",
                 tournament_location: str = "",
                 tournament_start_date: str = "",
                 tournament_end_date: str = "",
                 tournament_start_time: str = "",
                 tournament_end_time: str = "",
                 tournament_rounds_number: int = 4,
                 tournament_current_round: int = 1,
                 tournament_rounds_list: list = [],
                 tournament_players_list: list = [],
                 tournament_description: str = ""):

        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.tournament_start_time = tournament_start_time
        self.tournament_end_time = tournament_end_time
        self.tournament_rounds_number = tournament_rounds_number
        self.tournament_current_round = tournament_current_round
        self.tournament_rounds_list = tournament_rounds_list
        self.tournament_players_list = tournament_players_list
        self.tournament_description = tournament_description

        self.tournament_db = TinyDB('./database/tournament_db.json')

    def tournament_format(self):
        """Return tournament infos in a dict"""
        return {
            "tournament_id": self.tournament_id,
            "tournament_name": self.tournament_name,
            "tournament_location": self.tournament_location,
            "tournament_start_date": self.tournament_start_date,
            "tournament_end_date": self.tournament_end_date,
            "tournament_start_time": self.tournament_start_time,
            "tournament_end_time": self.tournament_end_time,
            "tournament_rounds_number": self.tournament_rounds_number,
            "tournament_current_round": self.tournament_current_round,
            "tournament_rounds_list": self.tournament_rounds_list,
            "tournament_players_list": self.tournament_players_list,
            "tournament_description": self.tournament_description
        }

    def add_tournament_to_db(self):
        """Add tournament to database"""
        new_tournament_data = self.tournament_format()

        if self.tournament_db.contains(doc_id=self.tournament_id):
            self.tournament_db.update(new_tournament_data, doc_ids=[
                                                            self.tournament_id]
                                      )
        else:
            tournament_list = self.tournament_db.all()
            if tournament_list:
                last_tournament = tournament_list[-1]
                last_tournament_id = last_tournament.get("tournament_id", 0)
            else:
                last_tournament_id = 0

            # Increment the tournament ID to obtain
            # the ID of the new tournament
            new_tournament_id = last_tournament_id + 1
            # Add the new tournament to the database with the correct ID
            new_tournament_data["tournament_id"] = new_tournament_id
            self.tournament_db.insert(new_tournament_data)
