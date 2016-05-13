from State.Board import *
from State.Brick import *
import random


def findBrick_left(state, currentBrick):
	result = []

	x = currentBrick.position[0]
	y = currentBrick.position[1] - 1
	board = state.createBoard(currentBrick.id)

	while y >= 0:
		value = board[x][y]
		if value != 0:
			result = [value] + result
		y -= 1

	return result

def findBrick_right(state,currentBrick):
	result = []

	x = currentBrick.position[0]
	y = currentBrick.position[1] + currentBrick.length
	board = state.createBoard(currentBrick.id)

	while y < 6:
		value = board[x][y]
		if value != 0:
			result = [value] + result
		y += 1

	return result

def findBrick_top(state,currentBrick):
	result = []

	x = currentBrick.position[0]
	y = currentBrick.position[1]
	board = state.createBoard(currentBrick.id)

	while x >= 0:
		value = board[x][y]
		if value != 0:
			result = [value] + result
		x -= 1

	return result

def findBrick_bottom(state, currentBrick):
	result = []

	x = currentBrick.position[0] + currentBrick.length
	y = currentBrick.position[1]
	board = state.createBoard(currentBrick.id)

	while x < 6:
		value = board[x][y]
		if value != 0:
			result = [value] + result
		x += 1

	return result


def heuristicFunc(state):
	block = []
	stack = []

	mainBrick = None

	for brick in state.listBrick:
		if brick.id == 1:
			mainBrick = brick
			break

	if mainBrick != None:
		stack = stack + findBrick_right(state,mainBrick)

	while stack != []:
		currentBrickId = stack.pop()

		if currentBrickId in block:
			continue
		else:
			block += [currentBrickId]

		currentBrick = state.findBrickById(currentBrickId)

		if currentBrick.isVetical:
			top = findBrick_top(state,currentBrick)
			bottom = findBrick_bottom(state,currentBrick)

			stack = stack + top
			stack = stack + bottom
			
		else:
			left = findBrick_left(state,currentBrick)
			right = findBrick_right(state,currentBrick)

			stack = stack + left
			stack = stack + right
			
	return len(block)


def checkState(state, listState):
	for s in listState:
		if state.createBoard(0) == s.createBoard(0):
			return True
	return False


'''	
def simple_hill_climbing(startState,depth = 100):
	stack = [startState]
	visited = []

	while stack != []:
		currentState = stack.pop()

		if currentState.checkGoal():
			return currentState

		visited += [currentState]


		nextStates = currentState.generateNextStates(currentState.parentMove[0])
		nextStates = random.sample(nextStates, len(nextStates))
		for state in nextStates:
			if checkState(state,visited):
				continue
			else:
				if heuristicFunc(state) <= heuristicFunc(currentState):
					stack += [state]
					print(heuristicFunc(state))
					break;

	return None
'''

def steepest_ascent_hill_climbing(startState, depth = 500):
	stack = [startState]
	visited = []

	while stack != []:
		currentState = stack.pop()

		if currentState.checkGoal():
			return currentState

		visited += [currentState]


		if currentState.depth < depth:
			nextStates = currentState.generateNextStates(currentState.parentMove[0])
			nextStates = random.sample(nextStates, len(nextStates))
			choice = None

			if nextStates == []:
				return None
			else:
				choice = nextStates[0]

			for state in nextStates:
				if checkState(state,visited):
					continue
				else:
					heuristicState = heuristicFunc(state)
					heuristicChoice = heuristicFunc(choice)
					if heuristicState <= heuristicChoice:
						choice = state

			if heuristicFunc(choice) <= heuristicFunc(currentState):
				stack += [choice]

	return None
	
def solveHeuristic(startState):
	return steepest_ascent_hill_climbing(startState)