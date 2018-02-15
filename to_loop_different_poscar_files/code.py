############################################################################
#
#############################################################################

import os
from shutil import copyfile


b = 0.40
for j in range(11):
    a = 0.40
    for i in range(11):
        drname = str('%4.2f' %b) + "_" + str('%4.2f' %a)
        #print ("make dir" + str('%4.2f' %a))
        #os.makedirs(str('%4.2f' %a))
        #print ("make dir" + drname)
        os.makedirs(drname)
        ftoread = open("POSCAR")
    
        os.chdir(drname)
        copyfile("../INCAR","./INCAR" )
        copyfile("../POTCAR","./POTCAR" )
        copyfile("../KPOINTS","./KPOINTS" )
        ftowrite = open("POSCAR", "w")
        for line in ftoread:
            if "xxxxxxxxxx" in line:
                ftowrite.write("       " + str('%11.8f' %b)+ str('%11.8f' %a)+ " 0.50000000\n")
            else:
                ftowrite.write(line)
        ftoread.close()
        ftowrite.close()
        os.chdir("../")
        a = a+0.02
    b = b+ 0.02

