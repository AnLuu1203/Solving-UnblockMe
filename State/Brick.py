#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Brick:
  #id: mã khối gạch
  #isVetical: dọc (True) hay ngang (False)
  #position: vị trí viên gạch trong Board
  #length: chiều dài gạch


  def __init__(self, id, isVetical, position, length):
    self.id = id
    self.isVetical = isVetical
    self.position = position
    self.length = length

  #@param:
  #board: kiểu Board
  #@return: list các bước di chuyển hợp lệ (id, move), vd: [(1,-1), (1,2), (1,1)]
  def generateNextMoves(self, board):
    listMove = []

    if self.isVetical:
      #chiều dọc

      #to the top
      i = self.position[0] - 1
      while i >= 0:
        if board[i][self.position[1]] == 0:
          listMove += [(self.id, i - self.position[0])]
        else:
          break;
        i -= 1

      #to the bottom
      i = self.position[0] + self.length
      while i <= 5:
        if board[i][self.position[1]] == 0:
          listMove += [(self.id, i - (self.length - 1) - self.position[0])]
        else:
          break;
        i += 1;
    else:
      #chiều ngang

      # to the left
      i = self.position[1] - 1
      while i >= 0:
        if board[self.position[0]][i] == 0:
          #print(i)
          listMove += [(self.id, i - self.position[1])]
        else:
          break
        i-=1

      #to the right
      i = self.position[1] + self.length
      while i <= 5:
        if board[self.position[0]][i] == 0:
          listMove += [(self.id, i - (self.length - 1) - self.position[1])]
        else:
          break
        i+=1

    return listMove





