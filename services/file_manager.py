import os, shutil
from os import listdir
from os.path import isfile, join

def onlyfiles(folder):
    return [f for f in listdir(folder) if isfile(join(folder, f))]

class FileManager:
    def __init__(self, base_directory : str, current_directory : str):
        self.base_directory = base_directory
        self.current_directory = current_directory        
        
    def clear_current(self, prefixos):     
        for filename in onlyfiles(self.current_directory):
            if filename[0:8] not in prefixos:
                file_path = os.path.join(self.current_directory, filename)
                try:
                    print('Deleting ' + filename)
                    os.unlink(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

    def update_current(self, prefixos):
        for file in onlyfiles(self.base_directory):
            if os.path.basename(file)[0:8] in prefixos:
                if not os.path.exists(os.path.join(self.current_directory, file)):
                    print('Copying ' + file)
                    shutil.copy(os.path.join(self.base_directory, file), os.path.join(self.current_directory, file))