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
    
- dirStr is a string that should represent a directory path.
- pathType is optional. This variable needs is required if you are 
intending to varify a directory path obeys rules for another file
system. e.g: You are creating a file for Linux and later plan to move
the file to Windows.  Curent pathTypes are:
    
    NTFS_PATH_TYPE
    UNIX_PATH_TYPE
    
The validate validate varients will automatically correct errors for
the file system and return the correction as a string. The check 
varients will raise exceptions when there is an error and leave it to
you to fix them.

Examples
++++++++

Please see and run the code in examples.py