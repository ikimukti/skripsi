import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y_values, title, xlabel, ylabels, rotation, figsize, tight_layout, colors, unit):
    # ...
    plt.switch_backend('AGG')
    plt.figure(figsize=figsize)
    plt.title(title)
    
    colors_y = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    for i, y in enumerate(y_values):
        label = ylabels[i]
        plt.plot(x, y, color=colors_y[i], marker='o', label=label)
    # tambahkan garis grid
    plt.grid(True)
    # plt axis maximum
    # Find the maximum y value from all values y_values 
    max_y = max(max(y) for y in y_values)
    # Set the y axis limit to be 10% more than the maximum y value
    # plt.ylim(0, max_y * 1.2)
    
    # tambahkan legend
    plt.legend(loc='upper left')
    plt.xticks(rotation=rotation)
    # add  "unt" to yticks
    unt = range(0, int(max_y * 1.2) + 1, 1)
    if unit == "%":
        # convert to percentage
        unt = range(0, int(max_y * 1.2) + 1, 10)
    elif unit == "dB":
        unt = range(0, int(max_y * 1.2) + 1, 10)
    plt.yticks(unt, [str(x) + " "+ unit for x in unt])
    # perbesar ukuran yticks
    plt.tick_params(axis='y', which='major', labelsize=6)
    plt.tick_params(axis='x', which='major', labelsize=6)
    # rotate xticks
    plt.xticks(rotation=90)
    
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabels)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot_table(x, y, title, xlabel, ylabel, rotation, figsize, tight_layout, colors):
    # ...
    plt.switch_backend('AGG')
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    graph = get_graph()
    return graph