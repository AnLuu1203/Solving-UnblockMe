#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
import sys
from pygame.locals import *
from Testcase import *
from Brick_GUI import *

from Algorithm.DepthFirstSearch import *
from Algorithm.BreathFirstSearch import *
from Algorithm.HeuristicSearch import *

clock = pygame.time.Clock()
height = 572
width = 400
unit = int ((322 - 2) / 6)



def create_GUI(board,sprites_list,unit):
    brick_list = []
    i = 0
    for brick in board.listBrick:
        tmp = Brick_GUI(brick,unit)
        brick_list.append(tmp)
        sprites_list.add(tmp)
        i += 1
    return brick_list

spritesList = pygame.sprite.Group()
spritesList2 = pygame.sprite.Group()
dfs = pygame.sprite.Sprite()
bfs = pygame.sprite.Sprite()
hill = pygame.sprite.Sprite()
run = pygame.sprite.Sprite()
nextBoard = pygame.sprite.Sprite()
preBoard = pygame.sprite.Sprite()
nextMove = pygame.sprite.Sprite()
backMove = pygame.sprite.Sprite()
autoMove = pygame.sprite.Sprite()
modeMove = pygame.sprite.Sprite()
refresh = pygame.sprite.Sprite()

def button_init():

    #BUTTON CHUYỂN NETX BOARD
    nextBoard_image = pygame.image.load('image/btnRight.png')
    nextBoard.image = nextBoard_image
    nextBoard.rect = nextBoard.image.get_rect()
    nextBoard.rect.topleft = [230,80]
    spritesList2.add(nextBoard)

    #BUTTON CHUYỂN PREVIOUS BOARD
    preBoard_image = pygame.image.load('image/btnLeft.png')
    preBoard.image = preBoard_image
    preBoard.rect = preBoard.image.get_rect()
    preBoard.rect.topleft = [50,80]
    spritesList2.add(preBoard)

    #BUTTON CHỌN DFS
    dfs_image = pygame.image.load('image/btnDFS.png')
    dfs.image = dfs_image
    dfs.rect = dfs.image.get_rect()
    dfs.rect.topleft = [12,510]
    spritesList2.add(dfs)

    #BUTTON CHỌN BFS
    bfs_image = pygame.image.load('image/btnBFS.png')
    bfs.image = bfs_image
    bfs.rect = bfs.image.get_rect()
    bfs.rect.topleft = [100,510]
    spritesList2.add(bfs)

    #BUTTON CHỌN HILL CLIMBING
    hill_image = pygame.image.load('image/btnHS.png')
    hill.image = hill_image
    hill.rect = hill.image.get_rect()
    hill.rect.topleft = [185,510]
    spritesList2.add(hill)

    #BUTTON CHẠY GIẢI THUẬT
    run_image = pygame.image.load('image/btnRUN.png')
    run.image = run_image
    run.rect = run.image.get_rect()
    run.rect.topleft = [270,510]
    spritesList2.add(run)

    #BUTTON NEXT MOVE
    nextMove_image = pygame.image.load('image/btnNEXT.png')
    nextMove.image = nextMove_image
    nextMove.rect = nextMove.image.get_rect()
    nextMove.rect.topleft = [520,510]
    spritesList2.add(nextMove)

    #BUTTON BACK MOVE
    backMove_image = pygame.image.load('image/btnPREV.png')
    backMove.image = backMove_image
    backMove.rect = backMove.image.get_rect()
    backMove.rect.topleft = [370,510]
    spritesList2.add(backMove)

    #BUTTON CHẠY AUTO MOVE
    autoMove_image = pygame.image.load('image/btnAUTO.png')
    autoMove.image = autoMove_image
    autoMove.rect = autoMove.image.get_rect()
    autoMove.rect.topleft = [445,450]
    spritesList2.add(autoMove)

    #BUTTON CHUYỂN CHẾ ĐỘ MOVE
    modeMove_image = pygame.Surface([100,50])
    modeMove.image = modeMove_image
    modeMove.rect = modeMove.image.get_rect()
    modeMove.rect.topleft = [430,300]
    spritesList2.add(modeMove)

    #BTN REFRESH
    refresh_image = pygame.image.load('image/btnRefresh.png')
    refresh.image = refresh_image
    refresh.rect = refresh.image.get_rect()
    refresh.rect.topleft = [450,495]
    spritesList2.add(refresh)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((width + 200,height))
    pygame.display.set_caption('Unblock me')
    background = pygame.image.load('image/background.png')

    button_init()

    #LEVEL
    font_level = pygame.font.Font(None,40)
    font_color = (255,255,255)
    level = 0
    #GIẢI THUẬT ĐƯỢC LỰA CHỌN
    mode = pygame.font.Font(None,23)
    mode_value = 'Depth first search'
    setMode = 1
    #THỜI GIAN GIẢI THUẬT
    timeRun = pygame.font.Font(None,30)
    time_value = 0
    #CHẾ ĐỘ DI CHUYỂN : AUTO - TAY
    modeMove_text = pygame.font.Font(None,20)
    modeMove_auto = True
    #SỐ BƯỚC DI CHUYỂN
    moveCount = pygame.font.Font(None,30)
    moveCount_value = 0
    tmp = '0'

    # CÁC BIỂN ĐỂ KIỂM TRA CHẾ ĐỘ CHẠY, ĐANG DI CHUYỂN ĐỂ MƯỢT, MÃ BRICK ĐANG MOVE,KIỂM TRA BẮT ĐẦU DI CHUYỂN
    running = True
    moving = True
    id = 0
    first = True

    # CHẾ ĐỘ DEMO
    demo = False
    auto = False
    moveNext = False
    moveBack = False

    # TỐC ĐỘ DI CHUYỂN
    fast = 2
    limit = float(unit/fast)

    listBoard = testcase()
    board = listBoard[level]
    board.printBoard()
    brick_list = create_GUI(board,spritesList,int(unit))
    l = 0
    i = 0

    while running :
        screen.fill((108,54,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if dfs.rect.collidepoint(pos):
                    mode_value = 'Depth first search'
                    setMode = 1
                elif bfs.rect.collidepoint(pos):
                    mode_value = 'Breath first search'
                    setMode = 2
                elif hill.rect.collidepoint(pos):
                    mode_value = 'Heuristic search'
                    setMode  = 3
                elif nextBoard.rect.collidepoint(pos):
                    level += 1
                    if level == 10:
                        level = 0
                    board = listBoard[level]
                    mode_value = 'Depth first search'
                    setMode = 1
                    demo  = False
                    modeMove_auto = True
                    time_value = 0
                    moveCount_value = 0
                    lst = []
                    spritesList = pygame.sprite.Group()
                    brick_list = create_GUI(board,spritesList,int(unit))

                elif preBoard.rect.collidepoint(pos):
                    level -= 1
                    if level == -1:
                        level = 9
                    board = listBoard[level]
                    mode_value = 'Depth first search'
                    setMode = 1
                    demo = False
                    moveCount_value = 0
                    time_value = 0
                    lst = []
                    spritesList = pygame.sprite.Group()
                    brick_list = create_GUI(board,spritesList,int(unit))
                elif run.rect.collidepoint(pos):
                    move_display = moveCount.render('Solving . . .',True,font_color)
                    move_rect = move_display.get_rect()
                    move_rect.centerx,move_rect.centery = [300,286]
                    screen.blit(move_display,move_rect)
                    pygame.display.flip()

                    if setMode == 1:
                        print('Running ... ')
                        start_time = time.time()
                        lst = solveDFS(board)
                        time_value = round(time.time() - start_time,5)
                    elif setMode == 2:
                        print('Running ... ')
                        start_time = time.time()
                        lst = solveBFS(board)
                        time_value = round(time.time() - start_time,5)

                    elif setMode == 3:
                        print('Running ... ')
                        start_time = time.time()
                        lst = solveHeuristic(board)
                        time_value = round(time.time() - start_time,5)
                        print(lst)

                    if lst == None:
                        moveCount_value = -1
                    else:
                        lst = lst.getResultMove(lst)
                        print(lst)
                        l = len(lst)
                        moveCount_value = l
                        i = -1
                        print('Done',l)

                elif modeMove.rect.collidepoint(pos):
                    modeMove_auto = not(modeMove_auto)
                    '''
                    if i == l: continue
                    else:
                        if modeMove_auto: i = 0
                        else: i = -1
                    '''
                elif autoMove.rect.collidepoint(pos):
                    if modeMove_auto:
                        auto = True
                        moveNext = False
                        moveBack = False
                        demo = True
                        if i == -1: i = 0
                        print(i,l)
                elif nextMove.rect.collidepoint(pos):
                    if not(modeMove_auto):
                        demo = True
                        moveNext = True
                        print(l,i)
                        if i < l and moveBack == False: i += 1
                        #if i == -1: i+= 1
                        moveBack = False
                        moving = True
                        first = True
                        auto = False
                elif backMove.rect.collidepoint(pos):
                    if not(modeMove_auto):
                        demo = True
                        moveBack = True
                        auto = False
                        if i >= 0 and i < l and moveNext: i+= 1
                        if i >= 0: i -= 1
                        moveNext = False
                        moving = True
                        first = True
                elif refresh.rect.collidepoint(pos):
                    demo = False
                    modeMove_auto = True
                    board = listBoard[level]
                    spritesList = pygame.sprite.Group()
                    brick_list = create_GUI(board,spritesList,int(unit))
                    i = -1
                    lst = []
                    l = len(lst)
                    moveCount_value = 0
                    time_value = 0


        '''
        if i < l:
            id = lst[i][0] - 1
            moves = lst[i][1]
            if board.listBrick[id].isVetical:
                brick_list[id].moveVertical(moves, 1)
            else:
                brick_list[id].moveHorizontal(moves, 1)

            i += 1
            #clock.tick(1)
            '''

        if i < l and i >= 0 and demo == True:
            id = lst[i][0] - 1
            if moveBack:
                move = -lst[i][1]
            else: move = lst[i][1]

            if moving == True:
                if board.listBrick[id].isVetical:
                    if first:
                        limity = brick_list[id].rect.topleft[1] + move*unit
                        first = False
                    if move < 0:
                        if brick_list[id].rect.topleft[1] > limity + limit:
                            brick_list[id].rect.y -= limit
                        else:
                            brick_list[id].rect.y = limity
                            moving = False
                    else:
                        if brick_list[id].rect.topleft[1] < limity - limit:
                            brick_list[id].rect.y += limit
                        else:
                            brick_list[id].rect.y = limity
                            moving =False
                else:
                    if first:
                        limitx = brick_list[id].rect.topleft[0] + move*unit
                        first = False
                    if move < 0:
                        if brick_list[id].rect.topleft[0] > limitx + limit:
                            brick_list[id].rect.x -= limit
                        else:
                            brick_list[id].rect.x = limitx
                            moving = False
                    else:
                        if brick_list[id].rect.topleft[0] < limitx - limit:
                            brick_list[id].rect.x += limit
                        else:
                            brick_list[id].rect.x = limitx
                            moving = False
            else:
                if auto:
                    i += 1
                    moving = True
                    first = True



        screen.blit(pygame.transform.scale(background,(345,572)),(0,0))
        spritesList.draw(screen)
        spritesList2.draw(screen)

        #LEVEL
        lv = font_level.render(str(level + 1),True,font_color)
        lv_rect = lv.get_rect()
        lv_rect.centerx, lv_rect.centery = 170,95
        screen.blit(lv,lv_rect)
        #algorithm
        m = mode.render(mode_value,True,font_color)
        m_rect = m.get_rect()
        m_rect.centerx,m_rect.centery = 170,130
        screen.blit(m,m_rect)

        #Timer
        t = timeRun.render('Time: ' + str(time_value),True,font_color)
        t_rect = t.get_rect()
        t_rect.topleft = [430,100]
        screen.blit(t,t_rect)

        #Mode move
        if modeMove_auto:
            mMove = modeMove_text.render('Auto',True,font_color)
        else: mMove = modeMove_text.render('Hand',True,font_color)
        mMove_rect = mMove.get_rect()
        mMove_rect.centerx,mMove_rect.centery = (480,325)
        screen.blit(mMove,mMove_rect)

        # SỐ BƯỚC MOVE
        if moveCount_value == -1:
            move_display = moveCount.render('No solution',True,font_color)
        else:
            move_display = moveCount.render('Moves: ' + str(moveCount_value),True,font_color)
        move_rect = move_display.get_rect()
        move_rect.topleft = [430,150]
        screen.blit(move_display,move_rect)

        pygame.display.flip()
        clock.tick(60)


    pygame.quit()
