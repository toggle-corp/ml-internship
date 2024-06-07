# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N0NspVFT4mgcPrR4JHLm92L29K1QsAI-

Introduction to Pandas

pandas is a Python package providing fast, flexible, and expressive data structures designed to work with relational or labeled data both. It is a fundamental high-level building block for doing practical, real world data analysis in Python.

pandas is well suited for:

    - Tabular data with heterogeneously-typed columns, as in an SQL table or - - Excel spreadsheet
    - Ordered and unordered (not necessarily fixed-frequency) time series data.
    - Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels
    - Any other form of observational / statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure

Key features:

    - Easy handling of missing data
    - Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
    - Automatic and explicit data alignment: objects can be explicitly aligned to a set of labels, or the data can be aligned automatically
    - Powerful, flexible group by functionality to perform split-apply-combine operations on data sets
    - Intelligent label-based slicing, fancy indexing, and subsetting of large data sets
    - Intuitive merging and joining data sets
    - Flexible reshaping and pivoting of data sets
    - Hierarchical labeling of axes
    - Robust IO tools for loading data from flat files, Excel files, databases, and HDF5
    - Time series functionality: date range generation and frequency conversion, moving window statistics, moving window linear regressions, date shifting and lagging, etc.

## Series
A Series is a single vector of data (like a NumPy 1-d array) with an index that labels each element in the vector.
"""

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print ("Labels:", labels)
print("My data:", my_data)
print("Dictionary:", d)

"""### Creating a Series (Pandas class)
* From numerical data only
* From numerical data and corresponding index (row labels)
* From NumPy array as the source of numerical data
* Just using a pre-defined dictionary
"""

pd.Series(data=my_data) # Output looks very similar to a NumPy array

"""If an index is not specified, a default sequence of integers is assigned as the index. A NumPy array comprises the values of the Series, while the index is a pandas Index object."""

pd.Series(data=my_data, index=labels) # Note the extra information about index

# Inputs are in order of the expected parameters (not explicitly named), NumPy array is used for data
pd.Series(arr, labels)

pd.Series(d) # Using a pre-defined Dictionary object

"""### What type of values can a Pandas Series hold?"""

print ("\nHolding numerical data\n",'-'*25, sep='')
print(pd.Series(arr))
print ("\nHolding text labels\n",'-'*20, sep='')
print(pd.Series(labels))
print ("\nHolding functions\n",'-'*20, sep='')
print(pd.Series(data=[sum,print,len]))
print ("\nHolding objects from a dictionary\n",'-'*40, sep='')
print(pd.Series(data=[d.keys, d.items, d.values]))

"""### Indexing and slicing"""

ser1 = pd.Series([1,2,3,4],['CA', 'OR', 'CO', 'AZ'])
ser2 = pd.Series([1,2,5,4],['CA', 'OR', 'NV', 'AZ'])

print ("\nIndexing by name of the item/object (string identifier)\n",'-'*56, sep='')
print("Value for CA in ser1:", ser1['CA'])
print("Value for AZ in ser1:", ser1['AZ'])
print("Value for NV in ser2:", ser2['NV'])

print ("\nIndexing by number (positional value in the series)\n",'-'*52, sep='')
print("Value for CA in ser1:", ser1[0])
print("Value for AZ in ser1:", ser1[3])
print("Value for NV in ser2:", ser2[2])

print ("\nIndexing by a range\n",'-'*25, sep='')
print ("Value for OR, CO, and AZ in ser1:\n", ser1[1:4], sep='')

"""### Adding/Merging two series with common indices"""

ser1 = pd.Series([1,2,3,4],['CA', 'OR', 'CO', 'AZ'])
ser2 = pd.Series([1,2,5,4],['CA', 'OR', 'NV', 'AZ'])
ser3 = ser1+ser2

print ("\nAfter adding the two series, the result looks like this...\n",'-'*59, sep='')
print(ser3)
print("\nPython tries to add values where it finds common index name, and puts NaN where indices are missing\n")

print ("\nThe idea works even for multiplication...\n",'-'*43, sep='')
print (ser1*ser2)

print ("\nOr even for combination of mathematical operations!\n",'-'*53, sep='')
print (np.exp(ser1)+np.log10(ser2))

