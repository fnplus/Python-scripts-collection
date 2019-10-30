#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: rename.py
# Author: ernitron (c) 2017
# Mit License

import os
import sys
import re

Version = "1.4.2"

# To print colored text on term
RED   = ''
BLUE  = ''
CYAN  = ''
GREEN = ''
RESET = ''
BOLD  = ''
REV   = ''

def color():
    global RED, BLUE, CYAN, GREEN, RESET, BOLD, REV
    RED   = '\033[1;31m'
    BLUE  = '\033[1;34m'
    CYAN  = '\033[1;36m'
    GREEN = '\033[0;32m'
    RESET = '\033[0;0m'
    BOLD  = '\033[;1m'
    REV   = '\033[;7m'

def nocolor():
    global RED, BLUE, CYAN, GREEN, RESET, BOLD, REV
    RED   = ''
    BLUE  = ''
    CYAN  = ''
    GREEN = ''
    RESET = ''
    BOLD  = ''
    REV   = ''

def skip_name(filename, skip=''):
    '''-k skip: strip chars at beginning of filename'''
    try: elen = int(skip)
    except: elen = len(skip)
    return filename[elen:].strip()

def ztrip_name(filename, skip=0):
    '''-z skip: strip chars at end of filename'''
    try: elen = int(skip)
    except: elen = len(skip)
    if elen < len(filename):
        return filename[:-elen].strip()
    return filename

def start_name(filename, start, replace):
    '''strip and replace string in filename'''
    startlen = 0
    filenamelower = filename.lower()
    if start and filenamelower.startswith(start.lower()):
        startlen = len(start)
    return replace + filename[startlen:].strip()

def remove_underscore(filename):
    filename = filename.replace('_', ' ')
    return filename.replace('-', ' ')

def replace_blank(filename, fill_char='_'):
    '''Replace blank or spaces with fill_char (default to '_') '''
    return filename.replace(' ', fill_char)

def strip_name(filename):
    f = filename.replace('  ', ' ')
    return f.strip(' -._\t\n\r')

def space_case(filename):
    '''Convert to Title Case inserting spaces where underscore'''
    prec = ''
    newname = ''
    for char in filename:
        if char == '_':
            newname += ' '
            continue
        if prec.islower() and char.isupper() :
            newname += ' '
        newname += char
        prec = char
    return newname

def camel_case(filename):
    '''Convert to CamelCase: from camel_case returns Camel Case'''
    #tmpname = filename.replace('_', ' ')
    tmpname = filename

    prec = ''
    newword = ''
    for char in tmpname:
        if prec.islower() and char.isupper() :
            newword += ' '
        newword += char
        prec = char
    tmpname = newword

    modified_name = re.findall('[\w]+', tmpname.lower())
    newname = ' '.join([word.title() for word in modified_name])
    tmpname = newname.replace("L ", "L'")
    return tmpname

def replace_content(filename, contains, replace):
    '''Replace content with replace string :returns newname '''
    if contains and contains in filename:
        return filename.replace(contains, replace)
    return filename

def delete_string(filename, contains):
    '''Delete content in string: returns newname'''
    if contains in filename:
        return filename.replace(contains, '')
    return filename

def lower_case(filename):
    '''Lower filename: from NEWNAME returns newname'''
    return filename.lower()

def upper_case(filename):
    '''Upper filename: from newname returns NEWNAME'''
    return filename.upper()

def title_case(filename):
    '''Upper filename: from newname returns Newname'''
    return filename.title()

def add_number(filename, counter, bottom):
    '''Add a sequence 2digit at beginning of filename :returns newname '''
    if bottom:
        return '%s-%02d' % (filename, counter)
    else:
        return '%02d-%s' % (counter, filename)

def add_string(filename, string, start=True):
    '''Add a string :returns string-newname '''
    if start:
        return '%s-%s' % (string, filename)
    else:
        return '%s-%s' % (filename, string)

def substitute(filename, pattern, replace):
    if not pattern: return filename
    if pattern[-1] == 'i':
        flags = re.IGNORECASE
    else:
        flags = None
    try:
        spb = pattern.split('/')
        return re.sub(spb[1], spb[2], filename, flags=flags)
    except:
        pass
    return re.sub(pattern, replace, filename)

def timestamp_name(filename, newname, bottom):
    from time import localtime, strftime
    filestat = os.stat(filename)
    timestring = strftime("%Y-%m-%d", localtime(filestat.st_mtime))
    if bottom:
        return f'{newname}-{timestring}'
    else:
        return f'{timestring}-{newname}'

