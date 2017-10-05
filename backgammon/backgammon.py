"""
Backgammon game
"""

import tkinter as tk

def draw_board(frame):
    canvas = tk.Canvas(frame, bg='blue')
    canvas.create_rectangle(10,10, 300, 200, width=5, fill='')
    canvas.create_rectangle(310, 10, 600, 200, width=5, fill='')
    #Upward points
    center = 575
    width = 290/6 - 5 
    canvas.create_polygon(center+width/2,200,center,120,center-width/2,200, fill='red')
    canvas.pack(expand='yes', fill='both', ipadx=10, ipady=10) 

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1080x800+200+200")
    frame = tk.Frame(root)
    frame.pack(fill='both')
    draw_board(frame)
    
    root.mainloop()