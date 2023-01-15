from OORC import Robot
import numpy as np  
import re 

def read_instructions():
    with open("instructions.txt","r") as file:
        instructions = file.readlines()
    return instructions

def separate_command(command):
    try:
        num = [float(s) for s in re.findall(r'-?\d+\.?\d*', command)]
        return command.split(str(num[0])[0])[0], num[0]  #string,flt
    except:
        return command,None

def main():
    #first create a grid of all the cells
    max_x_cells = 20 
    max_y_cells = 20 
    x = np.arange(0,max_x_cells+1,1)
    y = np.arange(0,max_y_cells+1,1)
    xc,yc = np.meshgrid(x, y)

if __name__ == "__main__":
    
    robot = Robot()
    commands = {"D":robot.drive,
                "T":robot.turn,
                "S":robot.stop,
                "ES":robot.eStop,
                "SS":robot.setLinSpeed,
                "ST":robot.setAngSpeed,
                "UL":robot.ultraSound}
    instructions = list(map(lambda x:x.strip(),read_instructions())) #reading the instructions and stripping the unnecessary "\n"
    start = (0,0) # starting cell 
    robot_face = "N" #This variable keeps track of the robot facing direction based on the rotation . N- North , E- East , S- South , W - West 
    """
    with open("log.txt","w") as log:
        log.write("Time: 0 Sec Position: (0,0) Heading: N Last Action: Start")
    """
    for ins in instructions:
        print(robot.robot_face)
        cmd,flt = separate_command(ins)
        # print(cmd,flt)
        if flt:
            print(commands[cmd](flt))
        else:
            print(commands[cmd]())

        
