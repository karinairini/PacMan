# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util #biblioteca  util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    stack = util.Stack()  # Utilizing the stack data structure from the 'util' module

    # Create a set to keep track of visited nodes
    visited = set()

    # Push the start state onto the stack as a tuple (state, actions)
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        state, actions = stack.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Mark the current state as visited
        visited.add(state)

        # Get the next possible actions from the current state
        possible_actions = problem.getActions(state)

        for action in possible_actions:
            # Get the next state and calculate the cost
            next_state = problem.getNextState(state, action)
            cost = problem.getActionCost(state, action, next_state)

            # Check if the next state has not been visited
            if next_state not in visited:
                # Push the next state and actions onto the stack
                stack.push((next_state, actions + [action]))

    # If the stack is empty and no goal state is found, return an empty list
    return []


def breadthFirstSearch(problem):
    queue = util.Queue()  # Using a queue for BFS

    # Create a set to keep track of visited nodes
    visited = set()

    # Push the start state onto the queue as a tuple (state, actions)
    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        state, actions = queue.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Mark the current state as visited
        visited.add(state)

        # Get the next possible actions from the current state
        possible_actions = problem.getActions(state)

        for action in possible_actions:
            # Get the next state and calculate the cost
            next_state = problem.getNextState(state, action)
            cost = problem.getActionCost(state, action, next_state)

            # Check if the next state has not been visited
            if next_state not in visited:
                # Push the next state and actions onto the queue
                queue.push((next_state, actions + [action]))

    # If the queue is empty and no goal state is found, return an empty list
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priority_queue = util.PriorityQueue()  # Utilizing the priority queue data structure from the 'util' module

    # Create a set to keep track of visited nodes
    visited = set()

    # Push the start state onto the priority queue with a priority of 0 (initial cost) and empty list of actions
    priority_queue.push((problem.getStartState(), [], 0), 0)

    while not priority_queue.isEmpty():
        state, actions, cost = priority_queue.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Mark the current state as visited
        visited.add(state)

        # Get the next possible actions from the current state
        possible_actions = problem.getActions(state)

        for action in possible_actions:
            # Get the next state and calculate the action cost and heuristic cost
            next_state = problem.getNextState(state, action)
            action_cost = problem.getActionCost(state, action, next_state)
            heuristic_cost = heuristic(next_state, problem)

            # Calculate the total cost (action cost + heuristic cost)
            total_cost = cost + action_cost + heuristic_cost

            # Check if the next state has not been visited
            if next_state not in visited:
                # Push the next state, actions, and total cost onto the priority queue
                priority_queue.push((next_state, actions + [action], cost + action_cost), total_cost)

    # If the priority queue is empty and no goal state is found, return an empty list
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch