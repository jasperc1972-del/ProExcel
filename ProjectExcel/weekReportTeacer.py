import json
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title, project="General", priority="Medium"):
    tasks = load_tasks()
    task = {
        "title": title,
        "project": project,
        "priority": priority,
        "status": "TODO",
        "created": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ 任務已新增：{title}")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        print(f"{i+1}. [{task['status']}] {task['title']} ({task['project']}, {task['priority']})")

def complete_task(index):
    tasks = load_tasks()
    tasks[index]["status"] = "DONE"
    save_tasks(tasks)
    print(f"🎉 任務完成：{tasks[index]['title']}")

# 範例操作
add_task("設計新模組架構", project="Backend", priority="High")
add_task("撰寫週報", project="Management", priority="Low")
list_tasks()
complete_task(0)