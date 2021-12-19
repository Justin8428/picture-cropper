from PIL import Image
import os

# params to modify
folder = "./bob"
dumpto = f"{folder}/new"
filetype = ".jpg"
desired_aspect_ratio = 4/3 # landscape only supported for now

# if desired_aspect_ratio > 1: # landscape only

os.mkdir(dumpto)
picture_files = [f for f in os.listdir(folder) if (os.path.isfile(os.path.join(folder, f)) and f.endswith(filetype))] # get only files in subfolder with ending .jpg (for eg)

for picture in picture_files:
    picdir = f"{folder}/{picture}" # kludgy but it will do for now
    im = Image.open(picdir)
    width, height = im.size

    # check to see if it is already in target aspect ratio, no need to crop otherwise
    if desired_aspect_ratio == width/height:
        print(f"{picture} already in {desired_aspect_ratio}, skipping...")
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
        print(f"Cropping {picture} to {desired_aspect_ratio}")
        im1 = im.crop((left, top, right, bottom)) # crop 
    # im1.show() # show image
    im1.save(f"{dumpto}/{picture}")