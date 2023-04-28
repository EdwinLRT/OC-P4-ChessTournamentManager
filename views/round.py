class RoundViews:
    def __init__(self):
        # self.table = PrettyTable()
        self.round_field_names = [
            "Match #",
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]
        self.results_field_names = [
            "Tournament ranking",
            "Name",
            "Final Score",
            "Global ranking"
        ]

    def display_matches(self, matches):
        """Display matches for current round as table
        @param matches: list of matches tuples
        """
        self.table.clear()
        self.table.field_names = self.round_field_names
        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i + 1))
            row.insert(4, "vs.")
            self.table.add_row(row)
        print(self.table)

    def display_results(self, t):
        """Display results at the end of the tournament
        @param t: current tournament
        """
        self.table.clear()
        self.table.field_names = self.results_field_names
        for i in range(len(t.players)):
            self.table.add_row([
                i + 1,
                t.players[i]["last_name"] + ", " + t.players[i]["first_name"],
                t.players[i]["score"],
                t.players[i]["rank"]
            ])
        print("\n\n- FINAL SCORES -\n")
