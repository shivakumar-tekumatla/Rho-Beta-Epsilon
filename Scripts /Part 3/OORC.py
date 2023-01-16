import numpy as np 
from collections import deque
class Robot:
    def __init__(self,robot_position=(0,0),robot_face="N") -> None:
        self.lin_speed = 1  #grid per sec 
        self.ang_speed = 1  #quarter turn per sec 
        self.robot_position = robot_position #by default starts at (0,0)
        self.max_x_cells = 20 
        self.max_y_cells = 20 
        self.time = 0 #keeping track of time in seconds 
        self.curr_order = "NWSE" #this is the rotation order for the robot in positive direction 
        self.robot_face = robot_face # North in the beginning 
        self.robot_face_ind = {"N":(0,1), #increase the y ind 
                                "S":(0,-1), #decrease the y ind 
                                "E":(1,0), #Increase the x ind 
                                "W":(-1,0) #decrease the x ind
                                } # based on the face of the robot , do the corresponding index increment 
        pass 
    def drive(self,num_cells)->str:
        prev_position = self.robot_position #storing the previous position before doing any operation 
        def is_goal_walkable(goal):
            x, y = goal 
            if x in range(0,self.max_x_cells+1) and y in range(0,self.max_y_cells+1): #checking if goal is walkable
                return True 
            else:
                self.turn(1) # turning one positive quarter turn . Positive is counter clockwise 
                return False
        i =0 
        while i < int(num_cells):
            x_mul,y_mul = self.robot_face_ind[self.robot_face]
            x_ind,y_ind =  self.robot_position
            goal = (x_ind+x_mul,y_ind+y_mul)
            if is_goal_walkable(goal):
                self.robot_position = goal
                i+=1
                self.time += (1/self.lin_speed)
        return f"Time: {self.time} sec Position: {self.robot_position} Heading: {self.robot_face} Last Action: Drove {prev_position} -> {self.robot_position}"

    def turn(self,num_quarter_rotations)->str:
        num_quarter_rotations = int(num_quarter_rotations)
        def wrapto2(n):
            #Wrapping to 2 
            q = n//2 
            r = n%2 
            if r==0:
                if q%2 ==0:
                    return 0  
                else:
                    return 2
            else:
                return int(pow((-1)*r,q))
        prev_robot_face = self.curr_order[0] #storing the prev facing direction 
        n = wrapto2(num_quarter_rotations)
        items   = deque(self.curr_order) 
        items.rotate(-n) #rotating the string  to find the robot facing direction 
        self.curr_order = "".join(items)
        # print(self.curr_order)
        self.robot_face = self.curr_order[0] #get the robot facing direction 
        self.time += (abs(n)/self.ang_speed)
        return f"Time: {self.time} sec Position: {self.robot_position} Heading: {self.robot_face} Last Action: Turned {prev_robot_face} -> {self.robot_face}"
    def stop(self)->str:
        self.time+=1 # staying in the place for one second 
        return f"Time: {self.time} sec Position: {self.robot_position} Heading: {self.robot_face} Last Action: Stopped at {self.robot_position}"
    def eStop(self)->str:
        return f"Time: {self.time} sec Position: {self.robot_position} Heading: {self.robot_face} Last Action: Shutting Down" 
 
    def setLinSpeed(self,grid_per_sec)->str:
        self.prev_lin_speed = self.lin_speed
        self.lin_speed = grid_per_sec
        return f"Time: {self.time} sec Position: {self.robot_position} Heading: {self.robot_face} Last Action: Set the Lin speed {self.prev_lin_speed} -> {self.lin_speed}" 
    def setAngSpeed(self,quarter_turn_per_sec)->str:
        self.prev_ang_speed = self.ang_speed 
        self.ang_speed = quarter_turn_per_sec
        return f"Time: {self.time} sec Position: {self.robot_position} Heading: {self.robot_face} Last Action: Set the Ang speed {self.prev_ang_speed} -> {self.ang_speed}" 
         
    def ultraSound(self,reading):
        if reading < 1:
            return self.turn(1) #turning one turn when the UL value is less than 1 
        return None  