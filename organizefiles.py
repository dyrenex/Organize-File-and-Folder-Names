import os
from glob import glob

"""
    If you have specific words to delete
    create a file and paste the name of
    the file below.
        Ex:
            WordsToDeleteFile = 'WordsToDelete.txt'

    If there are no words, then it will not look for a file.
    Please keep WordsToDeleteFile equal to ''
"""

replace_options = {
                    'words_file': 'NULL', # Name file with words in them
                    'periods': True, # would you like to replace periods?
                    'hyphens': True, # would you like to replace hyphens?
                  }

def change_name(file_name: str):

    global replace_options

    if (replace_options['periods']):
        file_name = file_name.replace('.', ' ', (file_name.count('.') - 1))

    if(replace_options['hyphens']):
        file_name = file_name.replace('-', '')

    if replace_options['words_file'] != 'NULL':
        try:
            words_file = open(replace_options['words_file'])

            for word in words_file:
                file_name = file_name.replace(word, '')

            words_file.close()

        except FileNotFoundError:
            print ('File not given or found')

    return file_name


if __name__ == "__main__":

    for (folders, subfolders, files) in os.walk('.'):
        for each_file in files:
            try:
                os.rename ( folders + '/' + each_file, folders + '/' + change_name(each_file) )
            except Exception as e:
                print (e)

    print ('done!')
