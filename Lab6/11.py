# Directories and Files  ex6
import string
for i in string.ascii_uppercase:
   with open(i + ".txt", "w") as a:
       a.writelines(i)