from todo_utils import load_tasks, save_tasks, add_task, list_tasks, mark_done


import logging

logging.basicConfig(
    filename="todo.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

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

        if action == "1":
            try:
                t = input("New task: ")
                add_task(tasks, t)
                logging.info(f"Added new task: {t}")
            except Exception as e:
                logging.exception(f"Error adding task: {e}")

        elif action == "3":
            try:
                i = int(input("Task number done: ")) - 1
                mark_done(tasks, i)
                logging.info(f"Marked task #{i+1} done")
            except Exception as e:
                logging.exception(f"Error marking done: {e}")

if __name__ == "__main__":
    main()
