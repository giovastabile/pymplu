import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "serif"
plt.rcParams.update({"axes.grid" : True})
plt.rcParams['lines.markersize'] = 10

def change_axes_font(font_size):
    """
    This function set the font size of the font used for the axes in a matplotlib graph

    Args:
        font_size {integer}: size of the font to set
    """
    plt.rc('axes', titlesize=font_size)     # fontsize of the axes title
    plt.rc('axes', labelsize=font_size)    # fontsize of the x and y labels

def change_tick_font(font_size):
    """
    This function set the font size of the font used for the ticks in a matplotlib graph

    Args:
        font_size {integer}: size of the font to set
    """
    plt.rc('xtick', labelsize=font_size)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=font_size)    # fontsize of the tick labels


def change_legend_font(font_size):
    """
    This function set the font size of the font used for the legend text in a matplotlib graph

    Args:
        font_size {integer}: size of the font to set
    """
    plt.rc('legend', fontsize=font_size)    # legend fontsize


def change_title_font(font_size):
    """
    This function set the font size of the font used for the title text in a matplotlib graph

    Args:
        font_size {integer}: size of the font to set
    """
    plt.rc('figure', titlesize=font_size)  # fontsize of the figure title

def set_default_font():
    """
    Set the default font sizes (18 for title, 16 for axes, 14 for legend and ticks)
    """
    change_title_font(18)
    change_axes_font(16)
    change_tick_font(14)
    change_legend_font(14)
    plt.rcParams.update({"axes.grid" : True})

markers = ['o','v','^','<','>','1','2','3','4','8','s','p','P']
colors = ["#0072BD"
,"#D95319"	
,"#EDB120"	
,"#7E2F8E"	
,"#77AC30"	
,"#4DBEEE"	
,"#A2142F"
,[0, 0, 1]
,[0, 0.5, 0]
,[1, 0, 0]
,[0, 0.75, 0.75]
,[0.75, 0, 0.75]
,[0.75, 0.75, 0]
]

linestyles = [
(0, ()) #solid
,(0, (1, 10)) #loosely dotted
,(0, (1, 5)) #dotted
,(0, (1, 1)) #densely dotted
,(0, (5, 10)) #loosely dashed
,(0, (5, 5)) #dashed
,(0, (5, 1)) #densely dashed
,(0, (3, 10, 1, 10)) #loosely dashdotted
,(0, (3, 5, 1, 5)) #dashdotted
,(0, (3, 1, 1, 1)) #densely dashdotted
,(0, (3, 10, 1, 10, 1, 10)) #loosely dashdotdotted
,(0, (3, 5, 1, 5, 1, 5)) #dashdotdotted
,(0, (3, 1, 1, 1, 1, 1)) #densely dashdotdotted 
]

def test():
    """
        Plot a test graph using the dafault options to visualize the different linestyles
    """
    import numpy as np
    set_default_font()
    x = np.linspace(0,10,100)
    y = np.sin(x)
    for i in range(12):
        plt.plot(x,y+i,label=str(i),color=colors[i],marker=markers[i],linestyle=linestyles[i],markevery=10)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("Test")
    plt.legend()
    plt.show()
        
