"""
'run_game' is the program that runs the Bidding Game.
'run_game' has one function, 'run_game' that initializes
the agents, initializes the bandits, creates the game,
and executes each round of the game. A graph of reward
accumulation over time is plotted at the end of the game.
"""
import numpy as np

from bandit import Bandit
from agent import Agent
from gamble import Gamble

import argparse


def run_game():
    """
    Function that runs the Gambling Game.
    'run_game' accept s3 command line arguments:
    'bandits' (int) - the number of bandits to choose from
    'rounds' (int) - the number of gambling rounds to execute
    'plot' (bool) - an indicator that display the gamble history of the game
    """
    # Set the program arguments
    parser = argparse.ArgumentParser(description="Gambling Run Game",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-b", "--bandits", default=3, help="number of bandits to initialize")
    parser.add_argument("-r", "--rounds", default=1000, help="number of rounds to initialize")
    parser.add_argument("-p", "--plot", default=False, help="display the gamble history graph")
    args = vars(parser.parse_args())
    num_bandits = int(args["bandits"])
    rounds = int(args["rounds"])
    plot = bool(args["plot"])

    print("\nStarting the Gambling Game...")
    print("Test your luck to see if you can win!\n------")

    # Step 1: initialize bandits
    bandits = []
    for i in range(0, num_bandits):
        bandits.append(Bandit(i, np.random.uniform(0, 1)))
    print(f"""{len(bandits)} Bandits available""")

    # Step 2: Initialize Agents
    agents = [cls(bandits=bandits, num_rounds=rounds) for cls in Agent.__subclasses__()]
    print(f"""{len(agents)} player(s) competing:""")
    for agent in agents:
        print(f"""-> {agent.name}""")
    print("Let the games begin!")

    # Step 3: Initialize Game
    gamble = Gamble(bandits=bandits, agents=agents)
    for i in range(0, rounds):
        gamble.execute_round()

    # Step 4: Print Results
    gamble.print_final_leaderboard()
    print("------\nThe game has ended.\n")

    if plot:
        gamble.plot_history()


if __name__ == '__main__':
    run_game()
