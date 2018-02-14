# Final version of code deal with both integer and decimal keys
# remaining remove .csv file
# 


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import os.path
import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
from pylab import loadtxt
import sys
import csv
import numpy
import openpyxl
import pandas as pd


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    filenames = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        #MainWindow.resize(1600, 900)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #main layout window

        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 700, 700))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))

        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))


        #line1
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))


        self.label = QtGui.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(220, 90, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout.addLayout(self.horizontalLayout)

        #line2
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))

        

        self.line = QtGui.QFrame(self.centralwidget)
        #self.line.setGeometry(QtCore.QRect(10, 150, 1500, 51))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout2.addWidget(self.line)

        

        self.verticalLayout.addLayout(self.horizontalLayout2)

        #line3
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))


        self.label_2 = QtGui.QLabel(self.centralwidget)
        #self.label_2.setGeometry(QtCore.QRect(110, 280, 191, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout3.addWidget(self.label_2) 

        self.b1 = self.btnFiles = QtGui.QPushButton(self.centralwidget)
        #self.btnFiles.setGeometry(QtCore.QRect(300, 280, 211, 27))
        self.btnFiles.setObjectName(_fromUtf8("pushButton"))
        self.b1.clicked.connect(self.getfiles)
        self.horizontalLayout3.addWidget(self.b1) 

        self.verticalLayout.addLayout(self.horizontalLayout3)


        #line4
        self.horizontalLayout4 = QtGui.QHBoxLayout()
        self.horizontalLayout4.setObjectName(_fromUtf8("horizontalLayout4"))

        self.lbl = self.lbl_file = QtGui.QLabel(self.centralwidget)
        #self.lbl_file.setGeometry(QtCore.QRect(110, 290, 800, 200))
        self.lbl_file.setObjectName(_fromUtf8("lbl_file"))
        self.horizontalLayout4.addWidget(self.lbl)

        self.verticalLayout.addLayout(self.horizontalLayout4)

################################################################

        #line5
        self.horizontalLayout5 = QtGui.QHBoxLayout()
        self.horizontalLayout5.setObjectName(_fromUtf8("horizontalLayout5"))

        self.lblx = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblx.setFont(font)
        self.lblx.setObjectName(_fromUtf8("lblx"))
        self.horizontalLayout5.addWidget(self.lblx)


        self.lineFactor = QtGui.QLineEdit(self.centralwidget)
        self.lineFactor.setInputMask(_fromUtf8(""))
        self.lineFactor.setObjectName(_fromUtf8("lineFactor"))    
        self.verticalLayout.addLayout(self.horizontalLayout5)
        self.horizontalLayout5.addWidget(self.lineFactor)
################################################################
# new code line6

        self.horizontalLayout6 = QtGui.QHBoxLayout()
        self.horizontalLayout6.setObjectName(_fromUtf8("horizontalLayout5"))

        self.lbly = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbly.setFont(font)
        self.lbly.setObjectName(_fromUtf8("lbly"))
        self.horizontalLayout6.addWidget(self.lbly)


        self.lineFactor2 = QtGui.QLineEdit(self.centralwidget)
        self.lineFactor2.setInputMask(_fromUtf8(""))
        self.lineFactor2.setObjectName(_fromUtf8("lineFactor2"))    
        self.horizontalLayout6.addWidget(self.lineFactor2)
  
        self.verticalLayout.addLayout(self.horizontalLayout6)
        




################################################################    

        #line7
        self.horizontalLayout6 = QtGui.QHBoxLayout()
        self.horizontalLayout6.setObjectName(_fromUtf8("horizontalLayout6"))

        self.lbloutput = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbloutput.setFont(font)
        self.lbloutput.setObjectName(_fromUtf8("lbloutput"))
        self.horizontalLayout6.addWidget(self.lbloutput)


        self.lineoutput = QtGui.QLineEdit(self.centralwidget)
        self.lineoutput.setInputMask(_fromUtf8(""))
        self.lineoutput.setObjectName(_fromUtf8("lineoutput"))    
        self.verticalLayout.addLayout(self.horizontalLayout6)
        self.horizontalLayout6.addWidget(self.lineoutput)

