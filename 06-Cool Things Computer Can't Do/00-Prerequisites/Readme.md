# Pre-requisite Libraries for ML in Python

1. Numpy
1. Pandas
1. Matplotlib
1. Seaborn
1. Plotly

# Numpy

NumPy is a low level library written in C and FORTRAN for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

It cleverly overcomes the problem of running slower algorithms on Python using multidimentional arrays and functions that operates on arrays. Any algorithm can then be expressed as a function on arrays, allowing the algorithms to be run quickly.

NumPy’s main object is the homogeneous multidimensional array called `N-d array`. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers.

In NumPy dimensions are called **axes**.

NumPy’s array class is called **ndarray**. It is also known by the alias **array**.

- NumPy arrays have a fixed size at creation and are homogeneous.
- The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

Numpy arrays are faster, occupy less memory and is much convenient than python list.

# Pandas

Pandas is a library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

It is a popular Python library used for working in tabular data (similar to the data stored in a spreadsheet).

Pandas provides helper functions to read data from various file formats like CSV, Excel spreadsheets, HTML tables, JSON, SQL, and more.

Unlike Numpy where we have only 1 DS (nd array), in pandas we have a lot of DS (eg. Dataframes, Series).

Dataframes are tablular data and series is a row or column selected from the table.

Dataframes have rows and columns and series have index and data.

CSV aka Comma Seperated Files are a common format for data.
