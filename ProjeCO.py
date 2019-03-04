import os

home = os.getenv("HOME")
os.chdir(home)
os.mkdir('os_lab_0')

os.chdir('os_lab_0')

os.system("touch 2.txt 3.txt 1.py")
os.system('ls -lt')
print(os.system('ls *txt'))l.