"""# DataFrame (the Real Meat!)

> A DataFrame is a tabular data structure, encapsulating multiple series like columns in a spreadsheet. Data are stored internally as a 2-dimensional object, but the DataFrame allows us to represent and manipulate higher-dimensional data.


"""

from numpy.random import randn as rn

"""## Creating and accessing DataFrame
* Indexing
* Adding and deleting rows and columns
* Subsetting DataFrame
"""

np.random.seed(101)
matrix_data = rn(5,4)
row_labels = ['A','B','C','D','E']
column_headings = ['W','X','Y','Z']

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe data frame looks like\n",'-'*45, sep='')
print(df)

"""### Indexing and slicing (columns)
* By bracket method
* By DOT method (NOT recommended)
"""

print("\nThe 'X' column\n",'-'*25, sep='')
print(df['X'])
print("\nType of the column: ", type(df['X']), sep='')
print("\nThe 'X' and 'Z' columns indexed by passing a list\n",'-'*55, sep='')
print(df[['X','Z']])
print("\nType of the pair of columns: ", type(df[['X','Z']]), sep='')
print ("\nSo, for more than one column, the object turns into a DataFrame")

print("\nThe 'X' column accessed by DOT method (NOT recommended)\n",'-'*55, sep='')
print(df.X)

"""### Creating and deleting a (new) column (or row)"""

print("\nA column is created by assigning it in relation to an existing column\n",'-'*75, sep='')
df['New'] = df['X']+df['Z']
df['New (Sum of X and Z)'] = df['X']+df['Z']
print(df)
print("\nA column is dropped by using df.drop() method\n",'-'*55, sep='')
df = df.drop('New', axis=1) # Notice the axis=1 option, axis = 0 is default, so one has to change it to 1
print(df)
df1=df.drop('A')
print("\nA row (index) is dropped by using df.drop() method and axis=0\n",'-'*65, sep='')
print(df1)
print("\nAn in-place change can be done by making inplace=True in the drop method\n",'-'*75, sep='')
df.drop('New (Sum of X and Z)', axis=1, inplace=True)
print(df)

"""### Selecting/indexing Rows
* Label-based 'loc' method
* Index (numeric) 'iloc' method
"""

print("\nLabel-based 'loc' method can be used for selecting row(s)\n",'-'*60, sep='')
print("\nSingle row\n")
print(df.loc['C'])
print("\nMultiple rows\n")
print(df.loc[['B','C']])
print("\nIndex position based 'iloc' method can be used for selecting row(s)\n",'-'*70, sep='')
print("\nSingle row\n")
print(df.iloc[2])
print("\nMultiple rows\n")
print(df.iloc[[1,2]])

"""### Subsetting DataFrame"""

np.random.seed(101)
matrix_data = rn(5,4)
row_labels = ['A','B','C','D','E']
column_headings = ['W','X','Y','Z']
df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)

print("\nThe DatFrame\n",'-'*45, sep='')
print(df)
print("\nElement at row 'B' and column 'Y' is\n")
print(df.loc['B','Y'])
print("\nSubset comprising of rows B and D, and columns W and Y, is\n")
df.loc[['B','D'],['W','Y']]

"""## Conditional selection, index (re)setting, multi-index

### Basic idea of conditional check and Boolean DataFrame
"""

print("\nThe DataFrame\n",'-'*45, sep='')
print(df)
print("\nBoolean DataFrame(s) where we are checking if the values are greater than 0\n",'-'*75, sep='')
print(df>0)
print("\n")
print(df.loc[['A','B','C']]>0)
booldf = df>0
print("\nDataFrame indexed by boolean dataframe\n",'-'*45, sep='')
print(df[booldf])

"""### Passing Boolean series to conditionally subset the DataFrame"""

matrix_data = np.matrix('22,66,140;42,70,148;30,62,125;35,68,160;25,62,152')
row_labels = ['A','B','C','D','E']
column_headings = ['Age', 'Height', 'Weight']

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nA new DataFrame\n",'-'*25, sep='')
print(df)
print("\nRows with Height > 65 inch\n",'-'*35, sep='')
print(df[df['Height']>65])

booldf1 = df['Height']>65
booldf2 = df['Weight']>145
print("\nRows with Height > 65 inch and Weight >145 lbs\n",'-'*55, sep='')
print(df[(booldf1) & (booldf2)])

