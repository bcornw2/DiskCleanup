import os.path, os, glob, shutil

path_to_parent = 'C:\\Users\\'
downloads = 'Downloads'
dirList = []
ans = ''

print(os.name)
os.chdir(path_to_parent)
print(os.getcwd())
dirList = glob.glob(path_to_parent+'\*\\'+downloads)
print(dirList)


ans = input('Do you want to empty downloads? (y/n)')
while ans.lower() != 'n':
    for i in range(len(dirList)):
        os.chdir(dirList[i])
        path = os.getcwd()
        print('This will delete all items and fodlers in \Downloads of each user')
        try:
            if os.path.isfile(path):
                os.unlink(path)
            elif os.path.isdir(path): shutil.rmtree(path)
        except Exception as e:
            print(e)
    print('Completed. Thank you!')
    break
print('No deletions or modifications made. Goodbye')

# This is a script which will delete the contents
#of all the Downloads folders (included sub-folders
# and their content) under every user, in C:\Users,
#but only enter those directories if the
#  C:\Users\$USER\ profile contains a directory
#named "Downloads" (case-sensitive). This can be
#modified to work on Linux too (/home/$USER/Downloads
#with a single if: statement but since all of our
#alerts are from Windows servers, this should work
#just fine. This script will work for all DCs because
#the script runs independently of domain admin username
#
#This can be modified to clear out any problem directory
#for any server.
#
#NOTE: I can modify this to self-elevate to a local administrator
#if necessary. I am not sure how RMM works with deploying
#scripts. Additionally, with minimal changes I could make this
#into an executable .exe file. I will need to learn how the default
#script settings work in RMM
#
#
#created by Ben Cornwell
