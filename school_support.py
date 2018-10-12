#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#


import sys
import pandas as pd
import numpy as np
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

'''Generate the var we may neeed'''
def set_Tk_var():
    global list1
    list1 = StringVar()
    global input
    input = StringVar()
    global list2
    list2 = StringVar()
    global list3
    list3 = StringVar()
    global list4
    list4 = StringVar()

'''print information about different cluster'''
def button1():
    print('school_support.button1')
    for i in range(30):
        w.Listbox1.insert(0,"")
    w.Listbox1.insert(0,("          % Advanced     % Proficient  % Basic  % Below Basic  Conduct OSS"))
    w.Listbox1.insert(1,("Cluster1  25.05          39.52         23.66    11.76          1.43"))
    w.Listbox1.insert(2,("Cluster2  3.71           18.29         31.92    46.06          13.94"))
    w.Listbox1.insert(3,("Cluster3  13.24          33.51         30.88    22.35          4.35"))
    w.Listbox1.insert(4,("Cluster4  2.41           13.58         31.61    52.38          56.46"))
    w.Listbox1.insert(5,("Cluster5  41.52          38.28         14.74    5.45           0.47"))
    sys.stdout.flush()


'''Show Information on listbox3'''
def combolist():
    print('school_support.combolist')
    for i in range(30):
        w.Listbox3.insert(0,"")
    cluster = list3.get()
    if cluster == "":
        cluster = "Cluster1"
    if cluster =='Cluster1':
        df=pd.read_csv("files/Cluster1.csv")
    if cluster =='Cluster2':
        df=pd.read_csv("files/Cluster2.csv")
    if cluster =='Cluster3':
        df=pd.read_csv("files/Cluster3.csv")
    if cluster =='Cluster4':
        df=pd.read_csv("files/Cluster4.csv")
    if cluster =='Cluster5':
        df=pd.read_csv("files/Cluster5.csv")
    npdf = np.array(df)#np.ndarray()
    list=npdf.tolist()#list
    for i in range(len(list)):
        w.Listbox3.insert(0,("School Name: "+list[i][4]))
        w.Listbox3.insert(1,("County Name: "+list[i][3]))
        w.Listbox3.insert(2,"")

'''Get information from the cluster and county that user chooses'''
def button2():
    for i in range(30):
        w.Listbox2.insert(0,"")
    
    if list3.get()=='Cluster1':
        df=pd.read_csv("files/Cluster1.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
            
    if list3.get()=='Cluster2':
        df=pd.read_csv("files/Cluster2.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    if list3.get()=='Cluster3':
        df=pd.read_csv("files/Cluster3.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    if list3.get()=='Cluster4':
        df=pd.read_csv("files/Cluster4.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    if list3.get()=='Cluster5':
        df=pd.read_csv("files/Cluster5.csv")
        npdf = np.array(df)#np.ndarray()
        list=npdf.tolist()#list
        row=0
        for i in range(len(list)):
            if list[i][3].lower()==input.get().lower():
                w.Listbox2.insert(row,("School Name: "+list[i][4]))
                row=row+1
        
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import school
    school.vp_start_gui()


