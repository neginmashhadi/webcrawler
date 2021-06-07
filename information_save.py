'''
This file host a class that aids in saving information for the index.
'''

import pathlib


class information_save():
    def __init__(self):
        self.bookkeeping_dict = {}
        self.index_dict = {}
        self.important_words_dict = {}
        self.unique_words_dict = {}
        self.url_dict = {}

        self.partial_index_file_paths = ['partial_index_0.txt',
                                         'partial_index_1.txt',
                                         'partial_index_2.txt']

        self.parent_path = str(pathlib.Path(__file__).parent.absolute())
        self.main_path = self.parent_path.replace('assignment_three_index_creation',
                                                  'assignment_three_main')

        self.dev_dir = self.parent_path + r'\\DEV\\'
        self.index_dir = self.parent_path + r'\\index_creation\\'
        self.final_index_dir = self.main_path + r'\\indexes\\'


info_class = information_save()
