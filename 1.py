def list_tasks(tasks, sort_by=None):
    if not tasks:
        print("当前没有任务")
        return

    display_list = tasks.copy()
    if sort_by == "priority":
        display_list.sort( key=lambda t: t.get("priority", 999))
    elif sort_by == "due":
        display_list.sort( key=lambda t: t.get("due", "9999-999-99"))
    elif sort_by == "status":
        display_list.sort( key=lambda t: (t["done"], t.get("priority", 999)))

    print(" \n待办事项：")
    for i, task in enumerate(display_list, 1):
        status = " ture " if task["done"] else "flase"
        prio = task.get("priority", "-")
        due = task.get("due", "-")
        print(f"{i}. [{status}]  {task['content']}")
        print(f"  id: {task['id']}   优先级: {prio}   截止: {due}")
    print()