##########################################################
        #line9
        self.horizontalLayout9 = QtGui.QHBoxLayout()
        self.horizontalLayout9.setObjectName(_fromUtf8("horizontalLayout9"))
        self.lblerr = self.lbl_err = QtGui.QLabel(self.centralwidget)
        self.lbl_err.setGeometry(QtCore.QRect(110, 570, 200, 200))
        self.lbl_err.setObjectName(_fromUtf8("lbl_err"))
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        #palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white)
        self.lblerr.setPalette(palette)
        #self.lblerr.hide()
        self.lblerr.setText("")
        self.lblerr.repaint()
        #self.lblerr.show()
        self.horizontalLayout9.addWidget(self.lblerr)

        
       
        self.verticalLayout.addLayout(self.horizontalLayout9)


        #line10
        self.horizontalLayout10 = QtGui.QHBoxLayout()
        self.horizontalLayout10.setObjectName(_fromUtf8("horizontalLayout10"))

        self.b2 = self.btnOk = QtGui.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(110, 700, 211, 27))
        self.btnOk.setObjectName(_fromUtf8("pushButton"))
        self.b2.clicked.connect(self.convert)
        self.horizontalLayout10.addWidget(self.b2)


        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(210, 700, 211, 27))
        self.btnStart.setObjectName(_fromUtf8("pushButton"))
        self.btnStart.clicked.connect(self.start_addVal)
        self.horizontalLayout10.addWidget(self.btnStart)
   
       

        self.b4 =self.btnCancel = QtGui.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(390, 700, 211, 27))
        self.btnCancel.setObjectName(_fromUtf8("pushButton_2"))
        self.b4.clicked.connect(self.reset)
        self.horizontalLayout10.addWidget(self.b4)

        spacerItem = QtGui.QSpacerItem(50, 50,  QtGui.QSizePolicy.Expanding , QtGui.QSizePolicy.Minimum)
        
        self.verticalLayout.addLayout(self.horizontalLayout10)

        
        self.verticalLayout.addItem(spacerItem)

        #############

        #line11
        self.horizontalLayout11 = QtGui.QHBoxLayout()
        self.horizontalLayout11.setObjectName(_fromUtf8("horizontalLayout11"))


        self.b3 = self.btnExit = QtGui.QPushButton(self.centralwidget)
        #self.btnExit.setGeometry(QtCore.QRect(120, 750, 231, 71))
        self.b3.clicked.connect(QtCore.QCoreApplication.instance().quit)


        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnExit.setFont(font)
        self.btnExit.setAutoFillBackground(False)
        self.btnExit.setFlat(False)
        self.btnExit.setObjectName(_fromUtf8("pushButton"))

        self.horizontalLayout11.addWidget(self.b3)


        self.verticalLayout.addLayout(self.horizontalLayout11)

       

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnFiles.setText(_translate("MainWindow", "browse", None))
        self.btnOk.setText(_translate("MainWindow", "Convert only", None))
        self.btnStart.setText(_translate("MainWindow", "Add Converted Files", None))
        self.btnCancel.setText(_translate("MainWindow", "Reset", None))
        self.label.setText(_translate("MainWindow", "Tabular Data", None))
        self.label_2.setText(_translate("MainWindow", "Please select your files :", None))
        self.lbl_file.setText(_translate("MainWindow", "Files :", None))
        self.lbl_err.setText(_translate("MainWindow", "", None))
        self.btnExit.setText(_translate("MainWindow", "Exit", None))
        self.lblx.setText(_translate("MainWindow", "Multiplying Factor File1 ", None))
        self.lineFactor.setText(_translate("MainWindow", "", None))
        self.lbly.setText(_translate("MainWindow", "Multiplying Factor File2", None))
        self.lineFactor2.setText(_translate("MainWindow", "", None))
        self.lbloutput.setText(_translate("MainWindow", "Output File Name", None))
        self.lineoutput.setText(_translate("MainWindow", "", None))
 


    def getfiles(self):
        
        self.lblerr.setText("")
        self.lblerr.repaint()
        
	#'''open file dialog.'''
        dlg = QtGui.QFileDialog()
        
        dlg.setFileMode(QtGui.QFileDialog.ExistingFiles)
        #dlg.setFilter("Text files (*.txt), data files (*.dat)")
        
        if dlg.exec_():
            Ui_MainWindow.filenames = dlg.selectedFiles()
            only_name = [QtCore.QFileInfo(n).fileName() for n in Ui_MainWindow.filenames]
            x = "\n".join(only_name)
            self.lbl.setText("Files: " + "\n" + x)
            self.newfile_name(only_name)
     
    def convert(self):
        flst = Ui_MainWindow.filenames
        if len(flst)!=0:
            
            for idx in range(len(flst)):

                for col in range(1,4): #for s,ss,-ss
                    fi = QtCore.QFileInfo(flst[idx] )
                    base = fi.fileName()
                    self.runConverter(flst[idx],col)
            
        else:
            
            self.lblerr.setText("Please select some files :")
            self.lblerr.repaint()



    def start_addVal(self):
        flst = Ui_MainWindow.filenames
        if self.lineoutput.text() != "":
            if len(flst) == 2:
                if self.lineFactor.text() == "" or self.lineFactor2.text() == "":
                    self.lblerr.setText("Please give some factor values :")
                    self.lblerr.repaint()
                else:
                    factor1 = self.lineFactor.text()
                    factor2 = self.lineFactor2.text()
                    self.addVal(flst[0],flst[1],factor1, factor2)  
            else:
                self.lblerr.setText("Please select any two files :")
                self.lblerr.repaint()

        else:
            self.lblerr.setText("Please give the name of output file")
            self.lblerr.repaint() 


    def sort(self, filename):
        
        xl = pd.ExcelFile(filename + "_unsorted.xlsx")
        df = xl.parse("Sheet")
        df = df.sort(columns=0)
        cols = df.columns
        idx = df.index
        writer = pd.ExcelWriter(filename + '.xlsx')
        df.to_excel(writer,sheet_name='Sheet',columns=cols ,index=False)
        writer.save()
        os.remove(filename + "_unsorted.xlsx")


    def addVal(self,file1, file2, factor1, factor2):
        #runs using excel files as input

        #file1 = file1 + ".xlsx"
        #file2 = file2 + ".xlsx"

        xl1 = pd.ExcelFile(file1)
        df1 = xl1.parse("Sheet")
        

        xl2 = pd.ExcelFile(file2)
        df2 = xl2.parse("Sheet")
        

        resultfile =  self.lineoutput.text() + '.xlsx'
        
        idx = df1.index
        cols=df1.columns

        a = len(df1.index)
        b = len(df2.index)
        c = len(df1.columns)

                
        #code to make rows equal in both files. we will cut down the extra rows from file.

        if a < b:
            tmp = df2.reindex(index= idx[0:a], columns=cols)
            #tmp = df2.values[0:a,:]
            df = pd.DataFrame(tmp, index=idx[0:a], columns=cols)
            df.to_excel("tmp.xlsx", sheet_name='Sheet1')
            xl = pd.ExcelFile("tmp.xlsx")
            lst_df2 = xl.parse("Sheet1")
            lst_df1 = df1.values
        elif b < a:
            tmp = df1.reindex(index=idx[0:b], columns=cols)
            #tmp = df1.values[0:b,:]
            df = pd.DataFrame(tmp, index=idx[0:b], columns=cols)
            df.to_excel("tmp.xlsx", sheet_name='Sheet1')
            xl = pd.ExcelFile("tmp.xlsx")
            lst_df1 = xl.parse("Sheet1")
            lst_df2 = df2.values
        else:
            lst_df1 = df1.values
            lst_df2 = df2.values

        #performing calculation and write data on file
        data = (lst_df1*float(factor1) + lst_df2*float(factor2))/ (float(factor1) + float(factor2))
        df = pd.DataFrame(data, index=idx, columns=cols)
        df.to_excel(resultfile, sheet_name='Sheet1')
       
            
    def addVal_prev(self,file1, file2, factor1, factor2):
        #runs using csv files as input. but cannot sort data if use this file because sort also requires excel file
        filename1 = file1 
        filename2 = file2 
        
        fh1 = open(filename1, "r")
        fh2 = open(filename2, "r")
        resultfile =  self.lineoutput.text() + ".csv"
        fh3 = open(resultfile, "w")

        firstitem = True
        add_num_lst=[]
            
            

        for x,y in zip(fh1,fh2):
            
            if firstitem == True:
                fieldnames = x.split(",")
                writer = csv.DictWriter(fh3, fieldnames=fieldnames)
                writer.writeheader()
                firstitem = False
                
                continue
            args1=x.split(",")
            
            args2=y.split(",")
            obj = {}
            obj[fieldnames[0]] = args1[0]
            if args1[0] == args2[0]:
                print("ok")
            else:
                print("error")
            
            for v in range(1, len(args1)):
 
                obj[fieldnames[v]] = (float(factor1)*float(args1[v])+ float(factor2)*float(args2[v]))/(float(factor1)+float(factor2))

            writer.writerow(obj)
            





    def runConverter(self,base, col_no):
        filename = base
        alphaValues = []
        lst = []
        betaValues = []
        fieldname = []

        with open(filename ,"r") as f:       
            for line in f:
                tmp = line
                words = tmp.split()
                if len(words)!=0:
                    if words[0].startswith('alpha'):
                        alphaValues.append(lst)
                        lst = []
                        #fieldnames are values in top row
                        fieldname.append(words[1])
                        lst.append("alpha= " + words[1])
                    elif words[0][0].isdigit():
                        flag = True
                        #betaValues are keys in the left column
                        for i in betaValues:
                            if i == words[0]:
                                flag = False
                        if flag == True:
                            betaValues.append(words[0])
