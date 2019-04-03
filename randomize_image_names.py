import uuid
import os
from os import listdir


def file_is_image(_file):
    # we can know an image file through its extension type
    is_image = _file[-4::] == ".jpg" or _file[-4::] == '.png' or _file[-5::] == ".jpeg"
    return is_image


def get_image_files(path):
    files = listdir(path)
    image_files = [_file for _file in files if file_is_image(_file)]    # the image files from the path
    return image_files


def randomize_file_names(path):
    image_files = get_image_files(path)
    # rename each file 
    for _file in image_files:
        print("Renaming:" + _file)
        # get extension type, as we'll need to maintain it
        file_extension = _file[-4::]
        new_name = "{}{}".format(uuid.uuid4(), file_extension)
        os.rename(path + _file, path + new_name)


if __name__ == "__main__":
    randomize_file_names(os.getcwd())