def swap_name(filename, swap):
    '''Swap name like Alfa Beta Gamma -> GAMMA, Alfa, Beta'''
    '''Swap name like Alfa Beta-> BETA, Alfa'''
    parts = filename.split(swap)
    newname = parts[-1].upper() + ','
    for part in parts[0:-1] :
        part = part.strip(',')
        newname += ' ' + part.title()
    newname = newname.strip(',')
    newname = newname.strip()
    return newname

def sanitize_name(filename):
    sanitize = """[]()%@"!$^&*,:;></?{}"""
    for char in sanitize:
        filename = filename.replace(char, '')
    return strip_name(filename)

def hash_name(filename, hash='sha256'):
    import hashlib
    try:
        h = hashlib.new(hash)
    except:
        print (hashlib.algorithms_available)
        sys.exit(0)
    filename = filename.encode('ascii', 'ignore')
    h.update(filename)
    return h.hexdigest()

def bulk_rename(a):
    '''The loop on current dir to rename files based on requests'''

    if a.files:
        filelist = a.files
    else:
        filelist = os.listdir('.')

    for filename in filelist:
        if a.recursive and os.path.isdir(filename):
            os.chdir(filename)
            bulk_rename(a)
            os.chdir('..')
        if a.directory and not os.path.isdir(filename):
            continue
        if a.regular and not os.path.isfile(filename):
            continue
        if a.match and not re.match(a.match, filename):
            continue
        if a.contains and not a.contains in filename:
            continue

        newname, extension = os.path.splitext(filename)
        if a.extlower:
            extension = extension.lower()
        if a.suffix and not a.suffix in extension:
            continue

        if a.remove:
            remove_filename(filename, a.force, a.yes, a.verbose)
            continue

        if a.start:
            newname = start_name(newname, a.start, a.replace)
        if a.skip:
            newname = skip_name(newname, a.skip)
        if a.delete:
            newname = delete_string(newname, a.delete)
        if a.contains:
            newname = replace_content(newname, a.contains, a.replace)
        if a.expression:
            newname = substitute(newname, a.expression, a.replace)
        if a.camel:
            newname = camel_case(newname)
        if a.upper:
            newname = upper_case(newname)
        if a.lower:
            newname = lower_case(newname)
        if a.title:
            newname = title_case(newname)
        if a.blank:
            newname = replace_blank(newname, fill_char=a.blank)
        if a.sanitize:
            newname = sanitize_name(newname)
        if a.timestamp:
            newname = timestamp_name(filename, newname, a.bottom)
        if a.number:
            newname = add_number(newname, a.number, a.bottom)
            a.number += 1
        if a.string:
            newname = add_string(newname, a.string, a.start)
        if a.strip:
            newname = strip_name(newname)
        if a.ztrip:
            newname = ztrip_name(newname, a.ztrip)
        if a.under:
            newname = remove_underscore(newname)
        if a.swap:
            newname = swap_name(newname, a.swap)
        if a.hash:
            newname = hash_name(newname, a.hash)
        if a.extension:
            extension = a.extension

        # Finally do the rename on file or directory
        if not newname:
            newname = timestamp_name(filename, 'ZZZZ-ToBeDefined', True)

        newname = newname + extension
        do_rename(filename, newname, a.force, a.yes, a.verbose)


def remove_filename(filename, force, yes, verbose):
    if verbose:
        print('File to be removed\t=>', CYAN, filename, RESET)

    if not yes:
       answer = input(f'remove {filename} " ? [y/n] ')
       yes = answer.lower() == 'y'
       if not yes: return

    cwd = os.getcwd()
    print('THIS FILE         \t=>', GREEN, cwd, filename, RESET)
    if yes and force:
        try:
            # Preserve creation and access time is default
            os.unlink(filename)
            print('WAS REMOVED \t=>', GREEN, filename, RESET)

        except:
            print('Cannot remove ', RED, filename, RESET)
    else:
        print('WILL BE REMOVED \t=>', CYAN, filename, RESET)

def do_rename(filename, newname, force, yes, verbose):

    if not newname or filename == newname:
        if verbose:
            print('Nothing to do for\t=>', RED, filename, RESET)
        return

    if verbose:
        print('File to be renamed\t=>', CYAN, filename, RESET)

    if not yes:
       answer = input(f'Rename {filename} to "{newname}" ? [y/n] ')
       yes = answer.lower() == 'y'
       if not yes: return

    print('THIS FILE         \t=>', GREEN, filename, RESET)
    if newname and yes and force:
        if os.path.isfile(newname):
            print('FILE EXISTS \t=>', RED, newname, RESET)
            if not force:
               print('CANT RENAME\t=>', RED, newname, RESET)
               return
        try:
            # Preserve creation and access time is default
            stat = os.stat(filename)
            os.rename(filename, newname)
            os.utime(newname, (stat.st_atime, stat.st_mtime))
            print('HAS BEEN RENAMED TO\t=>', GREEN, newname, RESET)

        except:
            print('Cannot rename ', RED, filename, RESET)
    else:
        print('WILL BE RENAMED TO\t=>', CYAN, newname, RESET)

