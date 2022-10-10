import pathlib;
import zipfile,fnmatch,os, re

rootPath = "/Users/brianrahadi/Documents/Personal/Langara College/TA Courses/sample files/sample_lab"

# start of rename file
def renameFile(oldName):
    # newName = ""
    for i in range(len(oldName)):
        if oldName[i].isalpha() or oldName[i] == '\'':
            return oldName[i:]

for path in pathlib.Path(rootPath).iterdir():
    if path.is_file():
        old_name = path.stem
        old_extension = path.suffix
        directory = path.parent
        new_name = renameFile(old_name + old_extension)
        path.rename(pathlib.Path(directory, new_name))
# end of rename file


# start of unzipping
pattern = '*.zip'
New = 'New*'

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        zipfile.ZipFile(os.path.join(root,     filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
        os.remove(os.path.join(rootPath, filename))

# end of unzipping