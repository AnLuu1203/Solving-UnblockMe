from State.Board import *
from State.Brick import *

def testcase1():
  test1 = Brick(1,False,(2,1),2)
  test2 = Brick(2,True,(1,0),2)
  test3 = Brick(3,True,(1,3),2)
  test4 = Brick(4,True,(1,4),3)
  test5 = Brick(5,True,(1,5),2)
  test6 = Brick(6,False,(3,0),2)
  test7 = Brick(7,False,(3,2),2)
  test8 = Brick(8,True,(4,1),2)
  test9 = Brick(9,True,(4,2),2)
  test10 = Brick(10,False,(4,3),3)
  test11 = Brick(11,False,(5,3),2)
  lst = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11]
  return Board(lst)

def testcase2():
  b1 = Brick(1,False,(2,0),2)
  b2 = Brick(2,False,(0,0),3)
  b3 = Brick(3,True,(0,5),3)
  b4 = Brick(4,True,(1,2),3)
  b5 = Brick(5,True,(3,0),2)
  b6 = Brick(6,False,(3,4),2)
  b7 = Brick(7,False,(5,0),3)
  b8 = Brick(8,True,(4,4),2)
  lst = [b1,b2,b3,b4,b5,b6,b7,b8]
  return Board(lst)

def testcase3():
  b1 = Brick(1,False,(2,0),2)
  b2 = Brick(2,True,(1,2),2)
  b3 = Brick(3,True,(1,3),3)
  b4 = Brick(4,True,(1,4),3)
  b5 = Brick(5,False,(3,0),2)
  b6 = Brick(6,True,(3,2),2)
  b7 = Brick(7,True,(4,1),2)
  b8 = Brick(8,False,(5,2),2)
  lst = [b1,b2,b3,b4,b5,b6,b7,b8]
  return Board(lst)

def testcase4():
  b1 = Brick(1,False,(2,0),2)
  b2 = Brick(2,True,(1,2),2)
  b3 = Brick(3,True,(1,3),3)
  b4 = Brick(4,True,(1,4),3)
  b5 = Brick(5,False,(3,0),2)
  b6 = Brick(6,True,(1,5),3)
  lst = [b1,b2,b3,b4,b5,b6]
  return Board(lst)

def testcase5():
  test1 = Brick(1,False,(2,0),2)
  test2 = Brick(2,True,(0,2),3)
  test3 = Brick(3,True,(0,3),2)
  test4 = Brick(4,False,(1,4),2)
  test5 = Brick(5,True,(2,4),2)
  test6 = Brick(6,True,(2,5),2)
  test7 = Brick(7,True,(3,0),3)
  test8 = Brick(8,True,(3,1),2)
  test9 = Brick(9,False,(5,1),2)
  test10 = Brick(10,False,(4,2),3)
  test11 = Brick(11,True,(4,5),2)
  lst = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11]
  return Board(lst)

def testcase6():
  test1 = Brick(1, False, (2,2), 2)
  test2 = Brick(2, True, (0,0), 2)
  test3 = Brick(3, False, (0,1), 2)
  test4 = Brick(4, True, (0,3), 2)
  test5 = Brick(5, False, (0,4), 2)
  test6 = Brick(6, True, (2,0), 2)
  test7 = Brick(7, True, (1,1), 3)
  test8 = Brick(8, True, (1,4), 2)
  test9 = Brick(9, True, (3,2), 2)
  test10 = Brick(10, False, (3,4), 2)
  test11 = Brick(11, False, (4,3), 2)
  test12 = Brick(12, False, (5,0), 3)
  test13 = Brick(13, True, (4,5), 2)
  listBrick = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12,test13]

  return Board(listBrick)

def testcase7():
  test1 = Brick(1, False, (2,2), 2)
  test2 = Brick(2, False, (0,0), 3)
  test3 = Brick(3, True, (1,0), 3)
  test4 = Brick(4, True, (0,4), 3)
  test5 = Brick(5, True, (0,5), 3)
  test6 = Brick(6, False, (5,0), 3)
  test7 = Brick(7, True, (3,2), 2)
  test8 = Brick(8, True, (3,3), 3)
  test9 = Brick(9, False, (4,4), 2)

  listBrick = [test1,test2,test3,test4,test5,test6,test7,test8,test9]

  return Board(listBrick)

def testcase8():
  listBrick = []

  listBrick.append(Brick(1, False, (2,1), 2))
  listBrick.append(Brick(2, True, (1,0), 2))
  listBrick.append(Brick(3, True, (3,0), 2))
  listBrick.append(Brick(4, True, (0,1), 2))
  listBrick.append(Brick(5, False, (0,2), 2))
  listBrick.append(Brick(6, False, (1,2), 2))
  listBrick.append(Brick(7, True, (0,4), 3))
  listBrick.append(Brick(8, True, (2,3), 2))
  listBrick.append(Brick(9, True, (3,2), 2))
  listBrick.append(Brick(10, False, (5,2), 2))
  listBrick.append(Brick(11, False, (4,3), 2))
  listBrick.append(Brick(12, False, (3,4), 2))
  listBrick.append(Brick(13, True, (4,5), 2))

  return Board(listBrick)

def testcase9():
  listBrick = []

  listBrick.append(Brick(1, False, (2,1), 2))
  listBrick.append(Brick(2, True, (0,0), 3))
  listBrick.append(Brick(3, False, (0,2),3))
  listBrick.append(Brick(4, False, (1,1), 2))
  listBrick.append(Brick(5, True, (1,4), 3))
  listBrick.append(Brick(6, True, (1,5), 3))
  listBrick.append(Brick(7, False, (3,0), 3))
  listBrick.append(Brick(8, True, (4,2), 2))
  listBrick.append(Brick(9, False, (4,3), 3))
  listBrick.append(Brick(10, False, (5,3), 3))

  return Board(listBrick)

def testcase10():
  listBrick = []

  listBrick.append(Brick(1, False, (2,1), 2))
  listBrick.append(Brick(2, True, (0,0), 3))
  listBrick.append(Brick(3, True, (1,3), 2))
  listBrick.append(Brick(4, True, (1,4), 3))
  listBrick.append(Brick(5, True, (3,3), 2))
  listBrick.append(Brick(6, False, (3,0), 3))
  listBrick.append(Brick(7, True, (4,2), 2))
  listBrick.append(Brick(8, False, (5,0), 2))
  listBrick.append(Brick(9, False, (5,3), 2))

  return Board(listBrick)




def testcase():
  test = []
  test.append(testcase1())
  test.append(testcase2())
  test.append(testcase3())
  test.append(testcase4())
  test.append(testcase5())
  test.append(testcase6())
  test.append(testcase7())
  test.append(testcase8())
  test.append(testcase9())
  test.append(testcase10())

  return test