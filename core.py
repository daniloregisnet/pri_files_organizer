import os, shutil
from os import listdir
from os.path import isfile, join

from services.criteria_service import CriteriaService
from services.file_manager import FileManager


class Core:
    def __init__(self, base_directory: str, current_directory: str):
        self.base_directory = base_directory
        self.current_directory = current_directory

        

    def run(self):

        if not self.verify_parameters():
            return

        criteriaService = CriteriaService()

        fileManager = FileManager(self.base_directory, self.current_directory)

        prefixos = criteriaService.build_pattern_prefix()

        fileManager.clear_current(prefixos)

        fileManager.update_current(prefixos)            

    def verify_parameters(self):
        if not os.path.exists(self.base_directory):
            print('Base directory %s  not found.' % (self.base_directory))
            return False

        if not os.path.exists(self.current_directory):
            print('Current directory %s not found.' % (self.current_directory))
            return False

        return True