# picture-cropper
An App to batch crop pictures in a folder to a specified aspect ratio.

Currently only landscape pictures are supported. (The App should not drastically fail with portrait picutres but results are less than ideal...)

Tested on Windows 10. Windows .exe binaries are avaiable, click on the "Releases" pane on the side of the page.

## Why? Aren't there tons of these apps already...?

 - There didn't seem to be many standalone apps that just do image cropping to an aspect ratio (usually they're part of multi GB very large image manipulation programs, which is great but I just needed something fast)
 - Needed to automate 16:9 cropping in the centre for a very large number of files (rather than going into Windows Image viewer and doing one-by-one)
 - Wanted something with scripting/CLI support (use the CLIcore.py script with argument options)

## How does it work
The cropping is performed via a very simple "algorithm" - essentially for cropping a wider aspect ratio than original, the top and bottom portions of the image are discarded and the crop is centered. The reverse is true if the user wants to crop the image to a narrower aspect ratio compared to the original image. (This means that for now panoramic images are cropped as well...)

## Building binaries from scratch
Prerequisites: Python 3.8 (other versions may work), PySimpleGUI, PIL image library, argparse for CLI version.

Pyinstaller is used to build the Windows binaries. It may be possible to build Mac OSX binaries as well with it however this is untested :-)

Use command `pyinstaller GUI.spec`

## Todo
 - portrait image support
 - fix exit button in CLIcore progress bar
 - better UI
 - HiDPI
 - network share support
