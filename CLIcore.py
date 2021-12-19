# CLI version

from PIL import Image
import os
import argparse
import PySimpleGUI as sg


""" # params to modify
folder = "./bob"
dumpto = f"{folder}/new"
filetype = ".jpg"
desired_aspect_ratio = 4/3 # landscape only supported for now """
# output folder needs to exist first before running script...
# example Windows usage py CLIcore.py -i "./bob" -o "./test" -t ".jpg" -r "16:9"

# "one giant App function" so that it can be imported into GUI frontend without hacks
def App(folder, dumpto, filetype, desired_aspect_ratio, cosmetic_aspect_ratio = "RATIO"):
    
    # find all the files
    picture_files = [f for f in os.listdir(folder) if (os.path.isfile(os.path.join(folder, f)) and f.endswith(filetype))] # get only files in subfolder with ending .jpg (for eg)
    num_files = len(picture_files) # define the number of files

    ## window logic
    # layout the window
    layout = [[sg.Text('Progress: '), sg.Text(key="ProgressPercent")],
          [sg.ProgressBar(num_files, orientation='h', size=(20, 20), key='progressbar'), sg.Text(key="DoneNotification")],
          [sg.Output(size=(80, 20))],
          [sg.Cancel()]]
    # create window
    window = sg.Window('Progress', layout)
    progress_bar = window['progressbar']


    ## core logic

    if desired_aspect_ratio > 1: # landscape only

        ongoingops = True # flag to check if something is being done
        while True:
            if ongoingops:
                for i, picture in enumerate(picture_files):
                    
                    # check to see if the cancel button was clicked and exit loop/window if clicked
                    event, values = window.read(timeout=10)
                    if event == 'Cancel' or event == sg.WIN_CLOSED:
                        ongoingops = False
                        print("Operation cancelled, you can exit the App now")
                        break



                    ################################## 
                    # part that does the cropping -- maybe we can refactor this bit out
                    picdir = f"{folder}/{picture}" # kludgy but it will do for now
                    im = Image.open(picdir)
                    width, height = im.size

                    # check to see if it is already in target aspect ratio, no need to crop otherwise
                    if desired_aspect_ratio == width/height:
                        print(f"{picture} already in {cosmetic_aspect_ratio}, skipping...")
                        im1 = im
                    else:
                        if desired_aspect_ratio > width/height: # if the new aspect ratio is "narrower" than the old one, e.g. from 4:3 to 16:9. Yes I know this only works for landscape pictures
                            # calculate new bounds
                            new_height = width*(1/(desired_aspect_ratio))

                            top = (height - new_height)/2
                            bottom = height - top
                            left = 0
                            right = width
                        else: # otherwise new aspect ratio must be wider and crop left and right off
                        # calculate new bounds
                            new_width = height*(desired_aspect_ratio)

                            top = 0
                            bottom = height
                            left = (width - new_width)/2
                            right = width - left

                        # after new bounds have been calculated
                        print(f"Cropping {picture} to {cosmetic_aspect_ratio}")
                        im1 = im.crop((left, top, right, bottom)) # crop 
                    # im1.show() # show image
                    im1.save(f"{dumpto}/{picture}")
                    
                    ##################################### end cropping routine, back to GUI programming








                    # update bar with loop value +1 so that bar eventually reaches the maximum
                    progress_bar.UpdateBar(i + 1)
                    percent_round = round(((i+1)/num_files)*100,1)
                    window["ProgressPercent"].update(f"{percent_round}% ({i+1} of {num_files} files)")

                    # once ops are done break the loop
                    if i + 1 >= num_files:
                        ongoingops = False
                        window["DoneNotification"].update("Done. You can now close this window.")
                        print("Done. You can now close this window.")
                        break

            else: # leave window up once task is done -- technically here we can change the text...
                event, values = window.read(timeout=10)
                if event == 'Cancel' or event == sg.WIN_CLOSED:
                    break   
        window.close()

    else:
        print("Only landscape is supported at this time.")


if __name__ == "__main__":
    # argument parser
    parser = argparse.ArgumentParser(description='Script to auto crop and centre a bunch of pictures to given aspect ratio')
    parser.add_argument('-i', '--folder', type=str, help = "Folder with input pics, provide in format './folder")
    parser.add_argument('-o', '--output', type=str, help = "Folder to store cropped pics, provide in format './folder")
    parser.add_argument('-t', '--type', type=str, default=".jpg", help = "Type of pictures to crop, either .jpg or .png")
    parser.add_argument('-r', '--aspect_ratio', type=str, default="16:9", help = "Desired aspect ratio, default 16:9. Provide in format 16:9")

    args = parser.parse_args() # parse argument

    # parse the stupid user input
    folder = args.folder
    dumpto = args.output
    filetype = args.type
    arparams = args.aspect_ratio.split(":")
    desired_aspect_ratio = int(arparams[0])/int(arparams[1])
    cosmetic_aspect_ratio = args.aspect_ratio

    # run App
    App(folder, dumpto, filetype, desired_aspect_ratio)
