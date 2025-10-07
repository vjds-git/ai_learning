import json
import os
from datetime import datetime

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    tasks.append({
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done_at": None
    })
    save_tasks(tasks)


def list_tasks(tasks):
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']} (created: {t.get('created_at', 'N/A')})")
        if t.get("done_at"):
            print(f"    ✔ done at {t.get('done_at')}")


def mark_done(tasks, i):
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        tasks[i]["done_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tasks(tasks)
    else:
        print("❗ invalid number")