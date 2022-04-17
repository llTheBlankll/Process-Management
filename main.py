from turtle import title
from xmlrpc.client import boolean
import psutil
import time
import prettytable
import os

list_of_blocked_processes: psutil.Process = []
blocking_started: bool = False


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear()
    print("Options:")
    print("1. Add process to block")
    print("2. Clear all blocked processes")
    print("3. Start Blocking")
    print("4. Stop Blocking")
    print("5. List of blocked processes")
    try:
        val = int(input("-> "))
        if val == 1:
            addProcess()
        elif val == 2:
            clearAllBlockedProcesses()
        elif val == 3:
            startBlocking()
        elif val == 4:
            stopBlocking()
        elif val == 5:
            listAllBlockedProcesses()
        else:
            print(f"Invalid input number {val}")
            time.sleep(2)
            main()
    except ValueError:
        print("Only numbers are allowed.")
        time.sleep(2)
        main()


def addProcess():
    print("You can type 'back' to go back to the main menu.")
    
    # * Print the running processes in the system through the use of prettytable module.
    ptable = prettytable.PrettyTable(field_names=["PID", "Process Name"], title="Process List")
    for proc in psutil.process_iter:
        ptable.add_row([proc.pid(), proc.name()])
    print(ptable)
    
    # Ask the user to pick from the process above.
    process_name = input("Enter process name (e.g: chrome.exe): ")
    if process_name == "":
        print("Process name cannot be empty.")
        time.sleep(2)
        main()
    elif process_name == "back":
        main()
    else:
        list_of_blocked_processes.append(process_name)
        print(f"Process {process_name} blocked successfully.")
        time.sleep(2)
        main()


def clearAllBlockedProcesses():
    list_of_blocked_processes.clear()
    print("Processes cleared successfully.")
    time.sleep(2)
    main()


def listAllBlockedProcesses():
    pass
    
    


def startBlocking():
    if len(list_of_blocked_processes) == 0:
        print("Please specify a blocked processes.")
        time.sleep(2)
        main()
    
    


if __name__ == "__main__":
    main()
