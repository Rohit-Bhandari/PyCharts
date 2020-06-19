# Bar Chart

from matplotlib import pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
day_temp = [27, 34, 30, 38, 25, 21, 29]
night_temp = [20, 27, 25, 32, 21, 16, 23]
plt.bar(days, day_temp, color="orange")
plt.bar(days, night_temp, color="orangered")
plt.title("Temperature Record Of The Last Week\n")
plt.xlabel("\nDays")
plt.ylabel("\nTemperature (C)")
plt.legend(["Day", "Night"])
plt.show()