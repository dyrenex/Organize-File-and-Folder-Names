import os
from glob import glob

def change_folder_name(tempname: str):

    tempname = dirname.replace('.', ' ')
    tempname = tempname.replace('-', ' ')
    tempname = '.' + tempname[1:]  # missing first '.' in path

    for word_to_replace in open_file:
        word_to_replace = word_to_replace.replace('\n', "")
        tempname = tempname.replace(word_to_replace, '')

    open_file.seek(0)  # resets to the top of file
    return str(tempname)


def change_file_name(templist: list):

    newList = []

    for item in templist:

        #don't replace the last '.'
        item = item.replace('.', ' ', (item.count('.') - 1))
        item = item.replace('-', ' ')

        for word_to_replace in open_file:
            word_to_replace = word_to_replace.replace('\n', '')  # endline messes with prorgam.
            item = item.replace(word_to_replace, '')


        #next while loop takes out any usless spaces at the end of file.
        while item[item.find('.') - 1: item.find('.')] == " ":
            item = item[:item.find('.') - 1] + item[item.find('.'):]

        open_file.seek(0)
        newList.append(item)

    return newList


if __name__ == "__main__":
    counter = 0
    filesNeedFolders = glob('./*.mp4')  # looks for all .mp4 files.
    filesNeedFolders = glob('./*.mkv')  # looks for all .mkv files.

    for files in filesNeedFolders:
        os.mkdir('{}'.format(files[:-4]))
        movefile = '{}/'.format(files[:-4]) + files[2:]
        os.rename(files, movefile)

    try:
         open_file = open('WordsToDelete.txt', 'r')

    except FileNotFoundError:
        print('Could not open WordsToDelete.txt...')

    for dirname, dirnames, filenames in os.walk('.'):
        # the second expression was to avoid any hidden files. EX: '.\.This file is hidden.txt'
        if ((counter != 0) and (dirname[0:3] != '.\.')) and ((counter != 0) and (dirname[0:3] != './.')):

            try:
                posOfList = 0
                for item in change_file_name(filenames):
                    os.rename(dirname + '/' + filenames[posOfList], dirname + '/' + item)
                    posOfList += 1

                os.rename(dirname, change_folder_name(dirname))

            except Exception as e:
                print(e)

        counter += 1

    open_file.close()
