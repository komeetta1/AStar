import numpy as np
from itertools import compress
import turtle
from Maze import maze2
from turtleGraphic import *
import time
import sys


ANY, UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3, 4

class Node:
  
    def __init__(self, parent=None, position=None, tulosuunta=UP):
        self.parent = parent
        self.position = position
        self.tulosuunta =  tulosuunta

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        if self.position == other.position and self.tulosuunta == other.tulosuunta:
            return True
        elif self.position == other.position and other.tulosuunta == ANY:
            return True
        else:
            return False
            

def kelaa(lista, n):
    tmp = lista.copy()
    i = 1
    while i<n:
        tmp = [tmp.pop(len(tmp)-1)] + tmp
        i=i+1
    
    return tmp

def select_moves(direction_constraints, tulosuunta):
    fil=direction_constraints.copy()
    moves  =  [[-1, 0], # ylös
             [ 0, 1 ], # oikealle
             [ 1, 0 ], # alas
             [ 0, -1]] # vasemmalle
    fil = kelaa(fil, tulosuunta) 
    return list(compress(moves, fil))

def tutki_tulosuunta(position):
    if position[0] == -1:
        return UP
    if position[1] == 1:
        return RIGHT
    if position[0] == 1:
        return DOWN
    if position[1] == -1:
        return LEFT

def search(maze, cost, start, end):
  
    start_node = Node(None, tuple(start))
    end_node = Node(None, tuple(end), ANY)

    yet_to_visit_list = []  
    visited_list = []
    crossroad = []
    visited_crossroad = []
    
    yet_to_visit_list.append(start_node)
    
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10

    nr_rows, nr_columns = np.shape(maze)
    
    
    while len(yet_to_visit_list) > 0:
        

        outer_iterations += 1    
        
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
            else:
                break
        
        if outer_iterations > max_iterations:
            print ("giving up on pathfinding too many iterations")
        
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        if current_node == end_node:
            crossroad.remove(start_node.position)
            
            return return_path(current_node,maze,crossroad)

        children = []
        children2 = []
        upAndDown = []
        
        tulosuunta = current_node.tulosuunta
        
        moves = select_moves([True, True, False, False], tulosuunta)    #Oikea
        #moves = select_moves([True, False, False, True], tulosuunta)    #Vasen
        #moves = select_moves([True, True, True, True], tulosuunta)      #Kaikki

        
        
        for new_position in moves: 

            tulosuunta = tutki_tulosuunta(new_position)
            
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            screen_x = -120 + (current_node.position[1]*24)
            screen_y = 120 - (current_node.position[0]*24)
            
            yellow.goto(screen_x, screen_y)
            yellow.stamp()
            #time.sleep(0.03)

            if (node_position[0] > (nr_rows - 1) or 
                node_position[0] < 0 or 
                node_position[1] > (nr_columns -1) or 
                node_position[1] < 0):
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position, tulosuunta)

            children.append(new_node)

        for new_position in [(-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                if (node_position[0] > (nr_rows - 1) or 
                    node_position[0] < 0 or 
                    node_position[1] > (nr_columns -1) or 
                    node_position[1] < 0):
                    continue
                if maze[node_position[0]][node_position[1]] != 0:
                    upAndDown.append(maze[node_position[0]][node_position[1]])
                    continue

        if len(upAndDown) == 1 and current_node.position not in visited_crossroad:
            crossroad.append(current_node.position)
            visited_crossroad.append(current_node.position)
        
        for new_position in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                if (node_position[0] > (nr_rows - 1) or 
                    node_position[0] < 0 or 
                    node_position[1] > (nr_columns -1) or 
                    node_position[1] < 0):
                    continue
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
                new_node = Node(current_node, node_position)
                children2.append(new_node)

        if len(children2) > 2 and current_node.position not in visited_crossroad:
            crossroad.append(current_node.position)
            visited_crossroad.append(current_node.position)

        for child in children:
            
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue
            
            child.g = current_node.g + cost
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + 
                       ((child.position[1] - end_node.position[1]) ** 2)) 
            child.f = child.g + child.h

            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            yet_to_visit_list.append(child)

def return_path(current_node,maze,crossroad):
    path = []
    path_suunta = []
    current = current_node
    nr_rows, nr_columns = np.shape(maze)
    result = [[-1 for i in range(nr_columns)] for j in range(nr_rows)]
    start_value = 0
    while current is not None:
        path.append(current.position)
        path_suunta.append(current.tulosuunta)
        current = current.parent
    path = path[::-1]
    path_suunta = path_suunta[::-1]
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    crossroad_list = list(set(path) & set(crossroad))
    for y in range(len(crossroad_list)):
                screen_x = -120 + (crossroad_list[y][1]*24)
                screen_y = 120 - (crossroad_list[y][0]*24)
                red.goto(screen_x, screen_y)
                red.stamp()
    suuntaPath(path_suunta, path, maze, current_node)
    return result


def suuntaPath(path_suunta, path, maze, current_node):
    for z in path:
        current_node.position = z
        print(current_node.position)
        for i in path_suunta:
            if i == 1:
                forward(path, maze, current_node)
                path_suunta.pop(0)
                break

            elif i == 2:
                right(path, maze, current_node)
                path_suunta.pop(0)
                break

            elif i == 3:
                down(path, maze, current_node)
                path_suunta.pop(0)
                break
            elif i == 4:
                left(path, maze, current_node)
                path_suunta.pop(0)
                break

def forward(path, maze, current_node):
    screen_x = -120 + (current_node.position[1]*24)
    screen_y = 120 - (current_node.position[0]*24)
    
    greenForward.goto(screen_x, screen_y)
    greenForward.stamp()
    
def right(path, maze, current_node):
    screen_x = -120 + (current_node.position[1]*24)
    screen_y = 120 - (current_node.position[0]*24)
    
    greenRight.goto(screen_x, screen_y)
    greenRight.stamp()

def down(path, maze, current_node):
    screen_x = -120 + (current_node.position[1]*24)
    screen_y = 120 - (current_node.position[0]*24)
    
    greenDown.goto(screen_x, screen_y)
    greenDown.stamp()

def left(path, maze, current_node):
    screen_x = -120 + (current_node.position[1]*24)
    screen_y = 120 - (current_node.position[0]*24)
    
    greenLeft.goto(screen_x, screen_y)
    greenLeft.stamp()


def main(maze2):

    start2 = [12, 11]
    end2 = [12, 3]
    #end2 = [3,11]


    cost = 1 # cost per movement

    path = search(maze2, cost, start2, end2)
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path]))


def setupMaze(maze2):
    for y in range(len(maze2)):
        for x in range(len(maze2[y])):
            character = maze2[y][x]
            screen_x = -120 + (x * 24)
            screen_y = 120 - (y * 24)

            if character == 1:
                maze.goto(screen_x, screen_y)
                maze.stamp() 
                walls.append((screen_x, screen_y))

            if character == 0:
                floor.goto(screen_x, screen_y)
                floor.stamp()
                walk.append((screen_x, screen_y))
                
maze = Maze()
walls =[]
floor = Floor()
walk = []
def endProgram():
    wn.exitonclick()
    sys.exit()
red = Red()
yellow = Yellow()
greenForward = GreenForward()
greenRight = GreenRight()
greenDown = GreenDown()
greenLeft = GreenLeft()


setupMaze(maze2)
main(maze2)
wn.exitonclick()


    