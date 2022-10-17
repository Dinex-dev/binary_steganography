from sys import argv
from hide import hide
from extract import extract

usage = """
Usage : python ./main.py [hide/extract] [OPTIONS]

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


def exiting():
    print(usage)
    exit(0)


try:
    mode = argv[1]
    if "-h" in argv or "--h" in argv:
        exiting()
    if "hide" in argv and "extract" in argv:
        print("Hide and Extract cannot be used together")
        exit()
    elif mode == "hide":
        if "-f" not in argv or "-d" not in argv:
            print("One or more required flags were not given.")
            print("Use --help for usage info.")
            exit()
        try:
            cover = argv[argv.index('-f') + 1]
        except ValueError:
            print("No Cover File Specified.")
            exit()

        try:
            dataFile = argv[argv.index('-d') + 1]
        except ValueError:
            print("No Data file File Specified")
            exit()

        try:
            password = argv[argv.index('-p') + 1]
        except ValueError:
            print("WARNING : No password given 'demo' will be used as password.")
            password = "demo"

        try:
            outputFile = argv[argv.index('-o') + 1]
        except ValueError:
            print(f"No output File Specified 'hidden {cover}' will be used as output file")
            outputFile = "hidden " + cover
        print(hide(dataFile, cover, outputFile, password))

    elif mode == "extract":
        try:
            file = argv[argv.index('-f') + 1]
        except Exception:
            print("No file Specified")
            exit(1)
        try:
            password = argv[argv.index('-p') + 1]
        except Exception:
            print("WARNING : No password given 'demo' will be used as password ")
            password = 'demo'

        try:
            outputFile = argv[argv.index('-o') + 1]
        except Exception:
            print(f"No output File Specified 'extracted_{file}' will be used as output file")
            outputFile = "extracted_" + file
        print(extract(file, password, outputFile))
except IndexError:
    exiting()
