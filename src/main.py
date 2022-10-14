from ast import arg
from sys import argv
from hide import hide
from extract import extract

usage = """
Usage : bsteg [hide/extract] [OPTIONS]

hide options : 
-f <file_path> \tCover file
-d <file_path> \tData file
-p <string>\tpassword
-o <file_path>\tOutput file 

extract options : 
-f <file_path> \tfile to extract data from 
-p <string> \tpassword
-o <file_path>\tOutput file 

-h/--help\tPrint this help 
"""

try:
    mode = argv[1]
except IndexError:
    print(usage)
    exit(0)

if mode == "hide":
    try:
        cover = argv[argv.index('-f')+1]
    except ValueError:
        print("No Cover File Specified")
    try:
        dataFile = argv[argv.index('-d')+1]
    except ValueError:
        print("No Data file File Specified")
        exit(1)
    try:
        password = argv[argv.index('-p')+1]
    except ValueError:
        print("WARNING : No password given 'demo' will be used as password ")
        password = "demo"
    try:
        outputfile = argv[argv.index('-o')+1]
    except ValueError:
        print("No output File Specified %s will be used as output file",'hidden'+cover)
        outputfile = "hidden"+cover
    print(hide(dataFile,cover,outputfile,password))
elif mode == "extract":
    try:
        file = argv[argv.index('-f')+1]
    except ValueError:
        print("No file Speccified")
        exit(1)
    try:
        password = argv[argv.index('-p')+1]
    except ValueError:
        print("WARNING : No password given 'demo' will be used as password ")
    try:
        outputfile = argv[argv.index('-o')+1]
    except:
        print("No output File Specified %s will be used as output file",'extracted_'+file)
        outputfile = "extracted_"+file
    print(extract(file,password,outputfile))