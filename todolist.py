import PySimpleGUI as sg
import json

sg.theme('Python')  # define o tema personalizado

# verifica se o arquivo já existe, se sim, lê as tarefas salvas
try:
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

layout = [
    [sg.Text("Tarefa:"), sg.InputText()],
    [sg.Button("Adicionar Tarefa", button_color=('black', '#ffd43b')),
     sg.Button("Remover Tarefa", button_color=('white', '#0073cf')),
     sg.Button("^", button_color=('black', '#ffd43b')),
     sg.Button("v", button_color=('white', '#0073cf'))],
    [sg.Listbox(values=tasks, size=(40, 10), key='listbox')]
]

window = sg.Window("Todolist", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Adicionar Tarefa":
        task = values[0]
        tasks.append(task)
        window.Element('listbox').Update(values=tasks)
    elif event == "Remover Tarefa":
        try:
            task = values['listbox'][0]
            tasks.remove(task)
            window.Element('listbox').Update(values=tasks)
        except:
            pass
    elif event == "^":
        try:
            idx = window['listbox'].get_indexes()[0]
            tasks[idx], tasks[idx-1] = tasks[idx-1], tasks[idx]
            selected_task = window['listbox'].get()[0]
            window.Element('listbox').Update(values=tasks)
            window['listbox'].set_value(selected_task)
        except:
            pass
    elif event == "v":
        try:
            idx = window['listbox'].get_indexes()[0]
            tasks[idx], tasks[idx+1] = tasks[idx+1], tasks[idx]
            selected_task = window['listbox'].get()[0]
            window.Element('listbox').Update(values=tasks)
            window['listbox'].set_value(selected_task)
        except:
            pass

# salva as tarefas em um arquivo .json
with open('tasks.json', 'w') as f:
    json.dump(tasks, f)

window.close()
