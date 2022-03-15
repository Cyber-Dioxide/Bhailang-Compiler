import sys
import os
import platform
from binaries import binaries

def clr_sc():
    if "Windows" in platform.platform():
        os.system("cls")

    else:
        os.system("clear")

file = sys.argv[1]

binaries.version()

print("\n--- Compiling".center(50))



def input_to_exit(str):
    input(f"\n{str} \n")


def cheking_file(file):
    ffile = file.split(".")
    if ffile[1] == "bhailang" :
        print(f"--- {file} is valid!")

    if file[1] == "BHAILANG":
        print(f"--- {file} is valid!")

    # if file[1] != "BHAILANG" or "bhailang":
    #     print(f"--- {file} is not a valid file! ")
    #     input_to_exit()

cheking_file(file=file)


input_to_exit("Press Enter to see the output!")
clr_sc()

def compiler(file):

    file_lines = open(file , "r+")
    l_no = 0
    for line in file_lines:
        l_no += 1
        if line.startswith("bol bhai"):
            start , content = line.split("bol bhai")
            print(content)
            # with open(f"{file.split('.')[0]}.py" , "a+") as writer:
            #     writer.write(f"print('{content}')")


        # if line.startswith("agar"):
        #     start , content = line.split("agar")
        #     with open(f"{file.split('.')[0]}.py" , "a+") as writer:
        #         writer.write(f"\nif {content}")

        # os.system(f"py -3 {file.split('.')[0]}.py")



compiler(file=file)







