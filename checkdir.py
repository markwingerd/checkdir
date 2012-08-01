#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


NTFS_PATH_TYPE = { 'drive': r'^[A-Z]{1}\:$', 'separator': r'\\+' }
NTFS_INVALID_CHAR = re.compile(r'[\"*:<>?/|]|^\.|\.$|^\ |\ $')
NTFS_LOWEST_VALUE = 32
NTFS_MAX_CHARS = 255
NTFS_INVALID_NAME = ('AUX', 'CLOCK$', 'COM1', 'COM2', 'COM3', 'COM4',
                     'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 
                     'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 
                     'LPT8', 'LPT9', 'NUL', 'PRN')
                     
UNIX_PATH_TYPE = { 'drive': r'file\:', 'separator': r'/+' }
UNIX_INVALID_CHAR = re.compile(r'[<>|:&]')
UNIX_LOWEST_VALUE = 1
UNIX_MAX_CHARS = 255
UNIX_INVALID_NAME = ('')


class DirectoryError(Exception):
    EMPTY_STRING = 1
    MAX_CHARS = 2
    INVALID_CHAR = 3
    INVALID_NAME = 4
    

def check_string_ntfs(s, pathType=NTFS_PATH_TYPE):
    """
    Checks a string against NTFS file system rules.
    
    s - A string that should be in the format of a directory path.
    pathType is optional. As an example it can be used to check Windows
        file format rules against a Unix Path.
    
    Raises a DirectoryError and its location.
    `   eg: ('Error Text',INVALID_CHAR,ErrorLocation)
        EMPTY_STRING will return 0.
        MAX_CHARS will return NTFS_MAX_CHARS
        INVALID_CHAR will return the position of the invalid char
        INVALID_NAME will return a string that is invalid.
    """
    pathParts = _get_path_parts(s, pathType)
        
    if _is_empty(s): raise DirectoryError('String is empty', DirectoryError.EMPTY_STRING, 0)
    if _check_max_chars(s, NTFS_MAX_CHARS): raise DirectoryError('Maximum characters in string exceeded', DirectoryError.MAX_CHARS, NTFS_MAX_CHARS)

    errPos = 0
    for part in pathParts:
        # If there is a drive present, add the length of the drive part
        if _has_drive(part, pathType):
            errPos += s.find(pathParts[1]) 
            continue
        if part in NTFS_INVALID_NAME: 
            raise DirectoryError('Path cannot use a reserved name', DirectoryError.INVALID_NAME, part)
        if NTFS_INVALID_CHAR.search(part): 
            errPos += NTFS_INVALID_CHAR.search(part).start()
            raise DirectoryError('String cannot use invalid characters', DirectoryError.INVALID_CHAR, errPos)
        errPos += len(part) + 1
       
    for i in range(0, len(s)):
        if ord(s[i]) < NTFS_LOWEST_VALUE: raise DirectoryError('String cannot use invalid characters', DirectoryError.INVALID_CHAR, i)


def check_string_unix(s, pathType=UNIX_PATH_TYPE):
    """
    Checks a string against UNIX file system rules.
    
    s - A string that should be in the format of a directory path.
    pathType is optional. As an example it can be used to check Windows
        file format rules against a NTFS Path.
    
    Raises a DirectoryError and its location.
    `   eg: ('Error Text',INVALID_CHAR,ErrorLocation)
        EMPTY_STRING will return 0.
        MAX_CHARS will return UNIX_MAX_CHARS
        INVALID_CHAR will return the position of the invalid char
        INVALID_NAME will return a string that is invalid.
    """
    pathParts = _get_path_parts(s, pathType)
    
    if _is_empty(s): raise DirectoryError('String is empty', DirectoryError.EMPTY_STRING, 0)
    if _check_max_chars(s, UNIX_MAX_CHARS): raise DirectoryError('Maximum characters in string exceeded', DirectoryError.MAX_CHARS, UNIX_MAX_CHARS)
    
    errPos = 0
    for part in pathParts:
        # If there is a drive present, add the length of the drive part
        if _has_drive(part, pathType):
            errPos += s.find(pathParts[1])
            continue
        if part in UNIX_INVALID_NAME:
            raise DirectoryError('Path cannot use a reserved name', DirectoryError.INVALID_NAME, part)
        if UNIX_INVALID_CHAR.search(part):
            errPos += UNIX_INVALID_CHAR.search(part).start()
            raise DirectoryError('String cannot use invalid characters', DirectoryError.INVALID_CHAR, errPos)
        errPos += len(part) + 1
    
    for i in range(0, len(s)):
        if ord(s[i]) < UNIX_LOWEST_VALUE: raise DirectoryError('String cannot use invalid characters', DirectoryError.INVALID_CHAR, i)



