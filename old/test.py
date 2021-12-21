import PySimpleGUI as sg
#import signal

# layout the window
layout = [[sg.Text('Progress: '), sg.Text(key="ProgressPercent")],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar'), sg.Text(key="DoneNotification")],
          [sg.Output(size=(80, 20))],
          [sg.Cancel()]]

# create the window
window = sg.Window('Progress', layout)
progress_bar = window['progressbar']

# loop that would normally do something useful
num_files = 100
ongoingops = True
while True:
    if ongoingops:
        for i in range(num_files):
            # check to see if the cancel button was clicked and exit loop if clicked
            event, values = window.read(timeout=10)
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                window.close()
            # update bar with loop value +1 so that bar eventually reaches the maximum
            progress_bar.UpdateBar(i + 1)
            window["ProgressPercent"].update(f"{i}% ({i} of {num_files} files)")
            print(i)
            if i + 1 >= num_files:
                ongoingops = False
                window["DoneNotification"].update("Done. You can now close this window.")
                print("Done. You can now close this window.")
                break
    else: # leave window up once task is done
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
window.close()
