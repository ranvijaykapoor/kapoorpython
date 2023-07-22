import os
#os.system('notepad')
#os.system('calc')
#os.system('mkdir Ram')
#os.system('rmdir Ram')

'''for i in range(1,1000):
    path='G:\\exa\\'
    folder_name='shyam'+str(i)
    t=(path+folder_name)
    creat_folder='mkdir '+t
    os.system(creat_folder)'''

# to see current working directory
'''print(os.getcwd())
os.chdir('G:\exa')
print(os.getcwd())'''

# to see current directory items
'''os.chdir('G:\Education')
print(os.getcwd())
#print(os.listdir())
x=os.listdir()
for item in x:
    print(item)h

list = os.walk('G:\Education')
for root_path,dir,files in list:
    print("root  = ",root_path)
    print("dir=  ",dir)
    print("files= ",files)
    print()
   '''
# to harrerical foldar

#os.makedirs('ram/shyam/mohan')
#os.removedirs('ram/shyam/mohan')

# change file name

print(os.getcwd())
os.chdir('G:\exa')
print(os.getcwd())

os.rename('ram.txt','shyam.txt')