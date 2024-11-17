# Import numpy with alias np
import numpy as np

# food_consumption is Panda DataFrame
# print(food_consumption.columns)
#
# Outputs
# Index(['Unnamed: 0', 'country', 'food_category', 'consumption', 'co2_emission'], dtype='object')

# Subset country for the USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_Consumption['consumption']))
