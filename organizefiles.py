import os
#from glob import glob

options = {
            'words_file'        : 'WordsToDelete.txt',
            'include_files'     : True,
            'include_folders'   : True,
            'periods'           : True,
            'hyphens'           : True,
            'trailing_spaces'   : True,
            'double_spaces'     : False
          }

def trailing_spaces(word: str):
    extension_pos = word.find('.') #starting position of file extensions example: .py

    while word[extension_pos - 1:extension_pos] == ' ':
        word = word[:extension_pos - 1] + word [extension_pos:]
        extension_pos = word.find('.')

    return word


def remove_words(word: str):
    try:
        open_file = open(options['words_file'], 'r')

        for current in open_file:
            current = current.replace('\n', '') # incase there are any endlines
            word = word.replace(current, '')

        open_file.close()

        return str(word)

    except FileNotFoundError:
        print('File not given or found')

def removing_doubles(word: str):
    while word.find('  ') != -1:
        word = word.replace('  ', ' ')
    return word

def change_name(word: str, is_file: bool):

    global options

    if options['periods'] and is_file == True:
        word = word.replace('.', ' ', (word.count('.') - 1))

    elif options['periods'] and is_file == False:
        word = word.replace('.', ' ')

    if options['hyphens']:
        word = word.replace('-', ' ')

    if options['words_file'] != 'NULL':
        word = remove_words(word)

    if options['double_spaces']:
        word = removing_doubles(word)

    if options['trailing_spaces']:
        word = trailing_spaces(word)

    return str(word)

if __name__ == "__main__":

    for x in range(2): # need to pass twice or some files won't get checked

        for (folders, subfolders, files) in os.walk('.'):

            if options['include_files']:
                if folders[0:3] != '.\.' and folders[0:3] != './.':

                    #Files
                    for each_file in files:
                        try:
                            if each_file[0:1] != '.':  # ignore hidden files
                                new_name = change_name(each_file, True)

                                if new_name != each_file:
                                    os.rename(folders + '/' + each_file,
                                              folders + '/' + new_name)

                        except OSError as oserror:
                            print(oserror)
                        except Exception as e:
                            raise e

                #Folders
                if options['include_folders']:
                    for each_folder in subfolders:

                        try:
                            if each_folder[0:1] != '.': #ignore hidden files
                                new_name = change_name(each_folder, False)

                                if new_name != each_folder:
                                    os.rename ( folders + '/' + each_folder,
                                                folders + '/' + new_name)

                        except OSError as oserror:
                            print(oserror)
                        except Exception as e:
                            raise e

    print ('done!')
