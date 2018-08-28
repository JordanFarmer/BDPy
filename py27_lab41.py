# encoding=UTF-8
import os

print os.getcwd()
dirName = u'中文_data'
os.mkdir(dirName)
os.chdir(dirName)
print os.getcwd().decode('ms950')
os.chdir('..')
os.rmdir(dirName)
print os.getcwd()