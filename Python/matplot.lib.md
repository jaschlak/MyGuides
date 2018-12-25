# Matplot.lib

    Basics of how to use Matplot.lib
    
## Code (can be pasted into IDE):

    import matplotlib.pyplot as plt

    import numpy as np

    # create array with 11 points from 0-5
    x = np.linspace(0,5,11)

    y = x ** 2

    # Functional Plotting Method (color and line style added)
    plt.plot(x, y)

    # Functional Plotting Method (color and line style added)
    plt.plot(x, y, 'r--')

    # Add title, and x and y labels
    plt.title('Here is a title')
    plt.xlabel('X Arguements')
    plt.ylabel('Y Arguements')
    plt.show()

    # Subplots (num rows, num col, this plot number)
    plt.subplot(1,2,1)
    plt.plot(x, y, 'r--')
    plt.subplot(1,2,2)
    plt.plot(y, x, 'g*-')



    #%% Object Oriented Ploting

    #Basically made the canvas for plotting
    fig = plt.figure();

    # axes zoom ([left, bottom, width, height])
    axes = fig.add_axes([0,0,.5,.5]);

    # Finally plot x and y
    axes.plot(x,y);

    axes.set_xlabel('x label');
    axes.set_ylabel('ylabel');
    axes.set_title('This Graph');

    # Finished Graph

    #%% Add second graph to the figure

    fig = plt.figure();
    axes1 = fig.add_axes([.1,.1,.8,.8]);
    axes1.plot(x,y);
    axes1.set_title('Larger Plot');

    #([Starts 20% from left, 50% from bottom, takes up 40 % width, 30% height])
    axes2 = fig.add_axes([.2, .5, .4, .3]);
    axes2.plot(y,x);
    axes2.set_title('Smaller Plot');

