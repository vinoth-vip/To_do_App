import app1_functions
import PySimpleGUI as sg


label = sg.Text("Type a task")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add")
listbox = sg.Listbox(values=app1_functions.get_work(), key="tasks",
                     enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My Task App',
                   layout=[[label], [input_box, add_button], [listbox, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = app1_functions.get_work()
            new_task = values['task']
            tasks.append(new_task)
            app1_functions.write_work(tasks)
            window['tasks'].update(values=tasks)
        case "Edit":
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = app1_functions.get_work()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            app1_functions.write_work(tasks)
            window['tasks'].update(values=tasks)
        case 'tasks':
            window['task'].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break

window.close()