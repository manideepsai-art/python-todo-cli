# Simple CLI Todo App - GSSoC '26 Track 2
tasks = []

def show_menu():
    print("\n📝 TODO CLI")
    print("1. Add task")
    print("2. View tasks") 
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Added!")

def view_tasks():
    if not tasks:
        print("No tasks!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⏳"
        print(f"{i}. {status} {task['task']}")

def remove_task():
    view_tasks()
    if tasks:
        idx = int(input("Remove task number: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("🗑️ Removed!")

while True:
    show_menu()
    choice = input("Choose (1-4): ")
    if choice == '1': add_task()
    elif choice == '2': view_tasks()
    elif choice == '3': remove_task()
    elif choice == '4': break
