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

    axes.yaxis.set_ticks(np.arange(0,85,10))
    
    
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


    #%% More Object Oriented 

    #Single plot inside subplot
    fig, axes = plt.subplots()

    axes.plot(x,y);


    #Set number of rows/columns in subplot
    fig, axes = plt.subplots(nrows = 1, ncols = 2);

    # Overlap issues occured, use: "plt.tight_layout();"
    
    '''
    # Or pad sides yourself using:
        fig.subplots_adjust(top=0.96)
        fig.subplots_adjust(bottom=0.06)
        fig.subplots_adjust(left=.2)
        fig.subplots_adjust(right=.98)
    '''


    #Using the fig, axes format, this enables you to use for loops to populate plots
    for current_ax in axes:
        current_ax.plot(x,y);
        
        
    #Set number of rows/columns in subplot
    fig, axes = plt.subplots(nrows = 1, ncols = 2);

    # Plot on first subplot
    axes[0].plot(x,y);

    # Plot on second subplot
    axes[1].plot(y,x);


    #%% Figure size, aspect ratio, and DPI

    #(figsize = (width, height), dpi = ndots, )
    fig = plt.figure(figsize = (3, 2), dpi = 100);

    ax = fig.add_axes([0,0,1,1]);

    ax.plot(x,y);

    #%% Adding more axes with these features


    fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 2), dpi = 100);

    axes[0].plot(x,y);

    axes[1].plot(y,x);

    #Gets rid of overlap
    plt.tight_layout();


    #%% Saving Figures

    fig = plt.figure();

    fig.set_axes([0,0,1,1]);
    ax.plot(x,y);
    ax.set_title('Title');
    ax.set_xlabel('x label');
    ax.set_ylabel('y label');
    
    # ax.set_ylabel('abc', rotation=0, fontsize=20, labelpad=20) #More options



    #fig.savefig('<filename>.<ext>', dots per in, );
    fig.savefig('my_picture.png', dpi = 100)

    #%% Legends

    fig = plt.figure();

    ax = fig.add_axes([0,0,1,1]);

    # making plots with legend info
    ax.plot(x, x**2, label = 'X Sqared');
    ax.plot(x, x**3, label = 'X Cubed');

    ax.legend();

    #%% Legends with locations
    # More info https://matplotlib.org/api/legend_api.html?highlight=legend#module-matplotlib.legend

    fig = plt.figure();

    ax = fig.add_axes([0,0,1,1]);

    # making plots with legend info
    ax.plot(x, x**2, label = 'X Sqared');
    ax.plot(x, x**3, label = 'X Cubed');

    # legend, have matplotlib find best location
    ax.legend(loc = 0);

    # legend in center
    ax.legend(loc = 10);

    # legend at tuple specification
    ax.legend(loc = (.1, .1));