from random import random


# TODO: name your agent class; Must be unique among other agents
class MyAgent(Agent):
    # TODO: name your agent; This will appear in the graph and leaderboard
    name = 'MyAgentName'
    """
    A simple description of your agent
    
    Authors:
    Contributors to this agent
    """

    def __init__(self, bandits, num_rounds):
        super().__init__(bandits, num_rounds)

    def action(self):
        # TODO: replace this random bandit selection with your algorithm
        bandit_choice = random.choice(self.bandits)
        # return a bandit object as the "arm" to pull
        return bandit_choice

    def update(self, bandit, reward):
        # TODO: update your algorithm using data about the reward for a given bandit
        return
