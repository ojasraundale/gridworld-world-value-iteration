# gridworld-world-value-iteration
Value Iteration algorithm to find the optimal policy for the Gridworld Problem

## About
This repo is derived from a homework assignment from the course COMPSCI 687: Reinforcement Learning, Fall '23 at the University of Massachusetts, Amherst. Following is the gridworld on which the value iteration algorithm is implemented:

![Gridworld 687](687_gridworld.png)

- **State:** This problem consists of a 5x5 grid world where each state \(s=(r,c)\) describes the current coordinates/location of the agent. In particular, \(r \in [0,4]\) is the current row where the agent is located and \(c \in [0,4]\) is the current column where the agent is located. Refer to Figure [gridworld](#gridworld) for an example. In this figure, the topmost row is row zero, and the leftmost column is column zero—i.e., *State1* corresponds to \(s=(0,0)\) and *State16* corresponds to \(s=(3,1)\).

- **Actions:** There are four actions: AttemptUp (AU), AttemptDown (AD), AttemptLeft (AL), and AttemptRight (AR).

- **Dynamics:** This is a *stochastic* MDP:
  - With 80% probability, the agent moves in the specified direction.
  - With 5% probability, the agent gets confused and veers to the right with respect to the intended direction.
  - With 5% probability, the agent gets confused and veers to the left with respect to the intended direction.
  - With 10% probability, the agent temporarily breaks and does not move.
  - The grid world is surrounded by walls. If the agent hits a wall, it stays in its current state.
  - There are two *Obstacle states* in this domain: one in state (2,2) and one in state (3,2). If the agent hits an obstacle, it stays in its current state. The agent cannot enter an Obstacle state.
  - There is a *Water state* located at (4,2).
  - There is a *Goal state* located at (4,4).

- **Rewards:** The reward is always 0, except when transitioning to (entering) the Goal state, in which case the reward is 10; or when transitioning to (entering) the Water state, in which case the reward is -10. Notice that, in order to model this type of reward function, you will need to use a reward function in the form \(R(S_t, A_t, S_{t+1})\), instead of \(R(S_t, A_t)\). This requires a small modification to the Value Iteration update equation: \(v_{i+1}(s) := \underset{a\in\mathcal{A}}{\max}\,\,\sum_{s'} p(s, a, s') \Big( R\big(s,a,s'\big) + \gamma v_i(s') \Big)\).

- **Terminal State:** The Goal state is terminal. Any actions executed in this state always transition to \(s_\infty\) with reward 0.

- **Discount:** Unless otherwise specified, \(\gamma=0.9\).

- **Initial State:** \(S_0=(0,0)\), deterministically.

[gridworld]: /687_gridworld.png "Gridworld Example"


