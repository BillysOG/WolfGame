import os
import json
import csv

file_path1 = "C:/Users/ariro/OneDrive/Desktop/Her.txt"
file_path2 = "C:/Users/ariro/OneDrive/Desktop/Her.json"
file_path3 = "C:/Users/ariro/OneDrive/Desktop/Her.csv"

text1 = "I like her...."

text2 = {"Molly": "Orange",
         "Blacky": "Black",
         "Agon": "White and Black"}

text3 = [["Name","Colour","Age"],
         ["Molly","Orange","9"],
         ["Blacky","Black","12"]] 

def check_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"\nThe file '{file_path}' exists")
        if os.path.isfile(file_path):
            print(f"The file '{file_path}' is a regular file")
        elif os.path.isdir(file_path):
            print(f"The file '{file_path}' is a directory")
    else:
        print(f"\nThe file '{file_path}' does not exist")

def create_txt_file(file_path1, text):
    try:
        with open(file_path1, "w") as file:
            for x in range(10):
                file.write(f"{text}\n")
                print(f"\nThe txt file '{file_path1}' was created\n")
    except FileExistsError:
        print(f"\nThe file already exists\n")
        
def create_json_file(file_path2,text2):
    try:
        with open(file_path2,"w") as file:
            json.dump(text2,file,indent=4)
            print(f"\nThe json file '{file_path2}' was created\n")
    except FileExistsError:
        print(f"\nThe file already exists\n")

def create_csv_file(file_path3):
    try:
        with open(file_path3,"w") as file:
            writer = csv.writer(file)
            for row in text3:
                writer.writerow(row)
            print(f"\nThe csv file '{file_path3}' was created\n")
    except FileExistsError:
        print(f"\nThe file already exists\n")

def read_file(file_path3):        
    try:
        with open(file_path3, 'r') as file:
            content = csv.reader(file)
            for line in content:
                print(line)
    except FileNotFoundError:
        print(f"\nThe file '{file_path1}' does not exist\n")
    except PermissionError:
        print(f"\nYou do not have permission to read the file '{file_path1}'\n")
        
read_file(file_path3)