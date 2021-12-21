import PySimpleGUI as sg
from CLIcore import App
from iconfix import icon_crop_ico

def main():
    layout = [[sg.Text('Batch Picture Cropper', font=('Helvetica', 24))],
            [sg.Text('Folder containing original images'), sg.Input(key="InputFolder"), sg.FolderBrowse()],
            [sg.Text('Folder to store Cropped Images'), sg.Input(key="OutputFolder"), sg.FolderBrowse()],
            [sg.Text('_'  * 100, size=(65, 1))],
            [sg.Text('Options', font=('Helvetica', 15), justification='left')],
            [sg.Text('Filetype to convert', size=(15, 1)), sg.Drop(values=('.jpg', '.png'), auto_size_text=True, key = "FileType")],
            [sg.Text('Desired aspect ratio', size=(15, 1)), sg.In(default_text='16:9', size=(10, 1), key = "AspectRatio"), sg.Text('Provide in format 16:9')],
            [sg.Button('Start'), sg.Button('Exit'), sg.Button('About')]]

    window = sg.Window('Batch Picture Cropper', layout, icon=icon_crop_ico)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'About':
            about() # launch about() function 
        if event == 'Start':
            # run App with specified parameters
            arparams = values['AspectRatio'].split(":")
            desired_aspect_ratio = int(arparams[0])/int(arparams[1])

            App(folder = values['InputFolder'], dumpto = values['OutputFolder'], filetype = values['FileType'], desired_aspect_ratio = desired_aspect_ratio, cosmetic_aspect_ratio = values['AspectRatio'])
            #print(values['InputFolder'], values['OutputFolder'], values['FileType'], desired_aspect_ratio)
    window.close()

def about(): # window containing credits etc
    layout = [[sg.Text("About Batch Picture Cropper Frontend", font=('Helvetica', 12))],
              [sg.Text("v0.9.3-beta")],
              [sg.Text("An App to batch crop pictures in a folder to a specified aspect ratio.")],
              [sg.Text("Author: Justin8428")],
              [sg.Text("https://github.com/Justin8428/picture-cropper")],
              [sg.Button("Close")]]
    window = sg.Window("About", layout, icon=icon_crop_ico)
    choice = None
    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            break
        
    window.close()

if __name__ == "__main__":
    #sg.theme('BluePurple')
    main()