Classes
========

The Gambling Game is composed of 3 classes: ``Gamble``, ``Bandit``, and ``Agent``.
During the game, a series of rounds are executed with ``Gamble.execute_round()``.
Each round, ``Bandits`` are available for ``Agents`` to select.
Each ``Bandit`` has a pre-determined probability of dispensing a reward.
The goal is for the ``Agent`` to employ a strategy that optimizes the
amount of rewards received by the end of the game (when the rounds are exhausted).

.. note::
   The only code you will need to edit/change the ``Agent`` code. A template is provided in agent_template.py

Bandits
-------
.. automodule:: bandit
    :members:

**Notes:**

The current class structure expects an **int** value for ``reward_amount``. Future enhancements could return various ranges or distributions.

**Examples:**

>>> from bandit import Bandit
>>> always_reward_bandit = Bandit(name=1, probability=1)
>>> always_reward_bandit.pull()
1000
>>> never_reward_bandit = Bandit(name=2, probability=0)
>>> never_reward_bandit.pull()
0

Agents
-------
.. automodule:: agent

.. autoclass:: Agent
    :members:

.. autoclass:: ExampleAgent

.. autoclass:: ExampleAgent2

**Notes:**

You will need to implement your own ``Agent`` class, similar to the way in which ``ExampleAgent`` and ``ExampleAgent2`` were implemented.

**Examples:**

>>> from agent import ExampleAgent
>>> from bandit import Bandit
>>> always_reward_bandit1 = Bandit(name=1, probability=1)
>>> always_reward_bandit2 = Bandit(name=2, probability=1)
>>> bandits = [always_reward_bandit, always_reward_bandit2]
>>> my_static_agent = ExampleAgent(bandits=bandits, num_rounds=1000)
1000

Gamble
-------
.. automodule:: gamble
    :members:

**Notes:**

For the Gambling Game, ``gamble`` will be run from `run_game.py`.

**Examples:**

>>> from agent import ExampleAgent, ExampleAgent2
>>> from bandit import Bandit
>>> from gamble import Gamble
>>> num_rounds = 1000
>>> always_reward_bandit1 = Bandit(name=1, probability=1)
>>> always_reward_bandit2 = Bandit(name=2, probability=1)
>>> bandits = [always_reward_bandit, always_reward_bandit2]
>>> my_static_agent = ExampleAgent(bandits=bandits, num_rounds=num_rounds)
>>> my_random_agent = ExampleAgent2(bandits=bandits, num_rounds=num_rounds)
>>> agents = [my_static_agent, my_random_agent]
>>> gamble = Gamble(bandits=bandits, agents=agents)
>>>    for i in range(0, num_rounds):
>>>        gamble.execute_round()

