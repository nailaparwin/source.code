####################################################################
# code to extract total energy (TOTEN)  #
####################################################################

# There are multiple folders. code will go through each folder one by
# one. read the outcar file and produce an entry (for value of energy)
# in excel sheet for each outcar file. the value of displacement is 
# same as the name of folder.
#####################################################################

import os
import pandas as pd
import xlsxwriter


x=0
#create a new excel file, the name of file is same as the name of folder
writer = pd.ExcelWriter( 'data.xlsx', engine='xlsxwriter')

# create a data set, provide header of each column
df = pd.DataFrame(columns=('Displacement', 'Energy'))

for y in range(0,11):
    if y == 10:
        folder = "1"
    elif y == 0:
        folder = "0"
    else:
        folder ="0." + str(y)

    # go inside each folder and read outcar file
    print(os.getcwd()," ",folder)
    os.chdir(folder)
    searchfile = open("OUTCAR", "r")


    # holds the total enery
    toten = ""




    # screen output
    print ("Displacement TotalEnergy ")

    # iterate each line of outcar file
    for line in searchfile:

        # extracts the number of current iteration
        if "free  energy   TOTEN" in line: 
            x = line.split(" ")
            toten=x[15]
            print(x[15])

            # appends a new line in data set
            df = df.append([{'Displacement':folder,'Energy':toten}])

 
            

    # close excel file        
    searchfile.close()

    # go outside the directory
    os.chdir("../")

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

