#import sys
#dir_to_look_in = [r'C:\Bib\Prod\Miniconda3-64\envs\weap-dev\Lib\site-packages',
#r'C:\Bib\Prod\Miniconda3-64\envs\statmath\Lib\site-packages',
#r'C:\Bib\Prod\Miniconda3-64\Lib\site-packages',
#r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App']
#[sys.path.append(x) for x in dir_to_look_in]
#-----------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QRadioButton, QMessageBox, QProgressBar
from PyQt5.QtWidgets import QFrame, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QTableView
#from PyQt5 import QtGui
#from PyQt5.QtGui import QPixmap
#------------------------------------------------------------------------------
import sys
import time
import datetime
#------------------------------------------------------------------------------
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
#------------------------------------------------------------------------------
from IREPS.app_functions import *
#------------------------------------------------------------------------------
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

sys.setrecursionlimit(10000000)

import subprocess
import os	

class Ui_Dialog():
    def __init__(self, Dialog, df):
        Dialog.setWindowIcon(QtGui.QIcon(r'AppIcon.png'))	
        Dialog.setWindowTitle('Data Filter')
        Dialog.setObjectName("Dialog")
        Dialog.resize(916, 339)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")        
        self.data = df
       #Header-----------------------------------------------
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText('Parameter')
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(40, 0))
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setMaximumSize(QtCore.QSize(490, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setText("Keywords to Filter")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setText('Check Unique Entries')
        self.label_6.setMinimumSize(QtCore.QSize(125, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # creating first seperation line
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        
       #--------------------------------------------------------------------------------------------------
        self.filter_dict = {variable: self.add_row_filter(variable, Dialog) for variable in self.data}

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setText('Filter')
        self.pushButton.clicked.connect(lambda: ui.return_filter_data())
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
    def add_row_filter(self, variable, Dialog):
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setText(str(variable))
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        
        self.comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox.setObjectName("comboBox")
        [self.comboBox.addItem(str(x)) for x in ['>', '>=', '<', '<=', '==', '!=', 'in', 'notin']]
        self.horizontalLayout_2.addWidget(self.comboBox)
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2.addWidget(self.frame_3)
        
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        [self.comboBox_2.addItem(str(x)) for x in self.data[variable].sort_values().unique()]
        self.comboBox_2.setMinimumSize(QtCore.QSize(125, 0))
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")        
        self.verticalLayout.addWidget(self.frame_2)
        return {'combobox':self.comboBox, 'linedit':self.lineEdit}
        
    def return_filter_data(self):
        filt_dict = {x[0]:[x[1]['combobox'].currentText(),
                       convert_to_right_datatype_to_filter(x[1]['linedit'].text())] for x in self.filter_dict.items() if x[1]['linedit'].text()!=''}
        filt_dict = {x[0]:[x[1][0], [y if not y.isdigit() else float(y) for y in x[1][1].split(', ')] if isinstance(x[1][1], str) else x[1][1]] for x in filt_dict.items()}

        self.filter_data = df_filtering(self.data, filt_dict)

class Data_Update(QDialog):
    def __init__(self):
        super().__init__()
        self.window = self
        Dialog = self
        self.setWindowIcon(QtGui.QIcon(r'AppIcon.png'))
        self.setWindowTitle('Tenders DataBase Update')
        Dialog.setObjectName("Dialog")
        Dialog.resize(861, 108)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0)) 
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        #self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setRange(0, 100)
        self.progressBar_2.setValue(0)
        #self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_3.addWidget(self.progressBar_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        self.onButtonClick_1()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        #Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Connection with server.."))
        self.label_2.setText(_translate("Dialog", "Waiting.."))
        self.label_3.setText(_translate("Dialog", "Get all zones details.."))
        self.label_4.setText(_translate("Dialog", "Get all tenders details.."))
        
                
        
    def onButtonClick_1(self):
        self.calc = External(self.label_2)
        self.calc.countChanged.connect(self.onCountChanged_1)
        self.calc.countChanged1.connect(self.onCountChanged_2)
        self.calc.start()
        self.calc.quit()                
    def onCountChanged_1(self, value):        
        if value==500:
            self.window.destroy()
            show_error_messg("Server Connection Error\n\nInternet Connectivity Issues!\nMake sure you have an active internet connection.\n\nReconnect with Internet and click on Update/Retry button to update or retry.")
            if ui._is_no_data:
                ui.label_2.setText('Connection with Server Failed')
                ui.pushButton.setText('Retry')
            ui.MainWindow.setEnabled(True)        
        else:
            self.progressBar.setValue(value)
    def onCountChanged_2(self, value):
        if value==100:
            self.window.destroy()
        elif value==1000:
            ui.finalize_updated_data()
        else:
            self.progressBar_2.setValue(value)
    def closeEvent(self, event):
        reply = QMessageBox.question(self.window, 'Quit Update', 'Update is in progress, are you sure you want to quit?',
                                     QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            
            self.window.destroy()
            event.accept()
            self.calc.terminate()
            ui.MainWindow.setEnabled(True)
        else:
            event.ignore()
class External(QThread):
    """
    Runs a counter thread.
    """
    def __init__(self, connection_label):
        super(External, self).__init__()
        self.connection_label = connection_label
    
    countChanged =  pyqtSignal(int)
    countChanged1 =  pyqtSignal(int)
    def get_main_table(self, soup):
        element= soup.find('table', id='mytable')
        a = pd.Series(element.find_all('tr', recursive=True))
        label_list = []
        for x in a.values:
            try:
                label_list.append([y.text for y in x.find_all('td')[0:3]])
            except:
                label_list.append([np.nan,np.nan, np.nan])

        url_list = []
        for x in a.values:
            try:
                url_list.append(x.find_all('td')[3].find('a').get('href'))
            except:
                url_list.append(np.nan)

        df = pd.concat([pd.Series(label_list).apply(pd.Series), pd.Series(url_list).to_frame('link')], axis=1)
        df = df.dropna(axis=0, how='all').drop(0).reset_index().drop('index', axis=1)
        df.columns = ['Sr No.','Rly zone.','Total tenders','Action']

        return df    
    def run(self):        
        try:
            self.is_data_process_done = False
            ui.MainWindow.setEnabled(False)
            url = r'https://www.ireps.gov.in/epsn/home/showTenderDetails.do?listType=nitLiveStores'
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data)
            df = self.get_main_table(soup)
            
            self.connection_label.setText('Done')
            #df = df.loc[100:200]			
           # first loop
            to_iterate = pd.Series(np.arange(0,df.shape[0]))
            to_iterate = (((to_iterate - to_iterate.min()) / (to_iterate.max()-to_iterate.min()))*100).round(1)
            url_list = []
            for perc, url in zip(to_iterate.values, df['Action'].values):
                if url is not np.nan:
                    url_list.append(get_numbers_url_for_large_page(url))
                else:
                    url_list.append(url)
                self.countChanged.emit(perc)
            df['acutal_urls'] = url_list

           #second loop
            df['acutal_urls'] = df['acutal_urls'].replace(np.nan, 'no tender')
            df1 = df.sort_values(['Rly zone.','Total tenders']).set_index(['Rly zone.','Total tenders'])['acutal_urls'].apply(pd.Series).stack().to_frame('url').reset_index()

            to_iterate = pd.Series(np.arange(0,df1.shape[0]))
            to_iterate = (((to_iterate - to_iterate.min()) / (to_iterate.max()-to_iterate.min()))*100).round(1)
            url_tender = []
            for perc, url in zip(to_iterate.values, df1['url'].values):
                if url=='no tender':
                    url_tender.append(url)
                else:
                    url_tender.append(get_zone_specific_details(url))
                self.countChanged1.emit(perc)

            df1['tender_details'] = url_tender
            df1.loc[df1['tender_details'].apply(lambda x: 'No result found..!' in x['due days'].values() if not isinstance(x, str) else False), 'tender_details'] = 'no tender'

            
            check = df1.set_index(['Rly zone.', 'Total tenders', 'level_2', 'url'])['tender_details'].apply(pd.Series).stack().apply(pd.Series).unstack().stack(0).reset_index()            
            check.rename(columns={'level_2':'pageno', 'level_4':'tender sr no'}, inplace=True)            
            check['pageno'] = check['pageno'] +1            
            check['tender sr no'] = check.groupby('Rly zone.').apply(lambda x: np.arange(1, len(x)+1)).apply(pd.Series).stack().reset_index()[0]            
            check['zone sr no'] = check['Rly zone.'].map({x:y for x, y in zip(check['Rly zone.'].unique(), np.arange(1,len(check['Rly zone.'].unique())+1))})
         
            check = check[['zone sr no']+list(check.columns[0:-1])]         
            check['link'] = check['link'].apply(lambda x: 'https://www.ireps.gov.in'+x.split('"')[1] if isinstance(x, str) and len(x)>0 else x)
            #check['link'] = check['link'].apply(lambda x: get_hyperlinked_label(x))
                     
            df_final = check.rename(columns={'zone sr no':'Zone Sr.No', 'Rly zone.':'Zone', 'Total tenders':'Total Tenders',
                               'tender sr no':'Tender Sr.No.', 'tender no':'Tender No.',
                               'type':'Tender Type', 'item':'Item', 'due date':'Due Date', 'due days':'Due Days',
                               'link':'Link'})[['Zone Sr.No', 'Zone', 'Total Tenders', 'Tender Sr.No.', 'Tender No.', 'Tender Type',
                                               'Item', 'Due Date', 'Due Days', 'Link']]
        
            df_final['Due Date'] = [pd.to_datetime(x,dayfirst=True) for x in df_final['Due Date']]        
            df_final['Due Days'] = df_final['Due Days'].replace(['No result found..!','TODAY'], [np.nan, 1]).astype(float)            
            #df_final.dropna(inplace=True)                     
            df_final.loc[df_final['Tender No.'].isnull(), ['Tender Type', 'Item', 'Link']] = 'No Tenders'     
            df_final.loc[df_final['Tender No.'].isnull(), 'Due Date'] = df_final['Due Date'].max()    
            df_final.loc[df_final['Tender No.'].isnull(), 'Due Days'] = df_final['Due Days'].max()     
            df_final.loc[df_final['Tender No.'].isnull(), 'Tender No.'] = 'No Tenders'    
            df_final[['Due Days', 'Tender Sr.No.', 'Total Tenders']] = df_final[['Due Days', 'Tender Sr.No.', 'Total Tenders']].astype(int)     
            df_final.loc[df_final['Tender No.']=='No Tenders', ['Total Tenders', 'Tender Sr.No.']] = 0
            df_final.insert(0,'Sr.No',np.arange(1,df_final.shape[0]+1,1))        
            df_final['Tender Details'] = 'Click to Open Tender Document' 
   
            df_final.to_excel(r'DB.xlsx')            
                
            self.is_data_process_done = True    
            self.updated_data = df_final    
            self.countChanged1.emit(1000)
        except:            
            ui.MainWindow.setEnabled(True)
            self.countChanged.emit(500)
						
class Tender_Details_ProgBar(QDialog):
    def __init__(self):
        super().__init__()
        self.window = self
        Dialog = self
        self.setWindowIcon(QtGui.QIcon(r'AppIcon.png'))
        self.setWindowTitle('Getting Tender Details..')		
        Dialog.setObjectName("Dialog")
        Dialog.resize(861, 10)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")        
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0)) 
        self.label_3.setText('Get Tender Details..')
        self.horizontalLayout_2.addWidget(self.label_3)
        
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
 
        self.onButtonClick_1()        
    def onButtonClick_1(self):
        self.calc = External_Detailed_ProgBar()
        self.calc.countChanged.connect(self.onCountChanged_1)
        self.calc.start()
        self.calc.quit()                
    def onCountChanged_1(self, value):        
        if value==500:
            self.window.destroy()
            show_error_messg("Server Connection Error\n\nInternet Connectivity Issues!\nMake sure you have an active internet connection.\n\nReconnect with Internet and try again.\n\nOR\n\nNo tender data to get details.")       
        elif value==100:
            self.window.destroy()
        elif value==115:
            ui.show_detailed_data()
        else:
            self.progressBar.setValue(value)
    def closeEvent(self, event):
        reply = QMessageBox.question(self.window, 'Quit Getting Tender Details', 'Update is in progress, are you sure you want to quit?',
                                     QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            
            self.window.destroy()
            event.accept()
            self.calc.terminate()
        else:
            event.ignore()
class External_Detailed_ProgBar(QThread):
    """
    Runs a counter thread.
    """
    def __init__(self):
        super(External_Detailed_ProgBar, self).__init__()
    
    countChanged =  pyqtSignal(int)
    
    def run(self):        
        try:
            self.is_data_process_done = False            
            df = ui.data
            
            if df.shape[0]==1:
                to_iterate = pd.Series(100)
            else:
                to_iterate = pd.Series(np.arange(0,df.shape[0]))
                to_iterate = (((to_iterate - to_iterate.min()) / (to_iterate.max()-to_iterate.min()))*100).round(1)
            url_list = []
            for perc, url in zip(to_iterate.values, df['Link'].values):
                try:
                    url_list.append(get_pdf_info(url))
                except:
                    url_list.append({'Tender Description':'', 'Quantity':'', 'PL Code':''})
                self.countChanged.emit(perc)
            if not all(pd.Series(url_list).apply(pd.Series)['PL Code']==''):
                df[['Tender Description', 'Quantity', 'PL Code']] = pd.Series(url_list).apply(pd.Series).set_index(df.index)[['Tender Description', 'Quantity', 'PL Code']]
                to_put_back = df[['Link', 'Tender Details']]
                df = df.drop(['Link', 'Tender Details'], axis=1)
                df[['Link', 'Tender Details']] = to_put_back

                self.is_data_process_done = True
                self.updated_data = df
                self.countChanged.emit(115)
            else:
                self.countChanged.emit(500)
        except:            
            self.countChanged.emit(500)
			
class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None  
			
class Ui_MainWindow(QMainWindow):
    def __init__(self):        
        super().__init__()
        self.MainWindow = self
        MainWindow = self
        self.setWindowIcon(QtGui.QIcon(r'AppIcon.png'))
        self.setWindowTitle('IREPS Tender DataBase Manager | ver 1.0')        
        try:
            #not_defined_1            
            self.data = pd.read_excel(r'DB.xlsx')
            ct = time.ctime(os.path.getmtime(r'DB.xlsx')).replace('  ', ' ').split(' ')
            self.file_datetime = 'File created on {}'.format(ct[0] + ', ' + ct[2]+'-'+ct[1]+'-'+ct[-1] + ' at ' + ct[3])
            self.org_data = self.data
            self._is_no_data = False
            self.col_to_show = ['Sr.No', 'Zone Sr.No', 'Zone', 'Total Tenders', 'Tender Sr.No.', 'Tender No.', 'Tender Type',
                                                   'Item', 'Due Date', 'Due Days', 'Tender Details']
        except:
            self.data = pd.DataFrame()
            self.org_data = self.data
            self._is_no_data = True
            self.col_to_show = []
            
     ## GUI layout
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText('IREPS DataBase')        
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        if self._is_no_data:
            self.label_2.setText('File created on: Unknown')
        else:
            self.label_2.setText(self.file_datetime)
        self.horizontalLayout.addWidget(self.label_2)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.data_update_status())
        self.horizontalLayout.addWidget(self.pushButton)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.incorporate_filter_window(self.data[self.col_to_show[1:-1]]))
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText('Details')
        self.pushButton_4.clicked.connect(lambda: self.get_detailed_data())
        self.horizontalLayout.addWidget(self.pushButton_4)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        
        
        
        self.tab = QtWidgets.QWidget()
        self.tab_data_dict = {}		
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableView.setLineWidth(1)
        self.tableView.setObjectName("tableView")
        self.tableView.setSortingEnabled(True)
        self.tableView.clicked.connect(self.connect_table_cell)        
        self.show_data_in_QT_table()
        self.pushButton_3.clicked.connect(lambda: self.reset_filtered_data())        
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)        
        self.tabWidget.addTab(self.tab, "Data")
        
        
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
       # Status Bar-------------------------------------------------------------------        
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        if self._is_no_data:
            self.statusbar.showMessage('')
        else:
            self.update_statusbar()
        
       # Menu Bar-------------------------------------------------------------------
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
                
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setText('Open')
        self.action_open.triggered.connect(lambda: self.open_file())
        self.menuNew.addAction(self.action_open)
        
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setText('Save')
        self.action_save.triggered.connect(lambda: self.save_file())
        self.menuNew.addAction(self.action_save)
        
        self.menuNew.addSeparator()
        
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setText('Exit')
        self.actionExit.triggered.connect(lambda: self.exit_window())
        self.menuNew.addAction(self.actionExit)

        self.menubar.addAction(self.menuNew.menuAction())

       #-----------------------------------------------------------------------------------------
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))
        #self.label_2.setText(_translate("MainWindow", "File Created on {} at {}"))
        self.pushButton.setText(_translate("MainWindow", "Update"))
        self.pushButton_2.setText(_translate("MainWindow", "Filter"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        
    def incorporate_filter_window(self, df):
        Dialog = QtWidgets.QDialog()
        ui_dialog = Ui_Dialog(Dialog, df)
        self.filter_dict = ui_dialog.filter_dict
        self.dialog_window = Dialog
        Dialog.show()
                
    def return_filter_data(self):
        try:
            filt_dict = {x[0]:[x[1]['combobox'].currentText(),
                           convert_to_right_datatype_to_filter(x[1]['linedit'].text())] for x in self.filter_dict.items() if x[1]['linedit'].text()!=''}
            filt_dict = {x[0]:[x[1][0], [y if not y.isdigit() else float(y) for y in x[1][1].split(', ')] if isinstance(x[1][1], str) and x[0]!='Tender No.' else ([k for k in x[1][1].split(', ')] if x[0]!='Due Date' else x[1][1])] for x in filt_dict.items()}
    						   
            if not len(filt_dict)==0:
                self.data = df_filtering(self.data, filt_dict).sort_values('Due Days')
                self.data['Sr.No'] = np.arange(1,self.data.shape[0]+1, 1)
                self.show_data_in_QT_table()
                self.tabWidget.setCurrentWidget(self.tab)
                self.dialog_window.close()
                self.update_statusbar()
            else:
                self.dialog_window.close()
        except:
            show_error_messg('Entries Error!\n\nInvalid Entries, Makse sure you put the right entries with right comparision symbols.\nMultiple entry must be seperated by comma followed by a space ", "')
                
    def reset_filtered_data(self):
        self.data = self.org_data
        self.show_data_in_QT_table()
        self.tabWidget.setCurrentWidget(self.tab)
        self.update_statusbar()
        
    def data_update_status(self):
        self.data_update_ui = Data_Update()
        self.data_update_ui.show()
        self.tabWidget.setCurrentWidget(self.tab)
    def closeTab(self, currentIndex):
        if not currentIndex==0:
            currentQWidget = self.tabWidget.widget(currentIndex)
            currentQWidget.deleteLater()
            self.tabWidget.removeTab(currentIndex)
    def get_detailed_data(self):
        self.Tender_Details_ProgBar = Tender_Details_ProgBar()
        self.Tender_Details_ProgBar.show()
    def show_detailed_data(self):
        if self.Tender_Details_ProgBar.calc.is_data_process_done:
            self.tab_detailed = QtWidgets.QWidget()
            self.tab_detailed.setObjectName("tab")
            self.gridLayout_detailed = QtWidgets.QGridLayout(self.tab_detailed)
            self.gridLayout_detailed.setContentsMargins(0, 0, 0, 0)
            self.gridLayout_detailed.setObjectName("gridLayout")
            self.tabWidget.addTab(self.tab_detailed, 'Detailed Data')    

            self.tableView_detailed = QtWidgets.QTableView(self.tab_detailed)
            self.tableView_detailed.clicked.connect(self.connect_table_cell)
            self.gridLayout_detailed.addWidget(self.tableView_detailed, 0, 0, 1, 1)
            self.tableView_detailed.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.tableView_detailed.setLineWidth(1)
            self.tableView_detailed.setObjectName("tableView")
            self.tableView_detailed.setSortingEnabled(True)
            self.tab_data_dict[self.tab_detailed] = self.Tender_Details_ProgBar.calc.updated_data			
            show_data_in_QT_table(self.Tender_Details_ProgBar.calc.updated_data, self.tableView_detailed)
            self.tabWidget.setCurrentWidget(self.tab_detailed)
    def open_file(self):
        self.open_file_path = QtWidgets.QFileDialog.getOpenFileName(parent=None, caption="Open File",
                                                                    directory = os.getcwd(),
                                                                    filter="excel files (*.xlsx)")
        if not self.open_file_path[0]=='':
            try:
                df = pd.read_excel(self.open_file_path[0])
                col_to_check = ['Sr.No', 'Zone Sr.No', 'Zone', 'Total Tenders', 'Tender Sr.No.',
                                'Tender No.', 'Tender Type', 'Item', 'Due Date', 'Due Days', 'Link', 'Tender Details']
                if all(df.columns == col_to_check):
                    self.data = df
                    self.org_data = df
                    self._is_no_data = False
                    self.col_to_show = ['Sr.No', 'Zone Sr.No', 'Zone', 'Total Tenders', 'Tender Sr.No.', 'Tender No.', 'Tender Type',
                                                   'Item', 'Due Date', 'Due Days', 'Tender Details']
                    self.show_data_in_QT_table()
                    self.update_statusbar() 

                    ct = time.ctime(os.path.getmtime(self.open_file_path[0])).split(' ')
                    update_datetime = 'File created on {}'.format(ct[0] + ', ' + ct[2]+'-'+ct[1]+'-'+ct[-1] + ' at ' + ct[3])
                    self.label_2.setText(update_datetime)

                else:
                    show_error_messg('File Format Error!\n\nFile is not in the right format. Make sure you load only the past saved file.')
            except:
                show_error_messg('File Format Error!\n\nFile is not in the right format. Make sure you load only the past saved file.')                
    def save_file(self):
        self.save_file_path = QtWidgets.QFileDialog.getSaveFileName(parent=None, caption="Save File",
                                                                    directory = os.getcwd(),
                                                                    filter="excel files (*.xlsx)")
        if not self.save_file_path[0]=='':
            self.data.to_excel(self.save_file_path[0])
    def exit_window(self):
        choice = QMessageBox.question(self.MainWindow, 'Exit Message!',
                                            "Are you sure you want to exit?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.MainWindow.destroy()
            subprocess.call([os.path.join(os.getcwd(), 'close_app.bat')])
        else:
            pass
    def closeEvent(self, event):
        reply = QMessageBox.question(self.MainWindow, 'Quit Message', 'Are you sure you want to quit?',
                                     QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.MainWindow.destroy()
            event.accept()
            subprocess.call([os.path.join(os.getcwd(), 'close_app.bat')])
        else:
            event.ignore()
    def update_statusbar(self):
        if not self._is_no_data:
            total_zones = self.data['Zone'].nunique()
            total_tenders = self.data.shape[0]
            try:
                tender_types = (pd.Series(self.data['Tender Type'].unique()).replace('', np.nan).dropna()+', ').sum()[:-2]
            except:
                tender_types = 0
            statusbar_messg = 'Total Zones = {} | Total Tenders = {} | Tender Type = {}'.format(total_zones, total_tenders, tender_types)
            self.statusbar.showMessage(statusbar_messg)
            
    def show_data_in_QT_table(self):
        model = pandasModel(self.data[self.col_to_show])
        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)
    def finalize_updated_data(self):
        if self.data_update_ui.calc.is_data_process_done:
            self._is_no_data = False
            self.col_to_show = ['Sr.No', 'Zone Sr.No', 'Zone', 'Total Tenders', 'Tender Sr.No.', 'Tender No.', 'Tender Type',
                                                   'Item', 'Due Date', 'Due Days', 'Tender Details']
            self.data = self.data_update_ui.calc.updated_data
            self.org_data = self.data_update_ui.calc.updated_data
            self.show_data_in_QT_table()

            ct_ = datetime.datetime.now()
            self.label_2.setText('File created on {}'.format(ct_.strftime("%a") + ', ' + ct_.strftime("%d-%b-%Y") + ' at ' + ct_.strftime("%H:%M:%S")))
            self.pushButton.setText('Update')

            self.MainWindow.setEnabled(True)            
            self.update_statusbar()
            
    def connect_table_cell(self, item):
        try:
            if self.tabWidget.currentWidget()==self.tab:
                url = self.data['Link'].iloc[item.row()]
            else:
                url = self.tab_data_dict[self.tabWidget.currentWidget()]['Link'].iloc[item.row()]
            if 'https://' in url and (item.column()==10 or item.column()==14):
                webbrowser.open(url)                
        except:
            show_error_messg('Internet Connection Error:\nMake sure you have an active internet connection.\n\nOR\n\nPDF Reader Error:\nMake sure you have a PDF reader or a web browser pdf reader plugin.')
			
			
app = QApplication(sys.argv)
ui = Ui_MainWindow()
ui.showMaximized()
try:
    subprocess.call([os.path.join(os.getcwd(), 'run_tika_server.bat')])
    if ui._is_no_data:
        ui.data_update_status()
except:
    show_error_messg("JAVA is not installed on your system OR outdated JAVA\n\nMake sure you have 1.8 or 8 version of JAVA installed.")
    ui.setWindowTitle('IREPS Tender DataBase Manager | ver 1.0 | Warning: Install JAVA v1.8 to enable Tender Details functionality.')
sys.exit(app.exec_())        