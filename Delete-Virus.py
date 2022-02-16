from ast import For
import os
import time
from colorama import Fore, Style, init

############################## DELETE FILE ##############################

def deleteFiles(name):

    time.sleep(3)

    for i in os.listdir():
        if name in i and i != 'Delete-Virus.py':
            os.remove(i)
            print(Fore.LIGHTRED_EX + " File Deleted Successfully.\n" + Style.RESET_ALL)
            
    END()

############################## END ##############################

def END():
    print(Fore.RED + ' [1] ' + Style.RESET_ALL + 'Back to main\n' +
          Fore.LIGHTBLACK_EX + 'Press any key to exit...'
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
        Fore.RED + ' [6] ' + Style.RESET_ALL + 'Detele Custom Files\n' +
        Fore.RED + ' [7] ' + Style.RESET_ALL + 'Detele All Files\n\n' +
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
        pass
    elif answer == '6':
        pass
    elif answer == '7':
        pass
    else:
        pass

############################## BODY ##############################

main()