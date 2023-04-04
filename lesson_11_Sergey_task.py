# Реализовать To Do список используя классы.
# В задаче хранить описание и приоритет (high, medium, low, по умолчанию low).
# Методы класса ToDoList:
# - добавить задачу
# - изменить описание задачи
# - изменить приоритет задачи
# - удалить задачу
# - вернуть список задач, отсортированный по приоритету (сначала высокий)
# - сохранить список в файл/загрузить из файла


from enum import IntEnum
import csv


class PriorityEnum(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Task:
    def __init__(self, name_task: str, task: str, priority: PriorityEnum):
        self.name_task = name_task
        self.task = task
        self.priority = priority

    def __repr__(self):
        return f'Task({self.name_task}, {self.task}, {self.priority.name})'


class ToDoList:

    file_name = 'task.csv'

    def __init__(self):
        self.to_do_list: list[Task] = []

    def add_list(self, task: Task):
        self.to_do_list.append(task)

    def edit_task(self, task: Task, new_task: str):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].task = new_task

    def edit_priority(self, task: Task, new_prior: PriorityEnum):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].priority = new_prior

    def del_task(self, task: Task):
        if task in self.to_do_list:
            self.to_do_list.remove(task)

    def get_list(self) -> list[Task]:
        return sorted(self.to_do_list, key=lambda task: task.priority, reverse=True)

    def save_file(self):
        with open(self.file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name_task', 'task', 'priority'])
            result = [[element.name_task, element.task, element.priority.value] for element in self.to_do_list]
            writer.writerows(result)

    def load_file(self):
        with open(self.file_name) as file:
            csv_reader = csv.reader(file)
            for i, (name, task, priority) in enumerate(csv_reader):
                if i == 0:
                    continue
                self.to_do_list.append(Task(name, task, PriorityEnum(int(priority))))


task = Task('first', 'first task', PriorityEnum.LOW)
task2 = Task('first2', 'first task', PriorityEnum.MEDIUM)
task3 = Task('first3', 'first task', PriorityEnum.HIGH)
task4 = Task('first4', 'first task', PriorityEnum.LOW)

to_do_list = ToDoList()
to_do_list.load_file()
to_do_list.get_list()
to_do_list.add_list(task)
to_do_list.add_list(task2)
to_do_list.add_list(task3)
to_do_list.add_list(task4)

print(to_do_list.get_list())
print(to_do_list.to_do_list)

to_do_list.edit_task(task3, 'edit task')
print(to_do_list.get_list())

to_do_list.del_task(task4)
print(to_do_list.get_list())

to_do_list.edit_priority(task, PriorityEnum.HIGH)
print(to_do_list.get_list())


to_do_list.save_file()
