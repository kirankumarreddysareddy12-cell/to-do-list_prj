# To-Do List Project (No File Storage)

tasks = []  # List to store tasks

def add_task():
    """Add a new task to the list"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(f"✅ Task '{task}' added successfully!")
    else:
        print("❌ Task cannot be empty.")

def view_tasks():
    """View all tasks"""
    if not tasks:
        print("\nNo tasks added yet.\n")
        return
    print("\n=== To-Do List ===")
    for i, t in enumerate(tasks, 1):
        status = "✔️ Done" if t["done"] else "❌ Not Done"
        print(f"{i}. {t['task']} [{status}]")
    print()

def mark_done():
    """Mark a task as completed"""
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print(f"🎉 Task '{tasks[idx-1]['task']}' marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

def delete_task():
    """Delete a task from the list"""
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"🗑️ Task '{removed['task']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

def main():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye! Stay productive.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
