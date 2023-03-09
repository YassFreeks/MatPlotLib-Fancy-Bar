import matplotlib.pyplot as plt

# Define a function to add labels to the top of each bar
def autolabel(rectangle_group):
    for rect in rectangle_group:
        # Get the height of the bar
        height = rect.get_height()

        # Add the label to the top of the bar
        ax.annotate(str(height),
            xy = (rect.get_x() + rect.get_width() / 2,height), # Set the position of the label
            ha = 'center', # Horizontally center the label
            xytext = (0,3), textcoords = 'offset points', # Add some offset to the label
            color = 'grey') # Set the color of the label

# Define the data to be plotted
phases      = ['Mid 90s', 'Early 2k', 'Mid 2k', 'Mid 2010s']
playstation = [102      ,  155      ,  87     ,  110       ]
xbox        = [0        ,  24       ,  86     ,  50        ]
nintendo    = [33       ,  22       ,  102    ,  62        ]
pc_sales    = [71       ,  128      ,  240    ,  316       ]

# Set the width of each bar
width = 0.2

# Create lists to position the bars for each platforms side by side
x_playstation = [x - width for x in range(len(playstation))]
x_xbox        = [x for x in range(len(xbox))]
x_nintendo    = [x + width for x in range(len(nintendo))]

# Create a figure and a set of subplots
fig,ax = plt.subplots()

# Create the bars for each platform
rect1 = ax.bar(x_playstation, playstation, width, label= 'Playstation', color= 'darkslategray')
rect2 = ax.bar(x_xbox, xbox, width, label= 'XBox', color= 'limegreen')
rect3 = ax.bar(x_nintendo, nintendo, width, label= 'Nintendo', color= 'crimson')

# Add the line plot of PC sales to the same chart
ax.plot(phases, pc_sales, label= 'PC Sales', color= 'black', marker= 'o')

# Set the title and y-axis label of the chart
ax.set_title('The hardware market')
ax.set_ylabel('Total sales (in millions)')

# Display the legend of the chart
ax.legend()

# Add the height labels to the top of each bar
autolabel(rect1)
autolabel(rect2)
autolabel(rect3)

# Display the chart
plt.show()
