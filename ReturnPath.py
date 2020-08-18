from turtleGraphic import GreenDown, GreenRight, GreenLeft, GreenForward

def suuntaPath(path_suunta, path, maze, current_node):
    for z in path:
        current_node.position = z
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


greenForward = GreenForward()
greenRight = GreenRight()
greenDown = GreenDown()
greenLeft = GreenLeft()




