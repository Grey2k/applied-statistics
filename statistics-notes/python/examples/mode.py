import statistics

import pandas

mode = statistics.mode(["Red", "Blue", "Green", "Yellow", "Red", "Blue", "Green", "Yellow", "Yellow"])
series = pandas.Series(["Red", "Blue", "Green", "Yellow", "Red", "Blue", "Green", "Yellow", "Yellow"])

# Prints Yellow as most common in given dataset
print(mode)

# describe data set (top is Yellow)
print(series.describe())

# Prints Yellow as top frequent in DataFrame
print(statistics.mode(series))
