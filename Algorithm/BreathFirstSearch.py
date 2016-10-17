from State.Board import *
from State.Brick import *

def isVisited(state, listState):
  for s in listState:
    if state.createBoard(0) == s.createBoard(0):
      return True
  return False

def solveBFS(startState):
  visited = []
  queue = [startState]

  while queue != []:
    currentState = queue.pop()

    if currentState.checkGoal():
      return currentState

    if isVisited(currentState, visited):
      continue

    visited += [currentState]

    nextStates = currentState.generateNextStates(currentState.parentMove[0])

    for s in nextStates:
      queue = [s] + queue

  return None