if __name__ == '__main__':
    import argparse

    example_text = '''
    Examples:
    $ rename.py --skip start_of_file --skip 5 --contains This --replace That --number --suffix .mp3 --force
    would rename a file like: start_of_file1234_Take_This.mp3
                 into: 01-Take_That.mp3

    $ rename.py -s start_of_file -k 5 -e '/This/That/' -n -x mp3 -F
    would do the same
 '''

    parser = argparse.ArgumentParser(description='rename files', epilog=example_text,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-a', '--string', help='add string')
    parser.add_argument('-b', '--blank', help='Replace blank with _', nargs='?', const='_')
    parser.add_argument('-c', '--contains', help='check for string in filename; works with -r')
    parser.add_argument('-d', '--delete', help='delete string in filename')
    parser.add_argument('-e', '--expression', help='pattern with regex')
    parser.add_argument('-r', '--replace', help='replace string; works with -c and -p', default='')
    parser.add_argument('-s', '--start', help='delete string from beginning of filename')
    parser.add_argument('-z', '--ztrip', help='delete n chars from end of filename')
    parser.add_argument('-k', '--skip', help='skip n char from start of filename')
    parser.add_argument('-n', '--number', type=int, help='Add a 2 digit sequence', nargs='?', const='1')
    parser.add_argument('-w', '--swap', help='swap names Alfa Beta->Beta Alfa', nargs='?', const=' ')
    parser.add_argument('-ext', '--extension', help='change extension example to .mp3')
    parser.add_argument('-exl', '--extlower', action='store_true', help='Transform extension into lower case')
    # Applicability
    parser.add_argument('--root', help='this will be the root directory', default='./')
    parser.add_argument('-m', '--match', help='apply only to file that match pattern')
    parser.add_argument('-x', '--suffix', help='apply only to file with suffix like .mp3')
    parser.add_argument('-D', '--directory', action='store_true', help='Apply only to directory')
    parser.add_argument('-G', '--regular', action='store_true', help='Apply only to regular files')
    parser.add_argument('-R', '--recursive', action='store_true', help='Recursive into subdirs')
    parser.add_argument('-Y', '--yes', action='store_false', help='Confirm before rename [y/n]')
    parser.add_argument('-F', '--force', action='store_true', help='Force to rename (do it!)', default=False)
    #parser.add_argument('-f', '--files', help='apply to list of files', nargs='*')
    # Other Boolean Flags
    parser.add_argument('-_', '--under', action='store_true', help='Remove underscores and minuses', default=False)
    parser.add_argument('-B', '--bottom', action='store_true', help='Put number sequence at end')
    parser.add_argument('-C', '--camel', action='store_true', help='Transform filename in CamelCase')
    parser.add_argument('-L', '--lower', action='store_true', help='Transform filename into lower case')
    parser.add_argument('-U', '--upper', action='store_true', help='Transform filename into upper case')
    parser.add_argument('-T', '--title', action='store_true', help='Transform into Title case ')
    parser.add_argument('-V', '--version', action='store_true', help='Print version and die')
    parser.add_argument('-O', '--color', action='store_true', help='Print messages in color')
    parser.add_argument('-S', '--strip', action='store_true', help='Strip blank|tab at end or bottom')
    parser.add_argument('-P', '--timestamp', action='store_true', help='Add timestamp of access time')
    parser.add_argument('-Z', '--sanitize', action='store_true', help='Sanitize name from weird chars')
    parser.add_argument('-H', '--hash', help='filename is hash', nargs='?', const='sha256')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    # Other Flags
    parser.add_argument('--remove', action='store_true', help='remove file if match')
    # Files
    parser.add_argument('files', nargs='*')

    # get args
    args = parser.parse_args()

    if args.version:
        print("Version ", Version)
        sys.exit(0)

    if args.color:
        color()

    # If it is piped to other program (i.e. rename.py... | less) than don't color print!
    if not os.isatty(1):
        nocolor()

    os.chdir(args.root)
    bulk_rename(args)

