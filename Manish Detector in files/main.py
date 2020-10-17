# suppose i have  multiple file in the directory and i want to reflect those files which
# is holding Manish
# so this project is helpful to detect spam
# i.e. i can check which file is containing the spam

import os


def isManish(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

        # detect all forms of Manish line mAnisH
        if "manish" in fileContent.lower():
            return True
        else:
            return False


if __name__ == '__main__':
    dir_contents = os.listdir()  # it will return the list of files present in this directory
    nManish = 0
    for item in dir_contents:
        # print(item)  # this line will print all the files name like .idea, main.py, 1.txt but i want to detect only txt file
        if item.endswith('txt'):  # this line will detect only txt files
            # print(item)
            print(f'detecting Manish in {item}: ')
            flag = isManish(item)
            if flag:
                print(f'Manish Detected in {item}')
                nManish += 1
            else:
                print(f'Manish not found in {item}')

    print("*****************Manish Detector Summary*****************")
    print(f'{nManish} files found with Manish hidden into them')
