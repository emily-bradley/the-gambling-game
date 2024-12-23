# The Gambling Game
You are a player in a casino. However, this casino is no ordinary
casino. It is composed entirely of slot machines. Furthermore,
these slot machines have a pre-determined and static probability
of dispensing a reward. And they all pay out at the same rate - $1000!
It occurs to you that, if you can find the machines with the highest
probability of giving a reward, you can receive more rewards over time.
This is your chance to finally beat the house! There is only one problem - 
you have limited resources. These slot machines only accept special
tokens, of which you only have 1000. You start to wonder,
given your limited resources, how you might develop a strategy
for maximizing the amount of money you leave the casino with...

# Background
The casino scenario is an example of a classic data science problem: the multi-armed bandit (MAB) problem. 
In MAB, there exists a set of bandits (such as slot machines) which have some
hidden probability of dispensing a reward.
During each round, the player can choose one bandit, or arm, to "pull". 
The selected choice will either dispense a reward (1000 in our case) or 
return no reward (0).
The objective is to develop an algorithm that maximizes the rewards 
earned over the entire game. 
Successful strategies can quickly identify the machine or set of machines with the 
highest likelihood of reward.

This problem demonstrates the data science concept of the exploration/exploitation
tradeoff.
Some portion of time (i.e. rounds or tokens) must be spent "exploring" 
bandits in order to further our understanding of the reward probability. 
A strategy that *always* selects a bandit at random would be an example 
of an "explore only" strategy. This strategy is demonstrated in the 
simulation's example agent (ExampleAgent):
```
self.static_selection = random.choice(self.bandits)

def action(self):
    return self.static_selection
```
Likewise, a strategy that *always* selects the same bandit would 
be an example of an "exploit only" strategy. This strategy is 
demonstrated in another example agent (ExampleAgent2):
```
def action(self):
    bandit_choice = random.choice(self.bandits)
    return bandit_choice
```

MAB is a reinforcement 
learning problem, which means a player will receive feedback after 
each choice is made. This paradigm enables your agent 
to update its algorithm each round using feedback from the environment. Updating
your agent can enable more sophisticated approaches than the two defined above.

In this game, we represent an over-simplified version of the problem, 
in which the reward probabilities are non-changing and rewards remain 
the same across all machines. However, this simulation lends itself to
expansions on the problem, which are applicable to a variety of real-world 
problems such as:
* design of experimental trials
* media recommendations (i.e. at movies or music)
* advertisement personalization

### Data Science Terms and Concepts
* reinforcement learning
* explore/exploit
* regret
* limited resource allocation dilemma
* online learning
* convergence
* long-tail effect

# Game Framework
The `run_game.py` is the main file in this program; it runs imports and executes the various classes.
run_game takes 2 parameters: `bandits` and `rounds`. `bandits` represents the number of bandits to
initialize. This will be the number of available slot machines to explore. The default is 3 slot machines.
`rounds` is an integer that represents the number of "chances" or "tokens" your agent will be given. Default
is 1000 rounds.

Execute a simulation on the command line:
```
python3 run_game.py --bandits 3 --rounds 1000
```

The `Gamble` class is the heart of the game; it controls each round with `execute_round`.
`Gamble` represents the environment of the reinforcement learning problem. It retains the 
`Agent` and `Bandit` objects, and tracks the performance of each competitor over time.

The `Bandit` class lays out the structure for a slot machine bandit. Bandits are named
in sequential order (i.e. 1, 2, 3, etc.).

The `Agent` class sets the structure for competing in the game. 
**The agent.py file is the *only* file you need to edit**
You will be responsible for developing your own implementation of an agent class.
The Agent ABC class must be inherited; all agents should implement an `action` and `update` method.
The `action` method returns a bandit to pull. The `update` method takes the reward information 
that results from an action.

**note**: A surprise change will be introduced half-way through the competition!
It would behoove you to think generally about the problem.

# How to Win
The game objective is to maximize the amount of rewards over time, or to 
**minimize regret**. Regret is the difference between the rewards an
agent received and the total rewards possible, given the optimal choice
was selected each round.

$regret = \sum_{i=0}^{n} max(A) - \sum_{i=0}^{n} \hat{a}$

Regret is the difference between the sum of all rewards possible
and the sum of rewards received, where A is the set of all possible actions
and $\hat{a}$ is the action selected or "pulled" at each time step.

### How Submit an Agent

#### 1. Clone the Repo
   * Checkout a feature branch: `git checkout -b my_team_name`
#### 2. Install Requirements 
   * Create a virtual environment `python -m venv .venv`
   * Activate the virtual environment `source .venv/bin/activate`
   * Install requirements: `pip install -r requirements.txt`
   * Test the game: `python run_game.py`
#### 3. Build and Agent
   * Work with your team to create a new agent instance **inside `agent.py`**
     1. **Copy the template** from `agent_template.py` and paste it into `agent.py`
     2. **Name your agent** class and the `name` attribute, which will be displayed on the leaderboard.
     3. **Develop an action strategy** that will choose a bandit object when called
     4. **Develop an update strategy** that will update your algorithm, give a bandit choice and the reward
#### 4. Test your competitor
   * Execute `python run_game.py` to import your competitor(s) from `agent.py`
   * **Tip**: You can develop multiple competitors and have them compete against eachother
   * `run_game.py` can take in 3 parameters: `bandits`, `rounds`, and `plot`
     * `-b` number of bandits to initialize
     * `-r` number of rounds to run
     * `-p` plot indicator (boolean value)
     * example: `python run_game.py -r 100000 -b 100 -p True`
   * Run `pytest test_classes.py` before submitting a PR
#### 5. Submit a pull request
   * To submit your agent, create a PR off of your feature branch into main


# Further Research and Resources
* [Article: What is the Multi-Armed Bandit Problem](https://lilianweng.github.io/posts/2018-01-23-multi-armed-bandit/)
* [Video: Multi-Armed Bandit Intro](https://www.youtube.com/watch?v=bkw6hWvh_3k)
* [Video: A/B Testing vs Multi-Armed Bandit](https://www.youtube.com/watch?v=VrFZCGCwzVc)
* [Real-World Use Case: Spotify Multi-Objective Contextual Bandits Use Case](https://www.youtube.com/watch?v=KoMKgNeUX4k)
* [Real-World Use Case: Stitch Fix Multi-Armed Bandit Recommendations](https://multithreaded.stitchfix.com/blog/2020/08/05/bandits/)
* [Research Paper: The Sample Complexity of Exploration in the Multi-Armed Bandit Problem](https://www.jmlr.org/papers/volume5/mannor04b/mannor04b.pdf)
