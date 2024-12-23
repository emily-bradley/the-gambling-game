from agent import ExampleAgent, Agent, ExampleAgent2
from bandit import Bandit
from gamble import Gamble
import numpy as np
import os


def test_bandit():
    bandit1 = Bandit(name=0, probability=0.5)
    bandit2 = Bandit(name=1, probability=0)
    bandit3 = Bandit(name=2, probability=1)
    bandit4 = Bandit(name=1, probability=0, reward_amount=5)
    bandit5 = Bandit(name=2, probability=1, reward_amount=5)
    assert bandit1.name == 0
    assert bandit2.name == 1
    assert bandit3.name == 2
    assert isinstance(bandit1.pull(), int)
    assert bandit2.pull() == 0
    assert bandit3.pull() == 1000
    assert bandit4.pull() == 0
    assert bandit5.pull() == 5


def test_agent_initialization(rounds=10):
    bandit = Bandit(name=0, probability=0.5)
    agent = ExampleAgent([bandit], rounds)
    assert isinstance(agent, Agent)
    assert agent.name == 'StaticSelectionAgent'
    assert agent.num_rounds == 10

    # ensure agent takes lists of bandits of various lengths
    for i in range(1, 4):
        # initialize a lit of bandits of i length
        bandits = [Bandit(name=j, probability=0.5) for j in np.arange(0, i)]
        print("bandits")
        print(bandits)
        agent = ExampleAgent(bandits=bandits, num_rounds=rounds)
        assert agent.bandits == bandits


def test_gamble_bandits_and_rounds(num_bandits=1, rounds=1):
    # initialize bandits
    bandits = []
    for i in range(0, num_bandits):
        bandits.append(Bandit(i, np.random.uniform(0, 1)))
    # initialize Agents
    agents = [ExampleAgent2(bandits=bandits, num_rounds=rounds)]
    # initialize Game
    gamble = Gamble(bandits=bandits, agents=agents)
    # run game
    for i in range(0, rounds):
        gamble.execute_round()


def test_gamble():
    # test one round, multi-bandit
    test_gamble_bandits_and_rounds(num_bandits=10, rounds=1)
    # test multi-round, single bandit
    test_gamble_bandits_and_rounds(num_bandits=1, rounds=10)
    # test multi-round, multi-bandit
    test_gamble_bandits_and_rounds(num_bandits=10, rounds=10)


def test_gamble_strings():
    # initialize bandits and agents
    rounds = 1
    bandits = [Bandit(name=0, probability=1)]
    agents = [ExampleAgent(bandits, rounds)]
    # initialize Game
    gamble = Gamble(bandits=bandits, agents=agents)
    # run game
    assert "Leaderboard: \nStaticSelectionAgent:  0 dollars" == str(gamble)
    assert "{'StaticSelectionAgent': 0}" == repr(gamble)
    gamble.execute_round()
    assert "Leaderboard: \nStaticSelectionAgent:  1000 dollars" == str(gamble)
    assert "{'StaticSelectionAgent': 1000}" == repr(gamble)

    bandits = [Bandit(name=0, probability=0)]
    agents = [ExampleAgent(bandits, rounds)]
    # initialize Game
    gamble = Gamble(bandits=bandits, agents=agents)
    # run game
    assert "Leaderboard: \nStaticSelectionAgent:  0 dollars" == str(gamble)
    assert "{'StaticSelectionAgent': 0}" == repr(gamble)
    gamble.execute_round()
    assert "Leaderboard: \nStaticSelectionAgent:  0 dollars" == str(gamble)
    assert "{'StaticSelectionAgent': 0}" == repr(gamble)


def test_all_agents():
    num_bandits = 10
    rounds = 100
    # initialize bandits
    bandits = []
    for i in range(0, num_bandits):
        bandits.append(Bandit(i, np.random.uniform(0, 1)))
    # initialize Agents
    agents = [cls(bandits=bandits, num_rounds=rounds) for cls in Agent.__subclasses__()]
    # initialize Game
    gamble = Gamble(bandits, agents)
    for i in range(0, rounds):
        gamble.execute_round()


def test_run_game():
    os.system("python3 run_game.py -b 1 -r 1")
    os.system("python3 run_game.py -b 1 -r 10")
    os.system("python3 run_game.py -b 10 -r 1")
    os.system("python3 run_game.py -b 10 -r 10")
