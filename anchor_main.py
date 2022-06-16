from tkinter import *

#degrees = i
#[loading value, status]
# yellow = loading value >= 90
#green
pole = []


def status(loading_value):
    if loading_value < 90:
        return "green"
    if 90 <= loading_value < 100:
        return "yellow"
    if loading_value > 100:
        return "red"


def anchor_placement():
    print("drawing")


def generateAnchorData():
    print("getAnchorData")
    #here is where you would get the horizontal loading data
    for i in range(30):
        pole.append(106)


def draw_chart():
    canvas = Canvas(root, width=800, height=800, bg='papaya whip')
    origin = (400, 400)
    canvas.create_line(origin, 0, 400, width="3")  # W
    canvas.create_line(origin, 400, 0, width="3", fill='red')  # N
    canvas.create_line(origin, 800, 400, width="3", fill='blue')  # E
    canvas.create_line(origin, 400, 800, width="3", fill='green')  # S

    start = 0
    length = 30
    start = (-1 * start) + 90
    length = length * -1

    canvas.create_arc(200, 200, 600, 600, start=start, extent=length, fill="red")

    start = 30
    length = 30
    start = (-1 * start) + 90
    length = length * -1

    canvas.create_arc(200, 200, 600, 600, start=start, extent=length, fill="yellow")

    start = 60
    length = 60
    start = (-1 * start) + 90
    length = length * -1

    canvas.create_arc(200, 200, 600, 600, start=start, extent=length, fill="lime green")

    start = 120
    length = 30
    start = (-1 * start) + 90
    length = length * -1

    canvas.create_arc(200, 200, 600, 600, start=start, extent=length, fill="yellow")

    start = 150
    length = 210
    start = (-1 * start) + 90
    length = length * -1

    canvas.create_arc(200, 200, 600, 600, start=start, extent=length, fill="red")

    canvas.pack()



if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    draw_chart()

    root.mainloop()