print("\nDataFrame with only Age and Weight columns whose Height > 65 inch\n",'-'*68, sep='')
print(df[booldf1][['Age','Weight']])

"""### Re-setting and Setting Index"""

matrix_data = np.matrix('22,66,140;42,70,148;30,62,125;35,68,160;25,62,152')
row_labels = ['A','B','C','D','E']
column_headings = ['Age', 'Height', 'Weight']

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe DataFrame\n",'-'*25, sep='')
print(df)
print("\nAfter resetting index\n",'-'*35, sep='')
print(df.reset_index())
print("\nAfter resetting index with 'drop' option TRUE\n",'-'*45, sep='')
print(df.reset_index(drop=True))
print("\nAdding a new column 'Profession'\n",'-'*45, sep='')
df['Profession'] = "Student Teacher Engineer Doctor Nurse".split()
print(df)
print("\nSetting 'Profession' column as index\n",'-'*45, sep='')
print (df.set_index('Profession'))

"""### Multi-indexing"""

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

print("\nTuple pairs after the zip and list command\n",'-'*45, sep='')
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print("\nIndex hierarchy\n",'-'*25, sep='')
print(hier_index)
print("\nIndex hierarchy type\n",'-'*25, sep='')
print(type(hier_index))

print("\nCreating DataFrame with multi-index\n",'-'*37, sep='')
np.random.seed(101)
df1 = pd.DataFrame(data=np.round(rn(6,3),2), index= hier_index, columns= ['A','B','C'])
print(df1)

print("\nSubsetting multi-index DataFrame using two 'loc' methods\n",'-'*60, sep='')
print(df1.loc['G2'].loc[[1,3]][['B','C']])

print("\nNaming the indices by 'index.names' method\n",'-'*45, sep='')
df1.index.names=['Outer', 'Inner']
print(df1)

"""### Cross-section ('XS') command"""

print("\nGrabbing a cross-section from outer level\n",'-'*45, sep='')
print(df1.xs('G1'))
print("\nGrabbing a cross-section from inner level (for all outer levels)\n",'-'*65, sep='')
print(df1.xs(2,level='Inner'))

"""## Missing Values"""

df = pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]})
df['States']="CA NV AZ".split()
df.set_index('States',inplace=True)
print(df)

"""### Pandas 'dropna' method"""

print("\nDropping any rows with a NaN value\n",'-'*35, sep='')
print(df.dropna(axis=0))
print("\nDropping any column with a NaN value\n",'-'*35, sep='')
print(df.dropna(axis=1))
print("\nDropping a row with a minimum 2 NaN value using 'thresh' parameter\n",'-'*68, sep='')
print(df.dropna(axis=0, thresh=2))

"""### Pandas 'fillna' method"""

print("\nFilling values with a default value\n",'-'*35, sep='')
print(df.fillna(value='FILL VALUE'))
print("\nFilling values with a computed value (mean of column A here)\n",'-'*60, sep='')
print(df.fillna(value=df['A'].mean()))

"""## GroupBy method"""

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df

byComp = df.groupby('Company')
print("\nGrouping by 'Company' column and listing mean sales\n",'-'*55, sep='')
print(byComp.mean(numeric_only=True))
print("\nGrouping by 'Company' column and listing sum of sales\n",'-'*55, sep='')
print(byComp.sum())
# Note dataframe conversion of the series and transpose
print("\nAll in one line of command (Stats for 'FB')\n",'-'*65, sep='')
print(pd.DataFrame(df.groupby('Company').describe().loc['FB']).transpose())
print("\nSame type of extraction with little different command\n",'-'*68, sep='')
print(df.groupby('Company').describe().loc[['GOOG', 'MSFT']])

"""## Merging, Joining, Concatenating
### Concatenation
"""

# Creating data frames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8,9,10,11])

print("\nThe DataFrame number 1\n",'-'*30, sep='')
print(df1)
print("\nThe DataFrame number 2\n",'-'*30, sep='')
print(df2)
print("\nThe DataFrame number 3\n",'-'*30, sep='')
print(df3)

