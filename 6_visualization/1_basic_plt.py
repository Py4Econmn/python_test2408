# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 4*pi in steps of 0.1
x = np.arange(0, 4 * np.pi, 0.1)

# Compute sine of x
y = np.sin(x)

# Plot sine of x
plt.plot(x, y)
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

# Compute cosine of x
z = np.cos(x)

# Plot both sine and cosine on the same graph
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()

# Plot sine and cosine on the same graph with a different style
plt.plot(x, y, x, z, x, y + z)
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('Function values')
plt.legend(['sin','cos','sin+cos'])
plt.grid(True)
plt.show()

# Plot sine and cosine with specific colors and markers
# named colors: https://matplotlib.org/stable/gallery/color/named_colors.html
plt.plot(x, y, 'tab:blue', label='sin(x)')  # blue line
plt.plot(x, z, 'k', label='cos(x)')         # black line
plt.legend()
plt.grid(True)
plt.show()

# markers: https://matplotlib.org/stable/api/markers_api.html
plt.plot(x, y, 'tab:blue', label='sin(x)')  # blue line
plt.plot(x, z, 'ko', label='cos(x)')        # black line with circle markers
plt.legend()
plt.grid(True)
plt.show()

# Plot cosine with RGB color array scaled to [0, 1]
plt.plot(x, z, color=np.array([24, 19, 74]) / 255)  # custom RGB color
plt.grid(True)
plt.show()

plt.plot(x, z, color=np.array([0.35, 0.4, 0.25]))   # custom RGB color as float
plt.grid(True)
plt.show()

plt.plot(x, z, color=np.array([51, 255, 51]) / 255) # another custom RGB color
plt.grid(True)
plt.show()

plt.plot(x, z, color="mediumblue", marker='^')      # predefined color with triangle markers
plt.grid(True)
plt.show()

plt.plot(x, y, color='#ed0e0e')                     # color specified in HEX
plt.grid(True)
plt.show()

# Adding descriptions to the plot
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')
plt.xlabel('x values from 0 to 4π')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin(x) and cos(x) from 0 to 4π', fontsize=20, fontweight="bold")
plt.legend()
plt.grid(True)
plt.show()

# Annotating specific points on the plot
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')
plt.xlabel('x values from 0 to 4π')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin(x) and cos(x) from 0 to 4π', pad=20,fontweight="bold")
plt.text(1, 0.5, 'This point is @ x=1, y=0.5')
plt.text(3, 0.25, 'This point is @ x=3, y=0.25')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, 4 * np.pi + 1, 0.5), fontsize=5,rotation=45)
plt.yticks(np.arange(-1, 1.1, 0.25), fontsize=12)
plt.subplots_adjust(bottom=0.5,left=0.2)
plt.show()

# Object-oriented approach to plotting
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0, 4.5)
plt.show()

# MATLAB-style approach to plotting
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0, 4.5)
plt.show()

# Creating subplots
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot data on the subplots
ax1.bar([1, 2, 3], [3, 4, 5])
ax2.barh([0.5, 1, 2.5], [0.5, 1, 2])
ax2.axhline(0.45)
ax1.axvline(1.5)
ax3.scatter(x, y)
ax1.set_title('Ax1 title')
ax3.set_title('Ax3 title')
fig.suptitle("Main title")
plt.show()

# Creating subplots using a more concise method
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
fig.suptitle("Super title")
ax1.bar([1, 2, 3], [3, 4, 5])
ax2.barh([0.5, 1, 2.5], [0, 1, 2])
ax2.axhline(0.45)
ax2.fill_betweenx([0, 1, 2], 0.45, 0.65, color='grey', alpha=0.5)
ax1.axvline(0.65)
ax3.scatter(x, y)
plt.show()

# Setting figure size
fig = plt.figure(figsize=(8, 4))
fig.suptitle("Main title")
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot data on the subplots
ax1.bar([1, 2, 3], [3, 4, 5])
ax2.barh([0.5, 1, 2.5], [0, 1, 2])
ax2.axhline(0.45)
ax1.axvline(1.5)
ax3.scatter(x, y)
ax3.set_title('Ax3 title')
plt.show()

# Save the figure
# plt.savefig('6_visualization/mypic.png')
fig.savefig('6_visualization/mypic.png')
