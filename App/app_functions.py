#import sys
#dir_to_look_in = [r'C:\Bib\Prod\Miniconda3-64\envs\weap-dev\Lib\site-packages',
#r'C:\Bib\Prod\Miniconda3-64\envs\statmath\Lib\site-packages',
#r'C:\Bib\Prod\Miniconda3-64\Lib\site-packages',
#r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App']
#[sys.path.append(x) for x in dir_to_look_in]
#-----------------------------------------------------------------------------------

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import bs4 as bs
import sys
sys.setrecursionlimit(10000000)
#------------------------------------------------------------------------------
import urllib3
from bs4 import BeautifulSoup
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
import certifi
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
#------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import os
import time
import webbrowser
import sys
sys.path.append(r'C:\Bib\Prod\Miniconda3-64\envs\weap-dev\Lib\site-packages')
import requests
from tika import parser
#------------------------------------------------------------------------------
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QAbstractTableModel, Qt
#------------------------------------------------------------------------------
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")




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

def ext_data(a):
    return pd.Series(a.split('</td>')).apply(lambda x: x.split('>')[-1] if not 'href' in x else x.split('href=')[-1].split('>')[0])
def ext_data_level1(a):
    return pd.Series(a.split('</td>')).apply(lambda x: x.split('>')[-1] if not 'href' in x else x.split('href=')[-1].split('>'))

def get_zone_specific_details(url_zone):    
    response = http.request('GET', url_zone)
    soup1 = BeautifulSoup(response.data)
    if 'pageNo=' in url_zone:
        a = pd.Series(str(soup1.find_all('table')[4]).split('<tr>')).apply(lambda x: ext_data_level1(x).apply(lambda x: [x.split('\r\n\t\t\t\t\t\t\t')[-1].split('\r\n\t\t\t')[0]] if not isinstance(x, list) else [x[0], x[1].split('<')[0]]).apply(pd.Series).stack()).T.reset_index().T[[2,3,4,5,6,7,8]].dropna(subset=[4]).drop(['level_0', 'level_1']).reset_index().drop('index', axis=1)
    else:
        a = pd.Series(str(soup1.find_all('table')[4]).split('<tr>')).apply(lambda x: ext_data_level1(x).apply(lambda x: [x.split('\r\n\t\t\t\t\t\t\t')[-1].split('\r\n\t\t\t')[0]] if not isinstance(x, list) else [x[0], x[1].split('<')[0]]).apply(pd.Series).stack()).T.reset_index().T[[1,2,3,4,5,6,7]].dropna(subset=[3]).drop(['level_0', 'level_1']).reset_index().drop('index', axis=1)
    a.columns = ['zone', 'link', 'tender no', 'item', 'type', 'due date', 'due days']
    a.reset_index().drop('index', axis=1, inplace=True)
    return a.to_dict()
def get_numbers_url(url_zone):
    try:        
        response = http.request('GET', url_zone)
        soup1 = BeautifulSoup(response.data)
        return [x.split(' ')[0].replace('amp;','').replace('"', '') for x in (pd.Series(str(soup1.find_all('table')[4]).split('<tr>')).apply(lambda x: x if x.startswith('<td align="right" colspan="8"><a href') else np.nan).dropna().iloc[0].split('href='))][1:]
    except:
        return [url_zone]
def get_numbers_url_for_large_page(url):
    a = get_numbers_url(url)
    try:
        if int(a[-1].split('=')[-1])>25:
            a = a+get_numbers_url(a[-1])[2:]
        else:
            None
        return a
    except:
        return a
		
def show_data_in_QT_table(df, table_widget):
    model = pandasModel(df)
    table_widget.setModel(model)
    table_widget.setSortingEnabled(True)    
def convert_to_right_datatype_to_filter(x):
    if any(y.isalpha() for y in x) or all(y.isdigit() for y in x.replace('.','').replace(', ','')):
        return x
    elif '/' in x or '-' in x:
        return pd.to_datetime(x,dayfirst=True)
    elif all(y.isdigit() for y in x.replace('.','')):
        return float(x)
    else:
        return np.nan
def check_str(check_with, to_check):
    check_with = check_with.lower().replace('\n','').split(' ')
    to_check = to_check.lower().replace('\n','').split(' ')
    return all(any(x in y for y in check_with) for x in to_check)    
