import os
print("1 .press 1 for Shutdown ")
print("1 .press 2 for Restart ")
print("3. press 3 for exit")
option=int(input("\n enter your choice"))
if option >= 1 and option<=1:
    if option==1:
        os.system("shutdown /s /t 1")
    else:

        os.system("shutdown /r /t 1")
else:
    exit()