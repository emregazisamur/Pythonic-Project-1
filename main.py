oncomingTasks = []
completedTasks = []
delayedTasks = []

#Controlling the date
def date_controller(date):
    dateParts = date.split(".") #Date is DD.MM.YYYY . We splitted it to 3 parts as DD MM and YYYY
    if len(dateParts) != 3: #We are checking the date if it has 3 parts or not.
        return False
    if len(dateParts[0]) != 2 or len(dateParts[1]) != 2 or len(dateParts[2]) != 4: #We are checking the date if its parts has the true length.
        return False
    if not dateParts[0].isdigit() or not dateParts[1].isdigit() or not dateParts[2].isdigit(): #We are checking the parts of the date if it consists of only digits.
        return False

    day=int(dateParts[0])
    month=int(dateParts[1])
    year=int(dateParts[2])

    if year < 1 or month < 1 or month > 12 or day < 1:
        return False

    if month==2:
        if year%400 == 0 or (year%4==0 and year %100 !=0):
            max_day = 29
        else:
            max_day = 28
    elif month == 4 or month == 6  or month == 9 or month == 11:
        max_day = 30
    else:
        max_day = 31

    if day > max_day:
        return False
    
    return True
        
#Comparing todays date with task date.
def date_comparator(todaysDate,taskDate):
        part1 = todaysDate.split(".")
        part2 = taskDate.split(".")

        for i in range(3):
            n1 = int(part1[i])
            n2 = int(part2[i])

            if n1<n2: return -1
            if n2<n1: return 1

        return 0
        
#Loading informations from file.
FILE_NAME = "study_organizer_data.txt"
def load_tasks_from_file(filename=FILE_NAME):
     
     with open(filename, "r") as file:
        for line in file:
            taskParts = line.strip().split(",")

            if len(taskParts)>=5:
                taskStatus = taskParts[0]
                task = {"taskName": taskParts[1],
                        "courseName": taskParts[2],
                        "topic": taskParts[3],
                        "lastDate": taskParts[4]
                        }
                if taskParts[0] == "oncoming":
                    oncomingTasks.append(task)
                elif taskStatus == "completed":
                    completedTasks.append(task)
                elif taskStatus == "delayed":
                    delayedTasks.append(task)

        
                
#Saving informations to file.
def save_tasks_to_file(filename=FILE_NAME):
    with open(filename, "w") as file:
        for status, task_list in [
            ("oncoming", oncomingTasks),
            ("completed", completedTasks),
            ("delayed", delayedTasks)
        ]:
            for task in task_list:
                file.write(
                    f"{status},{task['taskName']},{task['courseName']},"
                    f"{task['topic']},{task['lastDate']}\n"
                )

    print("[Info] Tasks successfully saved to file.")
            




#Deletes the delayed task from oncomingTasks list, then adds it to the delayedTasks list.
def check_delayedTasks():
    i = 0
    while i < len(oncomingTasks):
        task = oncomingTasks[i]

        if date_comparator(task["lastDate"],todaysDate) == -1: #If todays date is later than the task date, then task is delayed.
            task[4] = "delayed"

            delayedTasks.append(task)
            oncomingTasks.remove(task)
        else:
            i += 1
    save_tasks_to_file()



#Adding tasks to file.
def add_task():
    print("\nAdd New Task")
    task_name = input("Task name: ").strip()
    course_name = input("Course name: ").strip()
    topic = input("Topic: ").strip()

    if not task_name or not course_name or not topic:
        print("Please fill in all fields.")
        return

    if any("," in value for value in (task_name, course_name, topic)):
        print("Please do not use commas in task information.")
        return

    for task_list in (oncomingTasks, delayedTasks, completedTasks):
     for task in task_list:
         if task["taskName"].lower() == task_name.lower():
             print("A task with this name already exists.")
             return
            
    while True:
        date = input("Enter the last date (DD.MM.YYYY): ")

        if date_controller(date):
            break

        print("Invalid date! Example: 20.10.2026")

    if date_comparator(date, todaysDate) == -1:
        status = "delayed"
    else:
        status = "oncoming"
        


    task = {
        "taskName": task_name,
        "courseName": course_name,
        "topic": topic,
        "lastDate": date
    }

    if status == "delayed":
        delayedTasks.append(task)
    else:
        oncomingTasks.append(task)
    save_tasks_to_file()
    print("Task added.")






#Printing the selected list to terminal.
def show_selected_list(list):
    if len(list) == 0:
        print("There are no tasks in this list.")
        return

    for task in list:
        print("\nTask Name:", task["taskName"])
        print("Course:", task["courseName"])
        print("Topic:", task["topic"])
        print("Last Date:", task["lastDate"])





#Completing the tasks.
def complete_task():
    if not oncomingTasks and not delayedTasks:
        print("There are no tasks to complete.")
        return
 
    task_name = input("Enter the task name to complete: ").strip()

    for task_list in (oncomingTasks, delayedTasks):
        for task in task_list:
            if task["taskName"].lower() == task_name.lower():
                task_list.remove(task)
                completedTasks.append(task)
                save_tasks_to_file()
                print("Task completed.")
                return

    print("Task not found in upcoming or delayed tasks.")
 







#Initialization of the script.
while True:
    todaysDate = input("Enter today's date (DD.MM.YYYY): ")

    if date_controller(todaysDate):
        break
    print("Invalid date. Please enter a valid date.")

load_tasks_from_file()
check_delayedTasks()



#Main Menu
while True:

    print("\n----------------Pythonic Study Organizer----------------")
    print("1. Add a New Task")
    print("2. Show Completed Tasks")
    print("3. Show Oncoming Tasks")
    print("4. Show Delayed Tasks")
    print("5. Complete a Task")
    print("0. Finish")

    selection = input("What would you like to do? (0-5) ")

    if selection == "1":
        add_task()
    elif selection == "2":
        show_selected_list(completedTasks)
    elif selection == "3":
        show_selected_list(oncomingTasks)
    elif selection == "4":
        show_selected_list(delayedTasks)
    elif selection == "5":
        complete_task()
    elif selection == "0":
        save_tasks_to_file()
        
        break
    else:
        print("Invalid Selection.")

    

    
