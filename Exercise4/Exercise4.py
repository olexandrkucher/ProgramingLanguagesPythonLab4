__author__ = 'KOL'

import numpy as np
import matplotlib.pyplot as mpl
from scipy.spatial import distance
from sklearn.cluster import DBSCAN


def write_to_file(file_name, data_for_writing):
    """
    write coordinates of points into file for testing this data in another program, for example program from
    lab #6 from "Data mining" course
    """
    file = open(file_name, "w")
    x, y = data_for_writing[:, 0], data_for_writing[:, 1]
    for i in range(0, len(x)):
        file.write(str(x[i]) + "," + str(y[i]) + "\n")
    file.close()

# Creating data
c1 = np.random.random((100, 2)) + 5
c2 = np.random.random((50, 2))

# Creating a uniformly distributed background
u1 = np.random.uniform(low=-10, high=10, size=100)
u2 = np.random.uniform(low=-10, high=10, size=100)
c3 = np.column_stack([u1, u2])

# Pooling all the data into one 150 x 2 array
data = np.vstack([c1, c2, c3])
write_to_file("data.txt", data)

# Calculating the cluster with DBSCAN function.
# db.labels_ is an array with identifiers to the
# different clusters in the data.
db = DBSCAN(eps=0.95, min_samples=10).fit(data)
labels = db.labels_

# Retrieving coordinates for points in each
# identified core. There are two clusters
# denoted as 0 and 1 and the noise is denoted
# as -1. Here we split the data based on which
# component they belong to.
dbc1 = data[labels == 0]
dbc2 = data[labels == 1]
noise = data[labels == -1]

# Setting up plot details
x1, x2 = -12, 12
y1, y2 = -12, 12
fig = mpl.figure()
fig.subplots_adjust(hspace=0.1, wspace=0.1)
ax1 = fig.add_subplot(121, aspect='equal')
ax1.scatter(c1[:, 0], c1[:, 1], lw=0.5, color='#00CC00')
ax1.scatter(c2[:, 0], c2[:, 1], lw=0.5, color='#028E9B')
ax1.scatter(c3[:, 0], c3[:, 1], lw=0.5, color='#FF7800')
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax1.set_xlim(x1, x2)
ax1.set_ylim(y1, y2)
ax1.text(-11, 10, 'Original')
ax2 = fig.add_subplot(122, aspect='equal')
ax2.scatter(dbc1[:, 0], dbc1[:, 1], lw=0.5, color='#00CC00')
ax2.scatter(dbc2[:, 0], dbc2[:, 1], lw=0.5, color='#028E9B')
ax2.scatter(noise[:, 0], noise[:, 1], lw=0.5, color='#FF7800')
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
ax2.set_xlim(x1, x2)
ax2.set_ylim(y1, y2)
ax2.text(-11, 10, 'DBSCAN identified')
fig.savefig('scikit_learn_clusters.pdf', bbox_inches='tight')
