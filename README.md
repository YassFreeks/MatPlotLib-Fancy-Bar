# MatPlotLib-Fancy-Bar
Creating a fancy bar in MatPlotLib

This code is a Python script that uses the Matplotlib library to create a bar chart and a line chart that compare the sales of different gaming platforms over time

This code is a Python script that uses the Matplotlib library to create a bar chart and a line chart that compare the sales of different gaming platforms over time. The chart shows the total sales (in millions) of each platform in four different phases: "Mid 90s", "Early 2k", "Mid 2k", and "Mid 2010s".

## Here's a step-by-step breakdown of what the code does:

### 1. Import the necessary library: 

```
import matplotlib.pyplot as plt
```
This line imports the Matplotlib library and the pyplot module, which provides a convenient interface for creating plots.

### 2. Define a function to add labels to the top of each bar:

```
def autolabel(rectangle_group):
    for rect in rectangle_group:
        height = rect.get_height()

        ax.annotate(str(height),
            xy = (rect.get_x() + rect.get_width() / 2,height), 
            ha = 'center',
            xytext = (0,3), textcoords = 'offset points',
            color = 'grey')
```
This function takes a group of bar rectangles as input and adds a label to the top of each bar with the height of the bar. The annotate method is used to add the label to the plot.

### 3. Define the data to be plotted:
```
phases      = ['Mid 90s', 'Early 2k', 'Mid 2k', 'Mid 2010s']
playstation = [102      ,  155      ,  87     ,  110       ]
xbox        = [0        ,  24       ,  86     ,  50        ]
nintendo    = [33       ,  22       ,  102    ,  62        ]
pc_sales    = [71       ,  128      ,  240    ,  316       ]
```
These lines define the data to be plotted. Each list represents the sales of a different gaming platform in each phase.

### 4. Set the width of each bar:

```
width = 0.2
```

This line sets the width of each bar in the plot.

### 5. Create lists to position the bars for each platform side by side:

```
x_playstation = [x - width for x in range(len(playstation))]
x_xbox        = [x for x in range(len(xbox))]
x_nintendo    = [x + width for x in range(len(nintendo))]
```

These lines create three lists that determine the x-positions of the bars for each platform. The range function is used to create a sequence of integers that represent the positions of the bars.

### 6. Create a figure and a set of subplots:

```
fig,ax = plt.subplots()
```

These lines create a figure object and a set of subplots. The subplots function creates a new figure and returns a tuple containing the figure object and a set of axes.

### 7.Create the bars for each platform:

```
rect1 = ax.bar(x_playstation, playstation, width, label= 'Playstation', color= 'darkslategray')
rect2 = ax.bar(x_xbox, xbox, width, label= 'XBox', color= 'limegreen')
rect3 = ax.bar(x_nintendo, nintendo, width, label= 'Nintendo', color= 'crimson')
```

These lines create the bars for each platform using the bar function. The label argument specifies the label for each bar.
