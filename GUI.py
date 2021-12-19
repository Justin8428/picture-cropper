import PySimpleGUI as sg
from CLIcore import App

#sg.theme('BluePurple')

layout = [[sg.Text('Batch Picture Cropper', font=('Helvetica', 24))],
          [sg.Text('Folder containing original images'), sg.Input(key="InputFolder"), sg.FolderBrowse()],
          [sg.Text('Folder to store Cropped Images'), sg.Input(key="OutputFolder"), sg.FolderBrowse()],
          [sg.Text('_'  * 100, size=(65, 1))],
          [sg.Text('Flags', font=('Helvetica', 15), justification='left')],
          [sg.Text('Filetype to convert', size=(15, 1)), sg.Drop(values=('.jpg', '.png'), auto_size_text=True, key = "FileType")],
          [sg.Text('Desired aspect ratio', size=(15, 1)), sg.In(default_text='16:9', size=(10, 1), key = "AspectRatio")],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Batch Picture Cropper', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        # run App with specified parameters
        arparams = values['AspectRatio'].split(":")
        desired_aspect_ratio = int(arparams[0])/int(arparams[1])

        App(folder = values['InputFolder'], dumpto = values['OutputFolder'], filetype = values['FileType'], desired_aspect_ratio = desired_aspect_ratio, cosmetic_aspect_ratio = values['AspectRatio'])
        #print(values['InputFolder'], values['OutputFolder'], values['FileType'], desired_aspect_ratio)
window.close()