def validate_string_ntfs(s, pathType=NTFS_PATH_TYPE):
    """ 
    Checks and fixes string against NTFS file system rules.
    
    s - A string that should be in the format of a directory path.
    pathType - Optional. A given constant that describes the type of
               path given in s.
    
    Returns a corrected directory path as a string.
    """
    loopControl = 0
    
    # Loop breaks if no errors given.
    while loopControl <= 255:        
        try:
            check_string_ntfs(s,pathType)
            break
        except DirectoryError as e:
            if e[1] == DirectoryError.EMPTY_STRING: 
                s = _fix_empty_string(s)
            elif e[1] == DirectoryError.MAX_CHARS: 
                s = _fix_max_chars(s,e[2])
            elif e[1] == DirectoryError.INVALID_CHAR: 
                s = _fix_invalid_char(s,e[2])
            elif e[1] == DirectoryError.INVALID_NAME: 
                s = _fix_invalid_name(s,e[2])
        loopControl += 1
    return s
    
    
    
def validate_string_unix(s, pathType=UNIX_PATH_TYPE):
    """ 
    Checks and fixes string against UNIX file system rules.
    
    s - A string that should be in the format of a directory path.
    pathType - Optional. A given constant that describes the type of
               path given in s.
    
    Returns a corrected directory path as a string.
    """
    loopControl = 0
    
    # Loop breaks if no errors given
    while loopControl <= 255:
        try:
            check_string_unix(s,pathType)
            break
        except DirectoryError as e:
            if e[1] == DirectoryError.EMPTY_STRING: 
                s = _fix_empty_string(s)
            elif e[1] == DirectoryError.MAX_CHARS: 
                s = _fix_max_chars(s,e[2])
            elif e[1] == DirectoryError.INVALID_CHAR: 
                s = _fix_invalid_char(s,e[2])
            elif e[1] == DirectoryError.INVALID_NAME: 
                s = _fix_invalid_name(s,e[2])
        loopControl += 1
    return s        
   
        

def _get_path_parts(s, pathType):
    """ Breaks the directory string into subfolders/files """
    return re.split(pathType['separator'], s)
    
def _has_drive(part, pathType):
    """
    Determines if the path has a drive or 'file:' (can anyone tell me 
        what this is called?). This must be run after _get_path_parts
        
    part needs to be an item from _get_path_parts
    pathType must be one of the 
        predefined constants:
        NTFS_PATH_TYPE
        UNIX_PATH_TYPE
        etc
    
    Returns true if part is a drive letter or 'file:'.
    """
    if re.match(pathType['drive'], part, flags=re.IGNORECASE): 
        return True
    return False
    
def _check_max_chars(s, maxChars):
    """ Checks to see if the string is over the max Character limit """
    if len(s) > maxChars:
        return True
    return False
    
def _is_empty(s):
    """ Returns true if s has no value """
    if len(s) <= 0:
        return True
    return False

def _fix_invalid_char(s, i):
    """ Returns the string with the exlusion of the invalid char """
    return s[:i] + s[i+1:]
    
def _fix_invalid_name(s, name):
    """ Returns the string with added text behind the invalid name """
    i = s.find(name) + len(name)
    return s[:i] + 'fix' + s[i:]
    
def _fix_empty_string(s):
    """ Unfinished. Whats the best way to fix this """
    pass
    
def _fix_max_chars(s, i):
    """ Unfinished. Whats the bext way to fix this """
    pass
