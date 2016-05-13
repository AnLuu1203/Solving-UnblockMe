import copy
from State.Brick import *

class Board:
	#listBrick: danh các khối gạch

	def __init__(self, listBrick, parentState = None, parentMove = (0,0), depth = 0):
		self.listBrick = listBrick
		self.parentState = parentState
		self.parentMove = parentMove
		self.depth = depth

	#khởi tạo mảng trống
	def initBoard(self):
		board = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
		return board

	#@param:
	#id: id của khối gạch
	#return: vẽ các khối gạch trong mảng, trừ khối gạch có id truyền vào
	#note: vẽ tất cả khối gạch, truyền id = 0
	def createBoard(self, id):
		board = self.initBoard()

		for brick in self.listBrick:
			if brick.id != id:
				if brick.isVetical:
					x = brick.position[0]
					y = brick.position[1]

					for i in range(0,brick.length):
						board[x + i][y] = brick.id
				else:
					x = brick.position[0]
					y = brick.position[1]

					for i in range(0,brick.length):
						board[x][y + i] = brick.id

		return board

	#in mảng ra console
	def printBoard(self):
		for row in self.createBoard(0):
			print(row)


	#sinh ra list các bước di chuyển hợp lệ, trừ khối gạch có id truyền vào
	def generateNextMoves(self, id):
		listMove = []

		for brick in self.listBrick:
			if brick.id != id:
				board = self.createBoard(brick.id)
				moves = brick.generateNextMoves(board)
				listMove += moves

		return listMove

	#sinh ra các trạng thái từ các bước di chuyển hợp lệ
	def generateNextStates(self, previousId):
		listState = []
		for move in self.generateNextMoves(previousId):
			listState += [self.generateState(move)]
		return listState


	def printState(self):
		lst = self.generateNextState()
		for state in lst:
			for brick in state:
				print(brick.id, brick.isVetical, brick.position, brick.length)
			print("\n")

	#kiểm tra goal
	def checkGoal(self):
		board = self.createBoard(0)
		i = 5
		while (board[2][i] != 1):
			if board[2][i] != 0:
				return False
			i -= 1
		return True

	#@param: 
	#move: bước di chuyển
	#@return: trạng thái được sinh ra từ move
	def generateState(self, move):
		lst = copy.deepcopy(self.listBrick)
		for i in range(len(lst)):
			brick = lst[i]
			if brick.id == move[0]:
				if brick.isVetical == True:
					lst[i] = Brick(brick.id, brick.isVetical, (brick.position[0] + move[1],brick.position[1]), brick.length)
				else:
					lst[i] = Brick(brick.id, brick.isVetical, (brick.position[0],brick.position[1] + move[1]), brick.length)
				break
		return Board(lst,self,move,self.depth + 1)

	#return danh sách các bước di chuyển
	def getResultMove(self, board):
		if board.parentMove == (0,0):
			return []
		else:
			result = self.getResultMove(board.parentState)
			return result + [board.parentMove]

	def findBrickById(self,id):
		for brick in self.listBrick:
			if brick.id == id:
				return brick
		return None
