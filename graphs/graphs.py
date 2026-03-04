import os

import matplotlib.pyplot as plt
import csv

def create_graph(file_path, save_path, title, y_label):
    x = []
    y = []

    plt.clf()

    try:
        with open(file_path, 'r') as csv_file:
            plots = csv.reader(csv_file, delimiter=',')

            for row in plots:
                x.append(int(row[0]))
                y.append(float(row[1]))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    file_name = title.replace(" ", "_") + ".png"
    full_path = os.path.join(save_path, file_name)

    plt.plot(x, y)
    plt.xlabel("Games")
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    plt.savefig(full_path)

