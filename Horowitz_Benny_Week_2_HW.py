#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Benny Horowitz Homework Week two 2/2/2021
"""
import os
os.chdir(r"C:\Users\benny\OneDrive\Desktop\TAMU Sruff\Week 3 - Feb 2")
import requests, json 
import pandas as pd
import numpy  as np
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning

import matplotlib.pyplot as plt
from PIL import ImageTk, Image

from tkinter import Tk, Frame, Button, Canvas



from PIL import Image
filename = 'Benny Horowitz Professional Portrait.jpg'
img = Image.open(filename)
img.save('Horowtiz_Benjamin.ico')

class StockGUI:
    def __init__(self, guiWin, api_key):
        self.guiWin_ = guiWin
        self.guiWin_.title("Bennys Stock Price")
        self.guiWin_.iconbitmap('Horowtiz_Benjamin.ico')
        self.guiWin_.geometry("375x450")
        self.guiWin_.configure(bg='LightSkyBlue')
        self.api_key = api_key
                      
        # Declares root canvas is a grid of only one row and one column
        self.guiWin_.columnconfigure(4, weight=0)
        self.guiWin_.rowconfigure(3, weight=0)
        
        # Create 4 Frames inside GUI canvas
        self.mainframe = ttk.Frame(self.guiWin_, padding="5 5 5 5", relief=SUNKEN)
        self.mainframe.grid(column=1, row=1,columnspan=2, sticky=(N, W, E, S))
        # Create second Frame inside GUI canvas
        self.mainframe2 = ttk.Frame(self.guiWin_, padding="5 5 5 5", relief=SUNKEN)
        self.mainframe2.grid(column=3, row=1,columnspan=2,sticky=(N, W, E, S))
        
        self.mainframe3 = ttk.Frame(self.guiWin_, padding="5 5 5 5", relief=SUNKEN)
        self.mainframe3.grid(column=1, row=2,columnspan=4, sticky=(N, W, E, S))
        
        self.mainframe4 = ttk.Frame(self.guiWin_, padding="5 5 5 5", relief=SUNKEN)
        self.mainframe4.grid(column=1, row=3,columnspan=4, sticky=(N, W, E, S))
        
##############################################################################
#                 MAINFRAME 1                                   ##############        
##############################################################################  
        # Set styles for TK Label, Entry and Button Widgets

        col2wdt = 16
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial",  10),foreground='blue2')
        # Create Label Widgets Inside mainframe
        ttk.Label(self.mainframe, text="Symbol", width=col2wdt).grid(column=1,row=1, sticky=W)
        ttk.Label(self.mainframe, text="Close Price (USD)", width=col2wdt). \
                                              grid(column=1, row=2, sticky=W)
        ttk.Label(self.mainframe, text="Previous Close"). \
                                              grid(column=1, row=3, sticky=W)
        ttk.Label(self.mainframe, text="Percent Change"). \
                                              grid(column=1, row=4, sticky=W)
        ttk.Label(self.mainframe, text="Volume"). \
                                              grid(column=1, row=5, sticky=W)
        
        # Create Entry Widgets Inside Mainframe
        self.style.configure("TEntry", font=("Arial",  12),foreground='blue2')
        col2wdt = 10

        # Add Entry Widget for Display of Stock Symbol           
        self.symbol = StringVar()
        self.get_symbol = ttk.Entry(self.mainframe, width=col2wdt, 
                                textvariable=self.symbol, justify=CENTER)
        self.get_symbol.grid(column=2, row=1, sticky=(W, E))
          
        # Add Entry Widget for Display of the Last Stock Close Price           
        self.close_price = StringVar()
        self.close_price_entry = ttk.Entry(self.mainframe, width=col2wdt, 
                                textvariable=self.close_price, justify=CENTER)
        self.close_price_entry.grid(column=2, row=2, sticky=(W, E))
        
        # Add Entry Widget for Display of the Previous Stock Close Price
        self.p_close_price = StringVar()
        self.p_close_price_entry = ttk.Entry(self.mainframe, width=col2wdt, 
                              textvariable=self.p_close_price, justify=CENTER)
        self.p_close_price_entry.grid(column=2, row=3, sticky=(W, E))
        
        # Add Entry Widget for Display of the Percent Change in Price
        self.change = StringVar()
        self.change_entry = ttk.Entry(self.mainframe, width=col2wdt, 
                                     textvariable=self.change, justify=CENTER)
        self.change_entry.grid(column=2, row=4, sticky=(W, E))
        
        # Add Entry Widget for Display of Trading Volume for Last Day
        self.vol = StringVar()
        self.vol_entry = ttk.Entry(self.mainframe, width=col2wdt, 
                                        textvariable=self.vol, justify=CENTER)
        self.vol_entry.grid(column=2, row=5, sticky=(W, E))

##############################################################################
#                 MAINFRAME 2                                   ##############
##############################################################################
        self.a = IntVar()
        self.a.set(0)
        self.a1 = ttk.Checkbutton(self.mainframe2, text="Apple", 
                                  variable=self.a, command=self.stock_close1, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=1, sticky=W)                          

        self.f = IntVar()
        self.f.set(0)
        self.f1 = ttk.Checkbutton(self.mainframe2, text="Ford", 
                                  variable=self.f, command=self.stock_close2, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=2, sticky=W)                         
        self.gm = IntVar()
        self.gm.set(0)
        self.gm1 = ttk.Checkbutton(self.mainframe2, text="General Motors", 
                                  variable=self.gm, command=self.stock_close3, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=3, sticky=W)
        self.g = IntVar()
        self.g.set(0)
        self.g1 = ttk.Checkbutton(self.mainframe2, text="Google", 
                                  variable=self.g, command=self.stock_close4, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=4, sticky=W)
        self.t = IntVar()
        self.t.set(0)
        self.t1 = ttk.Checkbutton(self.mainframe2, text="Tesla", 
                                  variable=self.t, command=self.stock_close5, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=5, sticky=W)
        self.i = IntVar()
        self.i.set(0)
        self.i1 = ttk.Checkbutton(self.mainframe2, text="IBM", 
                                  variable=self.i, command=self.stock_close6, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=6, sticky=W)
        self.fb = IntVar()
        self.fb.set(0)
        self.fb1 = ttk.Checkbutton(self.mainframe2, text="Facebook", 
                                  variable=self.fb, command=self.stock_close7, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=1, row=7, sticky=W)

        
##############################################################################
#                 MAINFRAME 3                                   ##############
##############################################################################

        ttk.Separator(self.mainframe3, orient=HORIZONTAL).\
                               grid(column=1, row=1, columnspan=4, sticky="EW")
                                              
        ttk.Label(self.mainframe3,text="Last 100 Days"). \
                                              grid(column=1, row=2, sticky='NW')
        
        
        # Create Checkbutton Widgets Inside mainframe
        self.style.configure("TCheckbutton",font=("Arial", 10),
                             foreground='blue2')
        self.c = IntVar()
        self.c.set(0)
        self.c1 = ttk.Checkbutton(self.mainframe3, text="Closing Price", 
                                  variable=self.c, command=self.plt_close, 
                                  onvalue=1, offvalue=0).\
                                  grid(column=2, row=2, sticky=W)
        self.v = IntVar()
        self.v.set(0)
        self.v1 = ttk.Checkbutton(self.mainframe3, text="Volume", 
                                  variable=self.v, command=self.plt_vol, 
                                  onvalue=1, offvalue=0). \
                                  grid(column=3, row=2, sticky=W)
        self.ac = IntVar()
        self.ac.set(0)
        self.ac1 = ttk.Checkbutton(self.mainframe3, text="Adjusted Close", 
                                  variable=self.ac, command=self.plt_ac, 
                                  onvalue=1, offvalue=0). \
                                  grid(column=4, row=2, sticky=W)
                        

#############################################################################
##             FUNCTIONS FOR EACH INDIVIDUAL STOCK                        ##
#############################################################################
    # Function to get stock close information 
    def stock_close1(self) : 
        
        symbol = 'AAPL'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)
      
    def stock_close2(self) : 
        
        symbol = 'F'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)    

    def stock_close3(self) : 
        
        symbol = 'GM'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)
        
    def stock_close4(self) : 
        
        symbol = 'GOOG'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)

    def stock_close5(self) : 
        
        symbol = 'TSLA'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)    

    def stock_close6(self) : 
        
        symbol = 'IBM'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)    

    def stock_close7(self) : 
        
        symbol = 'FB'
        base_url = \
        r"https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

        # main_url variable store complete url 
        main_url = base_url + "&symbol=" + symbol + \
                   "&apikey=" + self.api_key      
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        self.result = res_obj.json()
        #try:
            
        # Get and Display Ticker SYmbol for this Stock
        self.t = self.result["Global Quote"]['01. symbol']
        t = str(self.symbol) # converts the string self.volume to integer
        #t = "{:}".format(t) # converts int to string with commas
        self.symbol.set(self.t)
        
        # Get and Display Last Closing Price
        self.c_price = self.result["Global Quote"]['05. price']
        f_price = round(float(self.c_price), 2)
        self.c_price = str(f_price)
        self.close_price.set("$"+self.c_price)
        
        # Get and Display Previous Day's Closing Price
        self.pc_price = self.result["Global Quote"]['08. previous close']
        f_price = round(float(self.pc_price), 2)
        self.pc_price = str(f_price)
        self.p_close_price.set("$"+self.pc_price)

        # Get and Display Percent Change in Stock Value
        self.p_change = self.result["Global Quote"]['10. change percent']
        self.change.set(self.p_change)
        
        # Get and Display Last Day's Volume for this Stock
        self.volume = self.result["Global Quote"]['06. volume']
        v = int(self.volume) # converts the string self.volume to integer
        v = "{:,}".format(v) # converts int to string with commas
        self.vol.set(v)    

    def clear_entries(self):
        self.symbol.set("")
        self.close_price.set("")
        self.p_close_price.set("")
        self.change.set("")
        self.vol.set("")
        self.imgwin = ttk.Label(self.mainframe, text=""). \
                        grid(column=1, row=8, columns=8, sticky=W)

    def get_series(self):
        # Check for missing stock symbol
        if self.symbol == "":
            showinfo(title="Warning", message="Symbol Missing")
            return
        c_symbol = self.symbol.get().upper()
        # base_url variable store base url  
        base_url = \
          r"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
    
        # main_url variable store complete url 
        main_url = base_url + "&symbol="+c_symbol+"&apikey="+self.api_key         
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        result = res_obj.json()
        
        try:
            series = result['Time Series (Daily)']
        except:
            # If Stock Symbol is Invalid Display a Warning
            warn_msg = "Symbol " + c_symbol + " Not Found"
            showwarning(title="Warning", message=warn_msg)
            self.clear_entries()
            return
        
        n = len(series)
        f_array = np.array([[0.0]*4]*n)
        i_array = pd.Series([0]*n)
        t_array = pd.Series([pd.to_datetime("2020-01-01")]*n)
        i = n-1
        
        for key in series:
            t_array.loc[i] = pd.to_datetime(key, utc=False)
            i_array.loc[i] = int(series[key]['6. volume'])
            f_array[i][0] = float(series[key]['5. adjusted close'])
            f_array[i][1] = float(series[key]['4. close'])
            f_array[i][2] = float(series[key]['3. low'])
            f_array[i][3] = float(series[key]['2. high'])
            i-=1
            
        df0 = pd.DataFrame(t_array, columns=['date'])
        df1 = pd.DataFrame(f_array, columns = \
                          ['adjusted_close', 'close', 'low', 'high'])
        df2 = pd.DataFrame(i_array, columns=['volume'])
    
        self.df  = pd.concat([df0, df1, df2], axis=1).set_index('date')
    
    def graph_ts(self):
        self.get_series()
        # Check for missing stock symbol
        if self.symbol.get() == "":
            showinfo(title="Warning", message="Symbol Missing")
            self.clear_entries()
            return

        if self.c.get() == 1:
            # plot close price
            title = "Closing Price"
            x     = 'close'
        elif self.v.get() == 1:
            # plot volume
            title = "Volume"
            x     = 'volume'
        elif self.ac.get() == 1:
            # plot change
            title = "Adjusted Close"
            x     = "adjusted_close"
            
        self.fig = plt.figure(figsize=(6, 4), dpi=60)
        self.fig.patch.set_facecolor('gray')
        self.fig.patch.set_alpha(0.3)
        font1 = {'family':'Arial','color':'maroon','size': 16,
                 'weight':'normal'}
        font2 = {'family':'Arial','color':'maroon','size': 14,
                 'weight':'normal'}
        gp = self.fig.add_subplot(1,1,1)
        gp.set_facecolor('maroon')
        gp.plot(self.df[x], color='white')
        
        start_date = str(self.df.index[0].date())
        n          = len(self.df.index)-1
        end_date   = str(self.df.index[n].date())
        
        c_symbol   = self.symbol.get().upper() + \
                             " ("  + start_date + " to "  + end_date+")"
                             
        base_url = \
          r"https://www.alphavantage.co/query?function=SYMBOL_SEARCH"
    
        # main_url variable store complete url 
        main_url = base_url + "&keywords="+self.symbol.get()+ \
                        "&apikey="+self.api_key         
        # get method of requests module returns response object  
        res_obj = requests.get(main_url) 
        # json method returns json format data into python dictionary data type. 
        # rates are returned in a list of nested dictionaries 
        result = res_obj.json()
        
        try:
            series = result['bestMatches']
        except:
            # If Stock Symbol is Invalid Display a Warning
            warn_msg = "Symbol " + c_symbol + " Not Found"
            showwarning(title="Warning", message=warn_msg)
            self.clear_entries()
            return
        first_company = result["bestMatches"][0]
        name = first_company["2. name"]
        score = float(first_company["9. matchScore"])
        if score > 0.9:
            plt.title(name,   fontdict=font1)
        else:
            plt.title(c_symbol, fontdict=font1)
        plt.ylabel(title, fontdict=font2)
        plt.grid(True)
        plt.savefig('ts_plot.png')
        plt.show()
        self.imgobj = ImageTk.PhotoImage(Image.open('ts_plot.png'))
        self.imgwin = ttk.Label(self.mainframe4, image=self.imgobj). \
                        grid(column=1, row=1, sticky=W)

    def plt_close(self):
        self.c.set(1)
        self.v.set(0)
        self.ac.set(0)
        self.graph_ts()
        
    def plt_vol(self):
        self.c.set(0)
        self.v.set(1)
        self.ac.set(0)
        self.graph_ts()
        
    def plt_ac(self):
        self.c.set(0)
        self.v.set(0)
        self.ac.set(1)
        self.graph_ts()
# Instantiate GUI Canvas Using Tk   

root = Tk()
root.title("Stock Price")
api_key         = "demo"
api_key         = "CK8FNM4QB629PDZL"
# Paint Canvas Using Class StockGUI __init__()
my_gui = StockGUI(root, api_key)
# Display GUI
root.mainloop()

