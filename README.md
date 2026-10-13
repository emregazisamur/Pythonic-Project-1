About the Project

Pythonic Study Organizer is a command-line application developed in Python to help students organize their study tasks. Users can add tasks, view tasks according to their status, complete or delete tasks, and sort tasks by their deadlines.
The program stores task information in a text file, allowing tasks to be saved and loaded between program runs.

Features

Add New Tasks: Create tasks by entering a task name, course name, topic, and deadline.

View Tasks: Display completed, oncoming, and delayed tasks separately.

Complete Tasks: Move tasks from the oncoming or delayed list to the completed list.

Delete Tasks: Remove tasks after confirming the deletion.

Deadline Management: Automatically classify tasks as oncoming or delayed according to their deadlines.

Sort Tasks: Sort all task lists by deadline, starting with the nearest date.

Data Persistence: Save tasks to a text file and load them when the program starts.

Input Validation: Check date validity, prevent empty fields, and avoid duplicate task names.

How the Program Works

1. Task Lists
The program uses three lists to organize tasks according to their status:

oncomingTasks: Stores tasks that have not passed their deadlines.

completedTasks: Stores tasks that have been completed.

delayedTasks: Stores tasks whose deadlines have passed and that have not been completed.

Each task is represented by a Python dictionary containing four fields:

taskName: The name of the task.

courseName: The course associated with the task.

topic: The topic to study.

lastDate: The task's deadline in DD.MM.YYYY format.

2. Date Validation — date_controller()
This function checks whether an entered date is valid. It verifies the date format, checks that the day and month are within valid ranges, and accounts for leap years when determining the number of days in February.

3. Date Comparison — date_comparator()
This function compares two dates by checking the year, month, and day in that order. It returns -1 if the first date is earlier, 1 if it is later, and 0 if both dates are equal.

4. Loading Tasks — load_tasks_from_file()
This function reads saved task information from study_organizer_data.txt. It separates each line into its individual fields and places each task into the appropriate list according to its saved status.

5. Saving Tasks — save_tasks_to_file()
This function writes all tasks and their statuses to the text file. It is called after important changes to keep the saved data up to date.

6. Checking Delayed Tasks — check_delayedTasks()
This function compares task deadlines with the current date. Tasks with past deadlines are moved from the oncoming list to the delayed list. If a delayed task's deadline is today or in the future, it is moved back to the oncoming list. The updated lists are then saved.

7. Adding Tasks — add_task()
This function collects task information from the user. It checks for empty fields and duplicate task names, validates the deadline, and adds the task to either the oncoming or delayed list, depending on its deadline.

8. Displaying Tasks — show_selected_list()
This function displays the details of every task in the selected list. If the list is empty, it displays an appropriate message.

9. Completing Tasks — complete_task()
This function searches for a task by name in the oncoming and delayed lists. When a match is found, the task is removed from its current list and added to the completed list.

10. Sorting Tasks — date_key() and sort_tasks_by_date()
The date_key() function converts a date into a tuple containing the year, month, and day. This allows Python to compare dates in chronological order.
The sort_tasks_by_date() function uses this key to sort all three task lists from the earliest deadline to the latest and saves the updated order.

11. Deleting Tasks — delete_task()
This function searches for a task by name across all three lists. Before deleting a matching task, it asks the user for confirmation. If the user confirms, the task is removed and the changes are saved.

How to Run

Run the program using a terminal:

python study_organizer.py

Enter today's date in DD.MM.YYYY format when prompted.

Use the numbered menu to manage your study tasks.

The program creates or updates study_organizer_data.txt to store task information.
