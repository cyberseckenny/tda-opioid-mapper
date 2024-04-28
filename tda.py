import kmapper as km
import numpy as np
import csv
import matplotlib.pyplot as plt

states = ["New York City", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
state_to_int = {state: i for i, state in enumerate(states)}
states_int = [state_to_int[state] for state in states]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_to_int = {month: i for i, month in enumerate(months)}
months_int = [month_to_int[month] for month in months]

# state, month
data = np.zeros((52, 12))

with open('VSRR_Provisional_Drug_Overdose_Death_Counts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        year = row[1]
        indicator = row[4]
        state = row[8]
        month = row[2]
        deaths = row[5]
        
        if year == '2022' and indicator == 'Opioids (T40.0-T40.4,T40.6)' and state != "United States":
            if deaths != '':
                data[state_to_int[state] - 1, month_to_int[month] - 1] = int(deaths.replace(',', ''))
                
# mapper = km.KeplerMapper(verbose=1)
# projected_data = mapper.fit_transform(data, projection=[0, 1]) # x-y axis
# cover = km.Cover(n_cubes=10)
# graph = mapper.map(projected_data, data, cover=cover)
# mapper.visualize(graph, path_html="tda.html")

states_int = states_int[:12]
print(states_int)
print(months_int)
print(data[:12])

plt.figure(figsize=(8, 6))
plt.scatter(states_int, months_int, cmap='YlGnBu', alpha=0.7)
plt.colorbar(label='Value')
plt.xlabel('States')
plt.ylabel('Months')
plt.title('Scatter plot of deaths by state and month for 2020')

ax = plt.gca()
ax.set_aspect('equal')

plt.show()

