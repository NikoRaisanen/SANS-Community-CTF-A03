#! python
# Challenge A03 from SANS Community CTF

import sys

print("\n\nWelcome to my Sign and Magnitude to Binary Converter!\n")
print("Example usage: 'python SM2BinaryConverter.py \"String To Be Converted\"'")
print("\n[+] IMPORTANT - Make sure to enclose the string that you would like converted in double quotes!\n")

serverOutput = sys.argv[1]
outputList = serverOutput.split(" ")
individualBinary = ""
binaryList = []

for number in outputList:
    if "-" in number:
        #  make MSD as "1" to signify negative
        individualBinary = individualBinary + "1"
        number = number.replace("-","")
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 64:
        individualBinary = individualBinary + "1"
        number = int(number) - 64
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 32:
        individualBinary = individualBinary + "1"
        number = int(number) - 32
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 16:
        individualBinary = individualBinary + "1"
        number = int(number) - 16
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 8:
        individualBinary = individualBinary + "1"
        number = int(number) - 8
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 4:
        individualBinary = individualBinary + "1"
        number = int(number) - 4
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 2:
        individualBinary = individualBinary + "1"
        number = int(number) -2
    else:
        individualBinary = individualBinary + "0"

    if int(number) >= 1:
        individualBinary = individualBinary + "1"
        number = int(number) - 1
    else:
        individualBinary = individualBinary + "0"

    binaryList.append(individualBinary)

    #  Resets individualBinary string to process next 8 bits
    individualBinary = ""

finalBinary = " ".join(binaryList)

print("\n\n\n[+] Conversion from sign-magnitude to 8 bit binary completed!\nThe output can be seen below:\n")
print(finalBinary)