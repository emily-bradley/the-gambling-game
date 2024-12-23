"""
This is the Bandit class.
A Bandit is a slot machine that has a chance to dispense a static reward amount.
Bandits are called each round to return a reward based on their probability.
"""

import numpy as np


class Bandit:
    """
    A slot machine with a probability of returning a static reward.

    Bandit is the object for gambling on in the Gambling Game.
    Each bandit has a unique name, which is typically numerical order.

    :ivar int name: an identifier for the bandit; typically sequential order
    :ivar float probability: value between 0 and 1 that represents the probability of dispensing a reward
    :ivar int reward_amount: the amount rewarded in pull() based on probability, defaults to 1000
    """

    def __init__(self, name, probability, reward_amount=1000):
        """Constructor method
        """
        self.name = name
        self.__probability = probability
        self.__reward_amount = reward_amount

    def pull(self):
        """
        Pull the bandit's arm to try and win the hidden reward_amount.
        The bandit has a hidden probability of dispensing the reward_amount.
        Reward is discrete - pull() returns either a reward or 0.

        :return: *int* of 0 if random number is > reward probability or reward_amount if probability is < reward probability
        """
        if np.random.uniform(0, 1) < self.__probability:
            return self.__reward_amount
        return 0
