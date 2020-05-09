import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_deaths = "deaths_global.csv"
file_recoveries = "recovered_global.csv"

# Get dates and values of deaths from file for just US.
with open(file_deaths) as f_d:
    reader = csv.reader(f_d)
    header_row = next(reader)

    deaths, dates = [], []

    for row in reader:
        if row[1] == 'US':
            current_date = datetime.strptime(row[4], "%Y-%m-%d")
            dates.append(current_date)

            value = int(row[5])
            deaths.append(value)
        else:
            continue

# Get dates and values of recoveries from file for just US.
with open(file_recoveries) as f_r:
    reader = csv.reader(f_r)
    header_row = next(reader)

    recover, dates = [], []

    for row in reader:
        if row[1] == 'US':
            current_date = datetime.strptime(row[4], "%Y-%m-%d")
            dates.append(current_date)

            value = int(row[5])
            recover.append(value)
        else:
            continue

# Plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, deaths, c='red', label="Deaths")
plt.plot(dates, recover, c='blue', label="Recoveries")

# Format plot.
plt.title("Covid Deaths in US", fontsize=24)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Deaths", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=8)
plt.legend()

plt.show()