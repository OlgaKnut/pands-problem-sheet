# python_es.py
# Author: Olga Knutova
# Description: program reads in a text file and outputs the number of e's it contains

import sys

def count_letter (count, let='e'):
    with open (FILENAME, 'r') as f:
            for line in f:
                    #line=line.lower()   Convert text to lower case if you want to count both lower and upper letter e together
                    for char in line: 

#https://theprogrammingexpert.com/python-read-file-character-by-character/?utm_content=cmp-true
                        #read_data = f.read()
                        if char == let :

                            count= count+1
                                
    return count

if len(sys.argv)!=2:
    exit ("Please enter a text file as an argument on the command line")
    #https://stackoverflow.com/questions/2194163/python-empty-argument

FILENAME = sys.argv[1]

#https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python

count = 0
let ='e' # Note: We will count only lowcase e's in this case. 

ans= count_letter(count)
print (ans)

