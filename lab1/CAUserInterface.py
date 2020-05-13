import matplotlib
from lab1 import cellularAutomata1D
import tkinter
import matplotlib.pyplot as plt

from tkinter.ttk import *

matplotlib.use("TKAgg")


def initialize_automaton():
    grid_size = int(entr1.get())
    iterations = int(entr2.get())
    rule = int(spin.get())
    init_state = [0] * grid_size
    init_state[int((0 + len(init_state) - 1 )/ 2)] = 1  # insert 1 in the middle of an array
    ca = cellularAutomata1D.CellularAutomata1D(iterations, grid_size, init_state, rule)
    state_array = ca.generate_automaton()
    plt.imshow(state_array, cmap='Greys', interpolation='nearest')
    plt.show()


window = tkinter.Tk()

window.title("Cellular automata 1D")
window.resizable(0, 0)
label1 = tkinter.Label(window, text=" Rule ").grid(row=1, column=0)
spin = tkinter.Spinbox(window, from_=0, to=255, width=5)
spin.grid(row=1, column=1)

label2 = tkinter.Label(window, text=" Grid size ").grid(row=1, column=2)
entr1 = Entry(window, width=10)
entr1.grid(row=1, column=3)
grid = entr1.get()
label3 = tkinter.Label(window, text=" Number of iterations ").grid(row=1, column=4)
entr2 = Entry(window, width=10)
entr2.grid(row=1, column=5)
bt = tkinter.Button(window, text=" Draw automaton ", command=initialize_automaton)
bt.grid(row=1, column=6)

window.geometry('500x100')

window.mainloop()
