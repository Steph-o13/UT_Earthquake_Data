# March 22, 2020

import matplotlib.pyplot as plt
import pandas as pd


# read earthquake data
earthquakes = pd.read_csv("https://raw.githubusercontent.com/Steph-o13/UT_Earthquake_Data/master/earthquakes.csv", error_bad_lines = False)

# summary information
print(earthquakes.head())
print(earthquakes.describe())

# histogram
plt.style.use('seaborn')
plt.hist(earthquakes.mag, bins = 10, alpha = .7, rwidth = .85)
plt.title("Number of Earthquakes of at least 1.0 Magnitude")
plt.xlabel("Magnitude")
plt.ylabel("Number of Earthquakes")
plt.show()
plt.clf()

# create data set of only earthquakes with magnitude greater than 2.5
earthquakes_twoFive = earthquakes[earthquakes["mag"]>=2.5]

# take a separate dataset of earthquakes with magnitude > 3.9
df = earthquakes_twoFive.query("mag >= 3.9")

# scatter plot of all earthquakes with magnitude >= 2.5
plt.scatter(earthquakes_twoFive.time, earthquakes_twoFive.mag, color = "grey", alpha = .75)
plt.title("Earthquakes above 2.5 Magnitude")
plt.grid(True)
plt.xlabel("Date ; Time (utc)")
plt.ylabel("Magnitude")
plt.xticks(rotation = 90)

# scatter plot of earthquakes with magnitude >= 3.9 (outliers)
plt.scatter(df.time, df.mag, color = "#AE1A28", alpha = .9)

# for earthquakes of magnitude >= 3.9, add label of the magnitude to the point.
for i in range(df.shape[0]):
    plt.annotate(df.mag.tolist()[i], (df.time.tolist()[i], df.mag.tolist()[i]))
print(df.shape[0])
plt.tight_layout()

# display plot.
plt.show()
plt.clf()


