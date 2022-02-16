from ast import For
from asyncio.windows_events import NULL
import os
import time
from colorama import Fore, Style, init
from datetime import datetime, timedelta

############################## DELETE ALL FILE ##############################

def deleteAll():
    
    os.system('cls')
    
    time.sleep(0.5)
    
    for i in os.listdir():
        if i != 'Delete-Virus.py' and i != '.git':
            os.remove(i)
            print(Fore.LIGHTRED_EX + "\n File Deleted Successfully.\n" + Style.RESET_ALL)
    END()

############################## DELETE FILE ##############################

def deleteFiles(name):

    if name == NULL:
        
        os.system('cls')
        
        print(Fore.WHITE + ' Enter your target ' + Fore.LIGHTBLACK_EX + '(like .txt) : ')
        custom = input(Fore.GREEN + ' >> ' + Style.RESET_ALL)
        
        if custom[0] == '.':
            time.sleep(2)
        
            for i in os.listdir():
                if custom in i and i != 'Delete-Virus.py':
                    os.remove(i)
                    print(Fore.LIGHTRED_EX + "\n File Deleted Successfully.\n" + Style.RESET_ALL)
                    
                    END()
        
            print(Fore.RED + '\n File doesn''t found. \n')
            
            END()
            
        else:
            print(Fore.RED + ' Format was wrong. Please try again...\n')
            
            print(Fore.LIGHTBLACK_EX + " Back to main in 5 seconds...")
            
            total_seconds = 5
            
            while total_seconds > 0:
                timer = timedelta(seconds = total_seconds)
                print(" " ,timer, end="\r")
                time.sleep(1)
                total_seconds -= 1
            main()
    
    else:
        
        os.system('cls')
        
        time.sleep(2)
        
        for i in os.listdir():
            if name in i and i != 'Delete-Virus.py':
                os.remove(i)
                print(Fore.LIGHTRED_EX + "\n File Deleted Successfully.\n" + Style.RESET_ALL)
        END()

############################## END ##############################

def END():
    print(Fore.RED + ' [1] ' + Style.RESET_ALL + 'Back to main\n\n' +
          Fore.LIGHTBLACK_EX + ' Press any key to exit...\n'
          )
    
    answer = input(Fore.GREEN + ' >> ' + Style.RESET_ALL)
    
    if answer == '1':
        main()
    else:
        pass

############################## MAIN ############################## 

def main():

    os.system('cls')
    
    print(
        Fore.RED + ' [1] ' + Style.RESET_ALL + 'Detele .txt Files\n' +
        Fore.RED + ' [2] ' + Style.RESET_ALL + 'Detele .mp4 Files\n' +
        Fore.RED + ' [3] ' + Style.RESET_ALL + 'Detele .mp3 Files\n' +
        Fore.RED + ' [4] ' + Style.RESET_ALL + 'Detele .pdf Files\n' +
        Fore.RED + ' [5] ' + Style.RESET_ALL + 'Detele Custom Files\n' +
        Fore.RED + ' [6] ' + Style.RESET_ALL + 'Detele All Files\n\n' +
        Fore.LIGHTBLACK_EX + " Press any key to exit...\n"
    )

    answer = input(Fore.GREEN + " >> " + Style.RESET_ALL)

    if answer == '1':
        deleteFiles('.txt')
    elif answer == '2':
        deleteFiles('.mp4')
    elif answer == '3':
        deleteFiles('.mp3')
    elif answer == '4':
        deleteFiles('.pdf')
    elif answer == '5':
        deleteFiles(name=NULL)
    elif answer == '6':
        deleteAll()
    else:
        pass

############################## BODY ##############################

main()