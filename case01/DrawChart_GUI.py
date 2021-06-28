# -*- coding: UTF-8 -*-
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter

def show():

        conn = sqlite3.connect('iot.db')
        df = pd.read_sql_query("SELECT id, cds, temp, humi, ts FROM Env "
                               "order by ts desc limit 15", con=conn)
        df = df[::-1] # reverse
        print(df)
        conn.close()

        # 建立視窗
        root = tkinter.Tk()
        root.title("溫濕度走勢圖")
        f = Figure(figsize=(5, 4), dpi=100)
        f_plot = f.add_subplot(111)
        canvs = FigureCanvasTkAgg(f, root)

        # 繪圖
        f_plot.plot(df['id'], df['temp'], label="temp")  # 繪製折線圖
        f_plot.plot(df['id'], df['humi'], label="humi")  # 繪製折線圖
        f_plot.grid(True)
        # 圖例
        plt.xlabel('time')
        plt.ylabel('value(%)')
        #f_plot.setp(f.xaxis.get_majorticklabels(), rotation=90)
        f_plot.legend()
        #plt.show()

        canvs.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        root.mainloop()
if __name__=='__main__':
    show()