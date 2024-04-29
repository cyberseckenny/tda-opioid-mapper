import kmapper as km
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import datasets
import sklearn

d = {}
type_1 = 'Synthetic opioids, excl. methadone (T40.4)'
type_2 = 'Heroin (T40.1)'
type_3 = 'Number of Drug Overdose Deaths'

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

        if state == 'United States':
            continue

        if indicator in [type_1, type_2, type_3]:
            key = (state, year, month)
            if key not in d:
                d[key] = {}
            d[key][indicator] = deaths

result = []
for state_year_month, values in d.items():
    synthetic_opioids = values.get(type_1, None) 
    heroin = values.get(type_2, None) 
    number = values.get(type_3, None)
    if all(values.values()) and synthetic_opioids is not None and heroin is not None and number is not None:  # Check if all values are not empty
        result.append([values[type_1], 
                        values[type_2], values[type_3]])

data = np.array(result)
# data, labels = datasets.make_circles(n_samples=5000, noise=0.1, factor=0.3)

mapper = km.KeplerMapper(verbose=2)
lens = mapper.fit_transform(data)
graph = mapper.map(
    lens,
    data,
    clusterer=sklearn.cluster.DBSCAN(eps=200, min_samples=6),
    cover=km.Cover(15, 0.2),
)
mapper.visualize(graph, path_html="tda.html", title='Opioid Deaths')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlabel('Synthetic opioids')
ax.set_ylabel('Heroin')
ax.set_zlabel('Overall Drug Overdose Deaths')

ax.scatter(data[: ,0], data[: ,1], data[: ,2])
plt.show()
