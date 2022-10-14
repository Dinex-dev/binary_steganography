from sys import argv
from hide import hide
from extract import extract

print("""
Usage : bsteg [hide/extract] [OPTIONS]

hide options : 
-f <file_path> \tFile to hide data in 
-a <file_path> \tFile you want to hide
-p <string>\tpassword
-o <file_path>\tOutput file name

extract options : 
-f <file_path> \tfile to extract data from 
-p <string> \tpassword
""")