def df_filtering(df, filters_dict, return_other=False):
    """
    filtering any df from filter defined by a filters dictionnary

    Parameters
    ----------
    df : pandas dataframe
        input data
    filters_dict : dictionnary defining filter
      take this form {'column1': ['==', 'a'],
                      'column2': ['!=', ['a', 'b']],
                      'column3': ['>', 2.3],
                      'column4': ['<=', 2.3]}
                    or list of filters_dict
    Returns
    -------
    df : pandas dataframe
        the corresponding filtered dataframe

    """
    # TODO consistency of dict keys.
    if filters_dict is None:
        return df
    else:
        ok = np.ones((len(df)), dtype=bool)

        if not isinstance(filters_dict, list):
            filters_dict_list = [filters_dict]
        else:
            filters_dict_list = filters_dict

        for filters_dict in filters_dict_list:

            for i, key in enumerate(filters_dict.keys()):

                # force type list..
                if not hasattr(filters_dict[key][1], '__iter__'):
                    filters_dict[key][1] = [filters_dict[key][1]]

                if filters_dict[key][0] == '==':
                    ok_ = np.zeros((len(df)), dtype=bool)
                    for val in filters_dict[key][1]:
                        ok_ += df[key] == val
                    ok *= ok_

                elif filters_dict[key][0] == '!=':
                    ok_ = np.zeros((len(df)), dtype=bool)
                    for val in filters_dict[key][1]:
                        ok *= df[key] != val
                    ok *= ok_

                elif filters_dict[key][0] == '>':
                    for val in filters_dict[key][1]:
                        ok *= df[key] > val

                elif filters_dict[key][0] == '<':
                    for val in filters_dict[key][1]:
                        ok *= df[key] < val

                elif filters_dict[key][0] == '>=':
                    for val in filters_dict[key][1]:
                        ok *= df[key] >= val

                elif filters_dict[key][0] == '<=':
                    for val in filters_dict[key][1]:
                        ok *= df[key] <= val

                elif filters_dict[key][0] == 'in':
                    #ok *= df[key].isin(filters_dict[key][1])
                    ok_ = np.zeros((len(df)), dtype=bool)
                    for val in filters_dict[key][1]:
                        ok_ += df[key].astype(str).apply(lambda x: check_str(x, val))
                    ok *= ok_
                
                elif filters_dict[key][0] == 'notin':
                    #ok *= (-df[key].isin(filters_dict[key][1]))
                    ok_ = np.zeros((len(df)), dtype=bool)
                    for val in filters_dict[key][1]:
                        ok_ += (-df[key].astype(str).apply(lambda x: check_str(x, val)))
                    ok *= ok_

                else:
                    warnings.warn('{} is not a known comparison symbol'.format(filters_dict[key][0]))

        if return_other:
            return df.ix[ok, :], df.ix[-ok, :]
        else:
            return df.ix[ok, :]    
def filter_data(data, col, to_filter):
    data['item_to_search'] = data[col].astype(str).replace(np.nan, 'nan').apply(lambda x: x.lower().replace(' ', '').replace(',','').replace('/',''))
    return data[data['item_to_search'].apply(lambda x: to_filter in x)].sort_values('due date').drop('item_to_search', axis=1)  
def print_something():
    print('It is working....!!')
     
def show_error_messg(set_text):
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    app.references = set()
    msg = QMessageBox()
    msg.setWindowIcon(QtGui.QIcon(r'AppIcon.png'))	
    msg.setIcon(QMessageBox.Critical)
    msg.setText(set_text)
    msg.setWindowTitle("Error")
    msg.show()
    app.references.add(msg)
def get_pdf_info(url):
    r = requests.get(url)
    with open(r"tender_downloaded.pdf",'wb') as f: 
        f.write(r.content) 
    raw = parser.from_file(r"tender_downloaded.pdf")
    desciption = raw['content'].split('Description')[1].split('Consignee')[0].replace('\n', '').replace(' :', '')
    
    quantity = [x for x in raw['content'].split('Description')[1].split('Consignee')[-1].split('\n\n') if any(char.isdigit() for char in x)][0]
    quantity = quantity[[ind for y, ind in zip(quantity, range(len(quantity))) if y.isdigit()][0]:]
    
    plcode = raw['content'].split('ITEM DETAILS')[-1].split('Description')[0].split('\n\n')[-2].split(' ')[1]
    return {'Tender Description':desciption, 'Quantity':quantity, 'PL Code':plcode}
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		