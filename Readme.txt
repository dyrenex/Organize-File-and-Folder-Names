By: Derek Santos

Which Python?
=============

Python 3!

What does this script do?
=========================

This script deletes any unwanted words, phrases, and hyphens that are found within a file name in the current folder, and any folder within.

Where does it work?
===================

Works on Mac and Linux.
SHOULD work on Windows, but still not sure yet. 

How does it work?
=================

WordsToDelete.txt is what words you would like to delete from a given file name. Put every word or phrase on separate lines please.


Options!
========

To easily choose what is effected by the program, I have included an 'options' dictionary within the python script.
Just change 'True' to 'False' to activate and deactivate an option.
     'True'  = Active
     'False' = Inactive

List of what everything does:

     'words_file':
          Change 'NULL' to the file that contains words that you want to delete.
          !!! Please make sure each word or phrase are on separate lines !!!

     'include_files':
          When this is True, files will be changed by the program.

     'include_folders':
          When this is True, folders will be changed by the program.

     'periods':
          When this is True, periods will be changed to a single space.

     'hyphens':
          When this is True, hyphens will be changed to a single space.

     'trailing_spaces':
          When this is True, trailing spaces in names will be deleted.
          Example:
               Before: "TempFile   .txt"
               After: "TempFile.txt"

     'double_spaces':
          When this is True, double spaces will be replaced by a single space.


Todo
====
[ X ] Include folders independently
[ X ] Include files independently
[ X ] Periods get deleted in file and folder names
[ X ] Hyphens get deleted in file and folder names
[ X ] Get rid of trailing spaces after file and folder names
[ X ] Replaces double spaces to single spaces
[ X ] Words and Phrases get deleted in file and folder names
[ ] If it finds a specific file extension not within a folder, in the current directory, it will make a folder with it's name, and move the file inside of the new folder.
