class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Ошибка: Неверный индекс задачи.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"Задача {index + 1}: {task}")

manager = TaskManager()

manager.add_task("Сделать уборку", "2024-10-25")
manager.add_task("Отправить посылку", "2024-10-28")

print("Все задачи:")
manager.display_tasks()

manager.mark_task_as_completed(1)

print("\nНевыполненные задачи:")
for task in manager.get_pending_tasks():
    print(task)