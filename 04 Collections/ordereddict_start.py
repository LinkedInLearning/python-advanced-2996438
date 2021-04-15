# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # TODO: create an ordered dictionary of the teams

    # TODO: Use popitem to remove the top item

    # TODO: What are next the top 4 teams?

    # TODO: test for equality

if __name__ == "__main__":
    main()
