Usage
=====

Run Game
--------

.. automodule:: run_game
    :members:

**Examples:**

>>> python run_game.py
Starting the Gambling Game...
Test your luck to see if you can win!
------
3 Bandits available
2 player(s) competing:
-> StaticSelectionAgent
-> RandomSelectionAgent
Let the games begin!
------
Leaderboard:
RandomSelectionAgent:  486000 dollars  (WINNER!)
StaticSelectionAgent:  104000 dollars
------
The game has ended.

>>> python run_game.py -b 10 -r 1000 -p True
Starting the Gambling Game...
Test your luck to see if you can win!
------
10 Bandits available
2 player(s) competing:
-> StaticSelectionAgent
-> RandomSelectionAgent
Let the games begin!
------
Leaderboard:
RandomSelectionAgent:  474000 dollars  (WINNER!)
StaticSelectionAgent:  393000 dollars
------
The game has ended.


How to Compete
--------------

Copy the format in the `agent_template.py` file into the end of the `agent.py` file::

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

Follow the tasks in the `TODO` prompts, then create a Pull Request to the main branch