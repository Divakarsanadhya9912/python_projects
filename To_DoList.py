def h():
    tasks = []

    while True:
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark Task as Done")
        print("4. Exit")

        ch = int(input("Enter your choice:"))

        if ch == 1:
            n_task = int(input("how many task do you want to add:"))

            for i in range(n_task):
                task = input("Enter the task:")
                tasks.append({"task":task,"done":False})
                print("Task added!")

        elif ch == 2:
            print("\nTask")
            for index,task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index+1}. {task['task']} - {status}")

        elif ch == 3:
            task_index = int(input("Enter the task no. to mark as done: ")) - 1
            if len(tasks) > task_index >= 0  :
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task no.")

        elif ch == 4:
            print("Exiting the to-do list.")
            break

        else:
            print("Invalid choice. try again.")

h()