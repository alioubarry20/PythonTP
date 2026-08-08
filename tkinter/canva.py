import tkinter as tk

root = tk.Tk()
root.title("Canvas test")

canvas =tk.Canvas(root,width=400,height=300,bg="white")
canvas.pack()


def click(event):
   print("widget:",event.widget)
   print("x:",event.x,"y:",event.y)
   """ canvas.create_oval(
        event.x - 10,event.y -10,
        event.x + 10,event.y +10,
        fill="black"

    )"""
   

canvas.bind("<Motion>",click)

root.mainloop()