# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as ptl

# food_consumption is Panda DataFrame
# print(food_consumption.columns)
#
# Outputs
# Index(['Unnamed: 0', 'country', 'food_category', 'consumption', 'co2_emission'], dtype='object')

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption.agg([np.mean, np.median]))

# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
ptl.show()
