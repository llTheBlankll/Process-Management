import subprocess
import psutil
import time
import prettytable
import os

list_of_blocked_processes: psutil.Process = []
blocking_started: bool = False


def clear():
    if os.name == 'nt':
        subprocess.Popen("cls", shell=True).communicate()
    else:
        print("\033c", endline="")


def isNumber(value):
    return any(char.isdigit() for char in value)


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
    for proc in psutil.process_iter():
        ptable.add_row([proc.pid, proc.name()])
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
        # If the entered input contains number then it can be called as PID of the program. 
        # If not, then it is a process name of the program not the PID.
        if isNumber(process_name):
            process_name = int(process_name)
            for proc in psutil.process_iter():
                if process_name == proc.pid:
                    print(f"Process {proc.name()} with the PID of {proc.pid} is blocked successfully.")
                    list_of_blocked_processes.append(proc)
                    time.sleep(2)
                    # * Go back to Main menu
                    main()
        else:
            process_name = str(process_name)
            for proc in psutil.process_iter():
                if process_name == str(proc.name()):
                    print(f"Process {proc.name()} is blocked successfully.")
                    list_of_blocked_processes.append(proc)
                    time.sleep(2)
                    # * Go back to Main menu
                    main()
        # * If no process was found, the program won't go to main menu, see the code above. 
        # * So we will raise an alert to say that no program was found and ask the user again for what the program to block.
        print(f"Process {process_name} was not found.")
        time.sleep(2)
        addProcess()


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
