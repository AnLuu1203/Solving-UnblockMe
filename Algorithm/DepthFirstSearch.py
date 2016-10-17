import random
from State.Board import *


#kiểm tra newState có nằm trong listState hay không
def checkState(newState, listState):
  for state in listState:
    if newState.depth >= state.depth:
      if newState.createBoard(0) == state.createBoard(0):
        return True
  return False

#DFS
def solveDFS(startState, depth = 500):
  stack = [startState]
  visited = []

  while stack != []:
    currentState = stack.pop()

    if currentState.checkGoal():
      return currentState

    if checkState(currentState,visited):
      continue

    visited += [currentState]

    if currentState.depth < depth:
      nextStates = currentState.generateNextStates(currentState.parentMove[0])

      for state in nextStates:
        if state.checkGoal():
          return state

      nextStates = random.sample(nextStates, len(nextStates))

      for s in nextStates:
        stack = stack + [s]

  return None
