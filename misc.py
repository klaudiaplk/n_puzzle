import math  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(path, board_height):
    fig, ax = plt.subplots()
    plt.axis('off')
    
    k = -len(path) + 1
    def update(frame_number):
        nonlocal k
        if -k < len(path) :
            k = k - 1
        else:
            k = -1
        ax.cla()
        plt.axis('off')
        intersection_matrix =  path[k].getBoard().getBoard()
        ax.matshow(intersection_matrix, cmap=plt.cm.Greens)
        for i in range(0, board_height):
            for j in range(0, board_height):
                c = intersection_matrix[j][i]
                ax.text(i, j, str(c), va='center', ha='center')


# create animation using update function
    
    animation = FuncAnimation(fig, update, interval=2000)
    plt.show()


def generate_board(n):
    
    height = int(math.sqrt(n+1))
    arr = [i for i in range(1, n+1)]
    arr.append(-1)
    np.random.shuffle(arr)
    board = np.reshape(arr, (height, height))
    return board
