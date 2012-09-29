#   example.py  Copyright (C) 2012 Mark Wingerd
#
#   This program comes with ABSOLUTELY NO WARRANTY;
#   This is free software, and you are welcome to redistribute it
#   under certain conditions; Please seel the file LICENSE for detail.
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import checkdir


unixTest = 'file://AUX/#music/Story: So & Far/Song.mp3'
ntfsTest = 'c:\AUX\#Music\O Seven: & The\Test.mp3'


# validate_string_ntfs with a windows directory path would be used
# solely for an ntfs file system. Because a windows directory path is
# given, there is no need to set the pathType flag.
print 'Windows Error Control - Given a windows path name\n'
print 'Invalid Windows Path:   ', ntfsTest
print 'Corrected Windows Path: ', checkdir.validate_string_ntfs(ntfsTest)
print '\nEND\n\n\n'


# This use of validate_string_ntfs is when you are writing a file to
# a unix system BUT you want to insure that the file structure is also
# valid for an ntfs file system like windows.  Since you are given the
# function a Unix directory path you MUST set the pathType value to
# UNIX_PATH_TYPE.
print 'Windows Error Control - Given a Linux path name\n'
print 'Unix path is invalid for Windows: ', unixTest
print 'Corrected Unix path for Windows:  ', checkdir.validate_string_ntfs(unixTest, pathType=checkdir.UNIX_PATH_TYPE)
print '\nEND\n\n\n'


# validate_string_unix when a unix directory path would be used when
# you only intend on the directory/file being used only on a unix file
# system.  No pathType needs to be declared since a unix path is given.
print 'Unix Error Control - Given a Linux path name\n'
print 'Invalid Unix Path:   ', unixTest
print 'Corrected Unix Path: ', checkdir.validate_string_unix(unixTest)
print '\nEND\n\n\n'


# This use of validate_string_unix is when you are writing a file to 
# Windows BUT you want to insure that the file structure is also valid 
# for a unix file system. The pathType flag must be set to 
# NTFS_PATH_TYPE
print 'Unix Error Control - Given a Windows path name\n'
print 'Windows path is invalid for Unix: ', ntfsTest
print 'Corrected Windows path for Unix:  ', checkdir.validate_string_unix(ntfsTest, pathType=checkdir.NTFS_PATH_TYPE)
print '\nEND\n\n\n'


# To truely make sure you want your directory path works for all file
# systems you want to use multiple checks.  In this example we are going
# to attempt to create a directory on a Unix file system but later we
# intent to move the directory to a windows machine. The import checkdir
# has already been established above.
myPath = 'file:/Misc /NUL/Ba*dD"ir/Inv<ali>d.txt'
print 'Does not work at all:                    ', myPath
myPath = checkdir.validate_string_unix(myPath)
print 'Works for Unix but not Windows:          ', myPath
myPath = checkdir.validate_string_ntfs(myPath, pathType=checkdir.UNIX_PATH_TYPE)
print 'This now works for both Unix and Windows:', myPath
# From here, you can call os.path.exists(myPath) and os.makedirs(myPath)
# without worrying about any unknown errors.



### check_string_**** #############################

# If you wish to handle the error correction yourself you can use the
# check varient of the functions (check_string_ntfs, check_string_unix).
# The check varients will raise an exception if it finds any errors in
# the directory string.  The exception returns three parts: The 
# description of the error, the error code, and a value for the error 
# which can be used to correct the error.
#
# The following is the Error code followed by the value for the error.
#   checkdir.EMPTY_STRING   This will always be Zero. No string given.
#   checkdir.MAX_CHARS      The max characters allowed. Shorten the str.
#   checkdir.INVALID_CHAR   The position of the invalid character.
#   checkdir.INVALID_NAME   The text that is invalid.
# For the latter two, you can delete the error or modify it how you
# prefer.
#
# Only one error is returned at a time so you will want to encase your
# error control in a loop.  See a validate function in checkdir.py for
# a better example.
