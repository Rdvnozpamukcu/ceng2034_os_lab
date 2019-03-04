import os

home = os.getenv("HOME")
os.chdir(home)
os.mkdir('os_lab_0')

os.chdir('os_lab_0')

os.system("touch selam.txt benridvan.txt 0.py")
os.system('ls -lt')
print(os.system('ls *txt'))l.
