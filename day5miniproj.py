
# welcome = """ Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit"""
# print(welcome)

# response = input(""" Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit""")

# if response == "1":
#     print("We're adding a task")


incomplete_task = []
completed_task = []

def adding_task(incomplete):
    task = input("Type out a daily task. ")
    if task not in incomplete:
        incomplete.append(task)
        print(incomplete_task)
    else:
        print("You already added that task!")


def view_task(incomplete, complete):
    task = input("Which set of task would you like to view. 1. incomplete 2. complete ")
    if task == "1":
        for task in incomplete:
            print(task)
    elif task == "2":
        for task in complete:
            print(task)
    else:
        print("Please enter a valid response 1 or 2.")


# for the user mark complete- move the incomplete task to completed task
def mark_task(incomplete, complete):
    task = input("Which task have you completed? ")
    try:
        incomplete.remove(task)
    except:
        print("You still have time to complete it!")
    else:
        complete.append(task)

# deleting or removing task from list
def delete_task(incomplete, complete):
    list_choice = input("Which list would you like to delete task from, 1. incomplete 2. complete? ")
    if list_choice == "1":
        deleted = input("Which task would you like to remove? ")
        try:
            incomplete.remove(deleted)
        except:
            print("That task is not found in that list ")
    elif list_choice == "2":
        deleted = input("Which task would you like to remove? ")
        try:
            complete.remove(deleted)
        except:
            print("That task is not found in that list ")
    else:
        print("Invalid entry")
    
        # if deleted in incomplete:
        #     incomplete.remove(deleted)
        # elif deleted in complete:
        #     complete.remove(deleted)
        # else:
        #     print("Couldn't find in the list")




def run(incomplete, complete):
    while True:
        response = input(""" Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
        Please choose from the menu above.""")
        if response == "1":
            adding_task(incomplete)
        elif response == "2":
            view_task(incomplete, complete)
        elif response == "3":
            mark_task(incomplete, complete)
        elif response == "4":
            delete_task(incomplete, complete)
        elif response == "5":
            break
run(incomplete_task, completed_task)


#def view_tasks(incomplete, complete):

