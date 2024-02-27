import app1_functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("task.txt"):
    with open("task.txt", 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text('', key='clock')
label = sg.Text("Type a task")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add", size=10, key="Add")
listbox = sg.Listbox(values=app1_functions.get_work(), key="tasks",
                     enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", key="Edit")
complete_button = sg.Button("Complete", key="Complete")
exit_Button = sg.Button("Exit", key="Exit")

# for icons:
# add_button = sg.Button(size=2, image_source="add.png", tooltip="Add Task", key="Add")
# edit_button = sg.Button(image_source="edit.png", tooltip="Edit Task", key="Edit")
# exit_Button = sg.Button(image_source="exit.png", tooltip="Exit", key="Exit")
# complete_button = sg.Button(image_source="complete.png", tooltip="Complete Task", key="Complete")

window = sg.Window('My Task App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [listbox, edit_button, complete_button],
                           [exit_Button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d %Y, %H:%M:%S"))
    match event:
        case "Add":
            tasks = app1_functions.get_work()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            app1_functions.write_work(tasks)
            window['tasks'].update(values=tasks)
        case "Edit":
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task'] + "\n"

                tasks = app1_functions.get_work()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                app1_functions.write_work(tasks)
                window['tasks'].update(values=tasks)
            except IndexError:
                sg.popup("Please select the value first!", font=("Times New Roman", 20))
        case "Complete":
            try:
                task_to_complete = values['tasks'][0]
                tasks = app1_functions.get_work()
                tasks.remove(task_to_complete)
                app1_functions.write_work(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value='')
            except IndexError:
                sg.popup("Please select the value first!", font=("Times New Roman", 20))
        case "Exit":
            break
        case 'tasks':
            window['task'].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break

window.close()