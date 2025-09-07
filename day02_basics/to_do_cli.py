
import json, os
tasks = []

FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file if it exists, else return empty list."""
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks list to JSON file."""
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


tasks = load_tasks()

while True:
    print("\n(1) add  (2) list  (3) done  (4) quit")
    action = input("Choose: ")

    if action == "1":
        t = input("New task: ")
        tasks.append({"title": t, "done": False})
        save_tasks(tasks)
        print("✅ added")

    elif action == "2":
        for i, t in enumerate(tasks, start=1):
            status = "✓" if t["done"] else " "
            print(f"{i}. [{status}] {t['title']}")

    elif action == "3":
        i = int(input("Task number done: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            save_tasks(tasks)
            print("👍 marked done")
        else:
            print("❗ invalid number")

    elif action == "4":
        print("bye!")
        break

    else:
        print("❗ invalid option")