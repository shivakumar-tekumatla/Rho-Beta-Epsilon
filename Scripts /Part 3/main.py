from OORC import Robot
import numpy as np  
import re 
import os 

def read_instructions():
    with open("instructions.txt","r") as file:
        instructions = file.readlines()
    return instructions

def separate_command(command):
    #separated the command to abstract the float and string 
    # for some commands there is no float 
    try:
        num = [float(s) for s in re.findall(r'-?\d+\.?\d*', command)]
        return command.split(str(num[0])[0])[0], num[0]  #string,flt
    except:
        return command,None

def write_log(log):
    #write log data to log.txt 
    with open("log.txt","a") as file:
        file.write(log+"\n")

def main():
    robot = Robot(robot_position=(0,0),robot_face = "N") #assuming that the robot is starting at (0,0) facing north(positive y axis)
    commands = {"D":robot.drive,
                "T":robot.turn,
                "S":robot.stop,
                "ES":robot.eStop,
                "SS":robot.setLinSpeed,
                "ST":robot.setAngSpeed,
                "UL":robot.ultraSound} # Functions will be called based on this mapping
    instructions = list(map(lambda x:x.strip(),read_instructions())) #reading the instructions and stripping the unnecessary "\n"
    #delete the log file if there is one already 
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    #write the first log 
    write_log(f"Time: {0} sec Position: {robot.robot_position} Heading: {robot.robot_face} Last Action: Start")
    for ins in instructions: #reading each command 
        # print(robot.robot_face)
        cmd,flt = separate_command(ins)  # separating the command 
        # print(cmd,flt)
        if flt:
            log = commands[cmd](flt)
        else:
            log = commands[cmd]()
        if log:
            write_log(log) #writing the log data to the logfile 

if __name__ == "__main__":
    main()