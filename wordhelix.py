#Python code which writes a verticle, multicolor helix of an input word on the screen at input framerate until the user presses
#a button which kills the process. 
#NOTE: Purely a "cool thing" kind a program. Serves no practical purpose.

from colorama import * #Grabbed from pip
import sys
import signal
import os
import subprocess
import threading
import time

#update every value so that way we give the illusion of progress
#TODO: Make more compatable with Windows versions after and before 10
#TODO: Make work on linux

def updateSine(array):
    for index, value in enumerate(array):
        if value[0] > 7:
           array[index][0] = 7
           array[index][1] = True
           
        elif value[0] < 0:
            array[index][0]= 0
            array[index][1] = False
        else:
            if array[index][1] == False:
                array[index][0] = array[index][0] + 1
            else:
                array[index][0] = array[index][0] - 1



def endProg(parentProcess):
    input()
    subprocess.run("cls", shell = True)
    subprocess.run("cls", shell = True)
    print(Style.RESET_ALL)
    os.kill(parentProcess,signal.SIGILL)
    
    
    


#------Main process------

init(autoreset=True)#Fix bug where it keeps color changes into the next print, also might have increase performance
pPhase = input("Please a phrase for your helix: ")
framerate = input("Please input a framerate (in seconds).\n(It can be a decimal greater than 0.01): ")
try:
    framerate = float(framerate)

except ValueError:
    print(Fore.RED + "ERROR: Input framerate is not a decimal!")
    sys.exit(1)

if framerate <= 0:
    print(Fore.RED + "ERROR: Input framerate is less then or equal to 0!")
    sys.exit(1)
elif not framerate >= 0.01:
    print(Fore.RED + "ERROR: Input framerate is not greater than 0.001!")
    sys.exit(1)

#TODO: Update code so that it is better compatible with linux
subprocess.run("cls", shell = True)
subprocess.run("mode 77, 49", shell = True)

current_pid = os.getpid()
input_thread = threading.Thread(target=endProg, args=[current_pid])
input_thread.start()

seq = [[0,False], [1,False], [2,False], [3,False], [4,False], [5,False],[6,False]]

while True:
    try:
        for ele in seq:
            #Set the color of the back of the Helix
            if ele[1] is True:
                colorBack = Back.WHITE
            else:
                colorBack = Back.BLACK

            #Color of the actual text
            match ele[0]:
                case 0:
                    print(Fore.RED + colorBack +"\t" + pPhase)
                    
                case 1:
                    print(Fore.GREEN + colorBack + "\t\t" + pPhase)

                case 2: 
                    print(Fore.YELLOW + colorBack + "\t\t\t" + pPhase)
                    
                case 3:
                    print(Fore.CYAN + colorBack + "\t\t\t\t" + pPhase)

                case 4:
                    print(Fore.YELLOW + colorBack + "\t\t\t\t\t" + pPhase)

                case 5:
                    print(Fore.GREEN + colorBack + "\t\t\t\t\t\t" + pPhase)  

                case 6:
                    print(Fore.RED + colorBack +"\t\t\t\t\t\t\t" + pPhase) 
        
        
        nextPrint = time.time() + framerate
        whenNextPrint = nextPrint - time.time()
        time.sleep(whenNextPrint)    
  
        updateSine(seq)
    except KeyboardInterrupt:

        print(Fore.RED + Back.BLACK + "\nMAIN TASK ENDED BY KEYBOARD INPUT!\n PLEASE PRESS ENTER TO RETURN TO COMMAND LINE...")
        sys.exit(1)
    

    