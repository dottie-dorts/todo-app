from tabulate import tabulate

todos = [{'id': 1, 'todo': 'Peep', 'done': False}, {'id': 2, 'todo': 'sit', 'done': True}]


def addTodo():
    new_todo = input('Enter new todo: ')
    id = len(todos) + 1
    todos.append({'id': id, 'todo': new_todo, 'done': False})

def removeTodo():
    id = input('Enter the id of the to do to remove: ')
    index = int(id) - 1
    todos.pop(index)

def display_todos():
    headers = [x.capitalize() for x in todos[1].keys()]
    rows =  [x.values() for x in todos]
    print(tabulate(rows, headers=headers))

def toggle_todo():
    id = input('Enter the id of the todo you wish to toggle: ')
    index = int(id) - 1
    todo = todos[index]
    value = todo['done']
    if value == False:
        todo['done'] = True
    else:
        todo['done'] = False

def update_todo():
     id = input('Enter the id of the todo you wish to update:  ')
     index = int(id) - 1
     todo = todos[index]
     new_todo = input('Enter the updated to-do: ')
     todo['todo'] = new_todo

while True:
    request = input('Enter command(Type h for help): ')

    if(request == 'h'):
        help_text = """
            h: help menu,
            a: add todo,
            r: remove todo,
            d: display todos,
            c: close application,
            t: toggle completed, 
            u: update todo
        """
        print(help_text)

    elif request == 'a':
        addTodo()
        display_todos()
    elif request == 'r':
        removeTodo()
        display_todos()   
    elif request == 'd':
        display_todos()
    elif request == 'c':
        break
    elif request == 't':
        toggle_todo()
        display_todos() 
    elif request == 'u':
        update_todo()
        display_todos()
    else:
        print('Invalid choice. Try again')
