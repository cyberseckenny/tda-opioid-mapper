import kmapper as km
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import datasets
import sklearn

x, y, z, j, k = [], [], [], [], []

with open('VSRR_Provisional_Drug_Overdose_Death_Counts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first = True

    for row in csv_reader:
        if (first == True):
            first = False
            continue

        year = row[1]
        indicator = row[4]
        state = row[8]
        month = row[2]

        if row[5] == '':
            continue

        deaths = int(float(row[5].replace(',', '')))
        
        # what actually matters

        if state != "United States":
            if indicator == 'Synthetic opioids, excl. methadone (T40.4)':
                x.append(deaths)
            elif indicator == 'Heroin (T40.1)':
                y.append(deaths)
            elif indicator == 'Number of Drug Overdose Deaths':
                z.append(deaths)

             
        # elif indicator == 'Methadone (T40.3)':
        #      j.append(deaths)

data = np.array(list(zip(x, y, z)))
print(len(x), len(y), len(z))
# data, labels = datasets.make_circles(n_samples=5000, noise=0.1, factor=0.3)

# mapper = km.KeplerMapper(verbose=2)
# lens = mapper.fit_transform(data)
# graph = mapper.map(
#     lens,
#     data,
#     clusterer=sklearn.cluster.DBSCAN(eps=100000, min_samples=1),
#     cover=km.Cover(30, 0.2),
# )
# mapper.visualize(graph, path_html="tda.html")

min_length = min(len(x), len(y), len(z))  
x = x[:min_length]
y = y[:min_length]
z = z[:min_length]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlabel('Synthetic opioids')
ax.set_ylabel('Heroin')
ax.set_zlabel('Overall Drug Overdose Deaths')

ax.scatter(data[: ,0], data[: ,1], data[: ,2])
plt.show()
