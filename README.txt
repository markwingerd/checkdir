About
-----

The CheckDir library allows you to check if a given string is a suitable
directory path for any file system and correct the string as needed.
This library is currently for python 2.7

Usage
=====

In your project import checkdir and call one of the following functions.

    validate_string_ntfs(dirStr [,pathType])
    validate_string_unix(dirStr [,pathType])
    check_string_ntfs(dirStr [,pathType])
    check_string_unix(dirStr [,pathType])
    delete_seperator_ntfs(fileName [,pathType])
    delete_seperator_unix(fileName [,pathType])
    check_seperator_ntfs(fileName [,pathType])
    check_seperator_unix(fileName [,pathType])
    split_file_and_path(dirStr, pathType)
    
    
- dirStr is a string that should represent a directory path.
- pathType is optional for all function except split_file_and_path. 
This variable is required if you are intending to varify a directory 
path obeys rules for another file system. e.g: You are creating a 
file for Linux and later plan to move the file to Windows.  Curent 
pathTypes are:
    
    NTFS_PATH_TYPE
    UNIX_PATH_TYPE
    
The validate varients will automatically correct errors for the file 
system and return the correction as a string. The check varients will 
raise exceptions when there is an error and leave it to you to fix them.

The _seperator_ functions are to be used only on filenames. the check
varients of these only display an error. the delete varients will 
automatically delete any seperator in the file names.  CURRENTLY you
will have to manually strip any preceeding seperator.  i.e:

    "/fileName.txt" - remove the "/"

Examples
++++++++

Please see and run the code in examples.py

LICENSE
+++++++
Copyright (C) 2012 Mark Wingerd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
