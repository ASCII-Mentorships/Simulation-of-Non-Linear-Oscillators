from turtle import color
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# creating a blank window
# for the animation
fig = plt.figure()
axis = plt.axes(xlim =(-10, 10),
				ylim =(-10, 10))

line, = axis.plot([], [], lw = 2)
scat = axis.scatter([], [], color="green", zorder=4)
scat2 = axis.scatter([], [], color="red", zorder=4)
scat3 = axis.scatter([], [], color="blue", zorder=4)
scat4 = axis.scatter([], [], color="yellow", zorder=4)
scat5 = axis.scatter([], [], color="black", zorder=4)

# what will our line dataset
# contain?
def init():
	line.set_data([], [])
	return line,

# initializing empty values
# for x and y co-ordinates
xdata, ydata = [], []

# Reading an excel file using Python
import xlrd
 
# Give the location of the file
# loc = ("D:\\Courses\\2-2\\SOP\\Data\\xls_data\\N=2\\1.000000\sims.xls")
loc = ("D:\\Courses\\2-2\\SOP\\Data\\xls_data\\N=4\\0.330000\\sims.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 



# animation function
def animate(i):
	# t is a parameter which varies
	# with the frame number
	t = 9+i
	
	# x, y values to be plotted
	x = sheet.cell_value(i,0)
	y = sheet.cell_value(i,4)

	x2 = sheet.cell_value(i,1)
	y2 = sheet.cell_value(i,5)

	x3 = sheet.cell_value(i,2)
	y3 = sheet.cell_value(i,6)

	x4 = sheet.cell_value(i,3)
	y4 = sheet.cell_value(i,7)
	
	x5 = sheet.cell_value(i,8)
	y5 = sheet.cell_value(i,9)
	
	# appending values to the previously
	# empty x and y data holders
	xdata.append(x)
	ydata.append(y)
	# line.set_data(xdata, ydata)
	# scat.set_markersize(100)
	scat.set_offsets([x,y])
	scat2.set_offsets([x2,y2])
	scat3.set_offsets([x3,y3])
	scat4.set_offsets([x4,y4])
	scat5.set_offsets([x5,y5])

	return line,scat, scat2, scat3, scat4,scat5

# calling the animation function	
anim = animation.FuncAnimation(fig, animate, init_func = init,
							frames = 10000, interval = 20, blit = True)

# saves the animation in our desktop
# anim.save("N=4_unsymm.mp4", writer = 'ffmpeg', fps = 30)

plt.xlabel("Phi")
plt.ylabel("Phi-dot")
plt.show()