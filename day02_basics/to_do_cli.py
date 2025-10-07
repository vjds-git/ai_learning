from todo_utils import load_tasks, save_tasks, add_task, list_tasks, mark_done



def main():
    tasks = load_tasks()
    while True:
        print("\n(1) add  (2) list  (3) done  (4) quit")
        action = input("Choose: ")

        if action == "1":
            t = input("New task: ")
            add_task(tasks, t)
        elif action == "2":
            list_tasks(tasks)
        elif action == "3":
            i = int(input("Task number done: ")) - 1
            mark_done(tasks, i)
        elif action == "4":
            print("bye!")
            break
        else:
            print("❗ invalid option")


if __name__ == "__main__":
    main()