df_cat1 = pd.concat([df1,df2,df3], axis=0)
print("\nAfter concatenation along row\n",'-'*30, sep='')
print(df_cat1)

df_cat2 = pd.concat([df1,df2,df3], axis=1)
print("\nAfter concatenation along column\n",'-'*60, sep='')
print(df_cat2)
df_cat2.fillna(value=0, inplace=True)
print("\nAfter filling missing values with zero\n",'-'*60, sep='')
print(df_cat2)

"""### Merging by a common 'key'
The **merge** function allows you to merge DataFrames together using a similar logic as merging SQL Tables together.
"""

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

print("\nThe DataFrame 'left'\n",'-'*30, sep='')
print(left)
print("\nThe DataFrame 'right'\n",'-'*30, sep='')
print(right)

merge1= pd.merge(left,right,how='inner',on='key')
print("\nAfter simple merging with 'inner' method\n",'-'*50, sep='')
print(merge1)

"""### Merging on a set of keys"""

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

left

right

pd.merge(left, right, on=['key1', 'key2'])

pd.merge(left, right, how='outer',on=['key1', 'key2'])

pd.merge(left, right, how='left',on=['key1', 'key2'])

pd.merge(left, right, how='right',on=['key1', 'key2'])

"""### Joining
Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a single DataFrame based on **'index keys'**.
"""

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

left

right

left.join(right)

left.join(right, how='outer')

"""## Useful operations
### head() and unique values
* head()
* unique()
* nunique()
* value_count()
"""

import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10],
                   'col2':[444,555,666,444,333,222,666,777,666,555],
                   'col3':'aaa bb c dd eeee fff gg h iii j'.split()})
df

print("\nMethod head() is for showing first few entries\n",'-'*50, sep='')
df.head()

print("\nFinding unique values in 'col2'\n",'-'*40, sep='') # Note 'unique' method applies to pd.series only
print(df['col2'].unique())

print("\nFinding number of unique values in 'col2'\n",'-'*45, sep='')
print(df['col2'].nunique())

print("\nTable of unique values in 'col2'\n",'-'*40, sep='')
t1=df['col2'].value_counts()
print(t1)

"""### Applying functions
Pandas work with **'apply'** method to accept any user-defined function
"""

# Define a function
def testfunc(x):
    if (x> 500):
        return (10*np.log10(x))
    else:
        return (x/10)

df['FuncApplied'] = df['col2'].apply(testfunc)
print(df)

"""**Apply works with built-in function too!**"""

df['col3length']= df['col3'].apply(len)
print(df)

"""**Combine 'apply' with lambda expession for in-line calculations**"""

df['FuncApplied'].apply(lambda x: np.sqrt(x))

"""**Standard statistical functions directly apply to columns**"""

print("\nSum of the column 'FuncApplied' is: ",df['FuncApplied'].sum())
print("Mean of the column 'FuncApplied' is: ",df['FuncApplied'].mean())
print("Std dev of the column 'FuncApplied' is: ",df['FuncApplied'].std())
print("Min and max of the column 'FuncApplied' are: ",df['FuncApplied'].min(),"and",df['FuncApplied'].max())

"""### Deletion, sorting, list of column and row names

**Getting the names of the columns**
"""

print("\nName of columns\n",'-'*20, sep='')
print(df.columns)
l = list(df.columns)
print("\nColumn names in a list of strings for later manipulation:",l)

"""**Deletion by 'del' command** # This affects the dataframe immediately, unlike drop method."""

print("\nDeleting last column by 'del' command\n",'-'*50, sep='')
del df['col3length']
print(df)
df['col3length']= df['col3'].apply(len)

"""**Sorting and Ordering a DataFrame **"""

df.sort_values(by='col2') #inplace=False by default

df.sort_values(by='FuncApplied',ascending=False) #inplace=False by default

"""**Find Null Values or Check for Null Values**"""

df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()

df.isnull()

df.fillna('FILL')

"""**Pivot Table**"""

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df

# Index out of 'A' and 'B', columns from 'C', actual numerical values from 'D'
df.pivot_table(values='D',index=['A', 'B'],columns=['C'])

# Index out of 'A' and 'B', columns from 'C', actual numerical values from 'D'
df.pivot_table(values='D',index=['A', 'B'],columns=['C'], fill_value='FILLED')