#################################################ss(a,b) = 2, ss(a,-b)= 3, default = 1 #######################

                        lst.append(float(words[col_no]))

        #to append the last list
        alphaValues.append(lst)

        fname = filename + "_upd.csv"
        with open(fname , 'w') as csvoutput:
            ## 000 is replaced for beta because it needs to convert into float later
            fieldnames = ['000']
            writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
            writer.writeheader()
    
    
            for i in betaValues:
                writer.writerow({'000':i})
        
        #################################       
        # to make all sub lists of equal length

        max = 10
        for i in alphaValues:
            if len(i) > max:
                max = len(i)
        
        for i in alphaValues:
            while len(i) < max:
                i.append(0)
        

########## append a new column #############
        oldfile = ''
        newfile = fname
        fileCounter = 0
        alphaValuesIter = 1

        for alpha in fieldname:
            #print (alpha)
            if alpha == '000':
                continue

            fileCounter = fileCounter+1
            if os.path.exists(oldfile):
                os.remove(oldfile)
            oldfile = newfile
            #newfile = newfile + '0'
            newfile = str(fileCounter) + '.csv'
    
            with open(oldfile ,'r') as csvinput:
                with open(newfile , 'w') as csvoutput:
                    writer = csv.writer(csvoutput)
                    reader = csv.reader(csvinput)
                    xrow = 0
                    all = []
                    row = next(reader)
            
                    row.append(alpha)
                    all.append(row)

                    #to break each lst inside alphaValues list
           
                    items = str(alphaValues[alphaValuesIter]).strip('[]')
                    item = items.split(",")

                    #print (item[0])

                    for row in reader:
                        xrow = xrow + 1

                        row.append(item[xrow])
                        all.append(row)

                    writer.writerows(all)
                    alphaValuesIter = alphaValuesIter  + 1

        if col_no == 1:
            filename = filename + "s(a,b).csv"
        elif col_no ==2:
            filename = filename + "ss(a,b).csv"
        else:
            filename = filename + "ss(a,-b).csv"
        os.rename(newfile, filename)

           
        self.csv_to_xlsx(filename)
        self.sort(filename)   



    def csv_to_xlsx(self, filename):
        f = open(filename)
        wb = openpyxl.Workbook()
        ws = wb.active
        reader = csv.reader(f, delimiter=',')
        for i in reader:
            try:
                i[0:] = [float(x) for x in i[0:]]
                ws.append(i)
            except ValueError:
                ws.append(i)

        f.close()
        wb.save(filename + "_unsorted.xlsx")
        os.remove(filename)




    def insertcol(self, betaValues, fieldname, filename):        

        fname = filename + "_upd.csv"
        

	########## append a new column #############
        
        oldfile = ''
        newfile = fname
        fileCounter = 0
        alphaValuesIter = 1

        for alpha in fieldname:
            
            fileCounter = fileCounter+1
            if os.path.exists(oldfile):
                os.remove(oldfile)
            oldfile = newfile
            
            newfile = str(fileCounter) + '.csv'
            try:
                with open(oldfile ,'r') as csvinput:
                    with open(newfile , 'w') as csvoutput:
                        writer = csv.writer(csvoutput)
                        reader = csv.reader(csvinput)
                        xrow = 0
                        all = []
                        row = next(reader)
                        row.append(alpha)
                        all.append(row)
                        
		        #to break each lst inside alphaValues list
		   
                        item =betaValues

                        for row in reader:
                            xrow = xrow + 1

                            row.append(item[xrow])
                            all.append(row)

                        writer.writerows(all)
                        alphaValuesIter = alphaValuesIter  + 1

                filename = filename + "_update.csv"
                os.rename(newfile, filename)
        
                self.csv_to_xlsx(filename, heading1, heading2)
	
            except:
                print (sys.exc_info()[0])



    def newfile_name(self, names_of_files):
        fn = ""
        fn = fn + names_of_files[0][3:-4]
        for f in names_of_files:
            fn = f[0:3] + fn  
        fn = fn + ".png"
        


    def reset(self):
        self.lbl.setText("Files: ")
        Ui_MainWindow.filenames=""
        self.lineFactor.setText("")
        self.lineFactor2.setText("")
        self.lineoutput.setText("")
        self.lblerr.setText("")
        self.lblerr.repaint()

        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    screen = app.desktop().screenGeometry()
    width, height = screen.width(), screen.height()
    
    MainWindow.setGeometry(0,0, width, height)
    MainWindow.setWindowTitle("Files Converter")
    MainWindow.show()
    #MainWindow.showMaximized()
    sys.exit(app.exec_())





