"""
This is the Gamble class.
Gamble is a game, involving a set of Agents and a set of Bandits.
Agents are rewarded each round, based on  the reward probability of the Bandit they select.
The Agent with the most rewards at the end of the game (i.e. when all rounds are
complete) is the winner.
"""

import numpy as np
from matplotlib import pyplot as plt


class Gamble:
    """
    Gamble is a game that can be executed one round at a time.
    The end of the game is determined externally (when no more rounds are executed).
    All of the attributes for tracking performance are available within this class.

    :ivar list _bandits: list of bandit objects available in the game
    :ivar list _agents: list of all agent objects participating in the game
    :ivar dictionary _agent_rewards: current rewards for each agent; initially 0
    :ivar dictionary _agent_rewards_over_time: rewards each round for plotting
    """

    def __init__(self, bandits, agents):
        """Constructor method
        """
        # list of bandit objects
        self._bandits = bandits
        # list of all agent objects.
        self._agents = agents
        # dictionary of the current rewards for each agent; initially 0
        self._agent_rewards = {agent.name: 0 for agent in self._agents}
        # dictionary of the rewards each round for plotting
        self._agent_rewards_over_time = {agent.name: [] for agent in self._agents}

    def __repr__(self):
        return str(self._agent_rewards)

    def __str__(self):
        gamble_str = "Leaderboard: "
        agent_view = [(self._agent_rewards[agent.name], agent.name) for agent in self._agents]
        agent_view.sort(reverse=True)  # natively sort tuples by first element
        for reward, agent in agent_view:
            gamble_str += f"""\n{agent}:  {reward} dollars"""
        return gamble_str

    def execute_round(self):
        """
        Play a round of the gambling game.
        Get rewards for all bandidt,
        call all agents to choose their bandit,
        update all agents with their respective rewards,
        and update game data.
        """
        # step 1: get rewards for bandits this round
        bandit_rewards = [bandit.pull() for bandit in self._bandits]

        # step 2: call all agent players to select their gambling choice; return the reward
        for agent in self._agents:
            # get the bandit award based on the agent action
            selected_bandit = agent.action().name
            reward = bandit_rewards[selected_bandit]
            # step 3: return rewards to each agent
            agent.update(selected_bandit, reward)
            # step 4: update agent balances by reward amount dollar if the agent pulled that bandit
            self._agent_rewards[agent.name] += reward
            # step 5: update data for plotting
            self._agent_rewards_over_time[agent.name].append(self._agent_rewards[agent.name])

    def print_final_leaderboard(self):
        """
        Prints the leaderboard of all agents based on their agent.name and total winnings.
        The leaderboard is sorted and identifies the winning agent.
        """
        print("------\nLeaderboard:")
        agent_view = [(self._agent_rewards[agent.name], agent.name) for agent in self._agents]
        agent_view.sort(reverse=True)  # natively sort tuples by first element
        winner = agent_view[0][1]
        for reward, agent in agent_view:
            end = "\n"
            if agent == winner:
                end = "  (WINNER!)\n"
            print(f"""{agent}:  {reward} dollars""", end=end)

    def plot_history(self):
        """
        Creates a visual representation of how the gambling game has progressed.
        Number of Rounds is on the x-axis and Total Agent Rewards for each agent
        is on the y-axis. Plots a matplotlib graph with each agent.name in
        the legend.
        """
        # plot the data
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        # plot
        for agent_name, winnings in self._agent_rewards_over_time.items():
            # the x-axis is the number of rounds
            rounds = np.arange(0, len(winnings))
            # print(winnings)
            plt.plot(rounds, winnings, label=f"{agent_name}")

        # include the legend
        plt.legend()

        # labels
        plt.xlabel("Number of Rounds")
        plt.ylabel("Total Agent Rewards")
        ax.set_title("Agent Winnings Over Time")

        # display the plot
        plt.show()
