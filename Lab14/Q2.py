import os

def exixts(old_file):
    if not os.path.isfile(old_file):
        raise RuntimeError("File does not exists.")
    
def same(old_text, new_text):
    if old_text == new_text:
        raise ValueError("Input is the same as the old text.")
    
def replace_text():
    file_name = input("Enter the file name: ")  
    # if not os.path.isfile(file_name):
    #     print("File does not exist.")
    #     return
    # else:
    try: 
        exixts(file_name)
    except RuntimeError as e:
        print(e)
        return
    old_text = input("Enter the text to replace: ")
    new_text = input("Enter the new text: ")
    infile = open(file_name, "r")
    content = infile.read()
    # if new_text in content:
    try:
        same(old_text, new_text)
        if old_text in content:
            content = content.replace(old_text, new_text)
            infile.close()
            infile = open(file_name, "w")
            infile.write(content)
            infile.close()
            print("Done")
        else:
            print("Text not found.")
            infile.close()
            return
    except ValueError as e:
        print("Input is the same as the old text.")
    except RuntimeError as e:
        print(e)
            
        
replace_text()
