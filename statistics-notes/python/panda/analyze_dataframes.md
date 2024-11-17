# Analyze DataFrames

## Get type of variable

```python
type(data_frame_variable)

# outputs pandas.core.frame.DataFrame
```

## Print all columns from DataFrame

```python
print(data_frame_variable.columns)

# outputs Index object representation with columns
```

## Describe data from DataFrame

[source](https://saturncloud.io/blog/python-spyder-display-all-columns-of-a-pandas-dataframe-in-describe/#:~:text=describe()%20method%20in%20Pandas,and%20maximum%20of%20the%20columns.)

The `.describe()` method in Pandas is a convenient way to get a quick overview of your data. By default, it provides the
count, mean, standard deviation, minimum, 25th percentile (Q1), median (50th percentile or Q2), 75th percentile (Q3),
and maximum of the columns.
