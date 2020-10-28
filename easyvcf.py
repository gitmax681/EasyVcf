# imports random time os and sys modules
import sys
import random
import time
import os
# referance the variable Name
Name = 0
raw = 0

# define varibles with ascii color code for easy access

mb = '\033[1;35m'
cb = '\033[1;36m'
rb = '\033[1;31m'
gb = '\033[1;32m'
yb = '\033[1;33m'
wb = '\033[1;37m'

#defining the list for the generating animation
animation = ["Generating [■□□□□□□□□□]", "gEnerating [■■□□□□□□□□]",
             "geNerating [■■■□□□□□□□]", "genErating [■■■■□□□□□□]",
             "geneRating [■■■■■□□□□□]", "generAting [■■■■■■□□□□]",
             "generaTing [■■■■■■■□□□]", "generatIng [■■■■■■■■□□]",
             "generatiNg [■■■■■■■■■□]", "generatinG [■■■■■■■■■■]"]

# collects the path of the file and opens in read mode
os.system('clear')
number_path = input(f'{yb}Enter The path of The File: {rb}')
fb = open(number_path, "r+")
number = fb.readlines()

# this fucntion is to generate vcf with random 8letter name


def write():
    alphabets = list('qwertyuiopasdfghjklzxcvbnm')
    a = random.choice(alphabets)
    b = random.choice(alphabets)
    c = random.choice(alphabets)
    d = random.choice(alphabets)
    e = random.choice(alphabets)
    f = random.choice(alphabets)
    g = random.choice(alphabets)
    h = random.choice(alphabets)
    name = a+b+c+d+e+f+g+h
    for i in number:
        if len(i) == 11:
            content = f"""
BEGIN:VCARD
VERSION:2.1
N:;{name};;;
FN:{name}
TEL;CELL;PREF:{i}END:VCARD"""
            with open('numbers.vcf', 'a+') as f:
                f.write(content)

# this fucntion is to generate vcf with name as numbers in increasing order


def write_2():
    for i in number:
        global Name
        Name += 1
        if len(i) == 11:
            content = f"""
BEGIN:VCARD
VERSION:2.1
N:;{Name};;;
FN:{Name}
TEL;CELL;PREF:{i}END:VCARD"""
            with open('numbers.vcf', 'a+') as f:
                f.write(content)

# this function is to generate vcf with name provided by the user individually


def write_3():
    global raw
    for i in number:
        if len(i) == 11:
            raw += 1
            Name = input(
                f'{wb}{raw}:- {yb}Enter The Name For Number: {rb}{i}>>{yb}')
            content = f"""
BEGIN:VCARD
VERSION:2.1
N:;{Name};;;
FN:{Name}
TEL;CELL;PREF:{i}END:VCARD"""
            with open('numbers.vcf', 'a+') as f:
                f.write(content)


# programm starts here
os.system('figlet -f big \'EasyVcf\' |lolcat')
print(f"""
{gb}-------------------------------------
{cb}[{mb}1{cb}]{yb} Use Random Alphabets As Name
{cb}[{mb}2{cb}]{yb} Use Increasing No. As Name
{cb}[{mb}3{cb}]{yb} Provide A Coustom Name
{cb}[{mb}4{cb}]{yb} Exit
{gb}-------------------------------------""")
# takes main input and call the function according to the user input
while True:
    try:
        Input = int(input(f'{wb}>>'))
        if Input == 1:
            write()
            break
        elif Input == 2:
            write_2()
            break
        elif Input == 3:
            write_3()
            break
        elif Input == 4:
            exit()
        else:
            print(f'{rb}Invalid input')

    except Exception as e:
        print(e)

for i in range(len(animation)):
    time.sleep(0.35)
    sys.stdout.write(f"{yb}\r" + animation[i % len(animation)])
    sys.stdout.flush()
print(f'{gb}\nsuccessfully created your vcf')

