# Machine Learning

Machine learning is a subset of artificial intelligence focused on building systems that can learn from historical data, identify patterns, and make logical decisions with little to no human intervention. It is a data analysis method that automates the building of analytical models through using data that encompasses diverse forms of digital information including numbers, words, clicks and images.

### Machine Learning Needs
There are a multitude of use cases that machine learning can be applied to in order to cut costs, mitigate risks, and improve overall quality of life including recommending products/services, detecting cybersecurity breaches, and enabling self-driving cars. With greater access to data and computation power, machine learning is becoming more ubiquitous every day and will soon be integrated into many facets of human life.

### Machine Learning methods
#### What is supervised Machine Learning

Supervised machine learning algorithms use labeled data as training data where the appropriate outputs to input data are known. The machine learning algorithm ingests a set of inputs and corresponding correct outputs. The algorithm compares its own predicted outputs with the correct outputs to calculate model accuracy and then optimizes model parameters to improve accuracy.

Supervised machine learning relies on patterns to predict values on unlabeled data. It is most often used in automation, over large amounts of data records or in cases where there are too many data inputs for humans to process effectively. For example, the algorithm can pick up credit card transactions that are likely to be fraudulent or identify the insurance customer who will most probably file a claim.

#### What is unsupervised Machine Learning

Unsupervised machine learning is best applied to data that do not have structured or objective answer. There is no pre-determination of the correct output for a given input. Instead, the algorithm must understand the input and form the appropriate decision. The aim is to examine the information and identify structure within it.

Unsupervised machine learning works well on transactional information. For example, the algorithm can identify customer segments who possess similar attributes. Customers within these segments can then be targeted by similar marketing campaigns. Popular techniques used in unsupervised learning include nearest-neighbor mapping, self-organizing maps, singular value decomposition and k-means clustering. The algorithms are subsequently used to segment topics, identify outliers and recommend items.

![image](https://github.com/toggle-corp/ml-internship/assets/47474980/36d8bf0b-ade2-46f8-89a6-cf0c00a9edc9)

### Datasets

Dataset is essentially the backbone for all operations, techniques or models used by developers to interpret them. Datasets involve a large amount of data points grouped into one table. Datasets are used in almost all industries today for various reasons.

A dataset is a collection of data that contains data specific to its category and nothing else. This is used to develop Machine Learning models perform Data Analysis, Data and Feature Engineering. Datasets may be structured (Height, weight analysis) or unstructured (audio files, videos, images).

##### Types of Datasets
There are various types of datasets available out there. They are:

**Numerical Dataset**: They include numerical data points that can be solved with equations. These include temperature, humidity, marks and so on.
**Categorical Dataset**: These include categories such as colour, gender, occupation, games, sports and so on.
**Web Dataset**: These include datasets created by calling APIs using HTTP requests and populating them with values for data analysis. These are mostly stored in JSON (JavaScript Object Notation) formats.
**Time series Dataset**: These include datasets between a period, for example, changes in geographical terrain over time.
**Image Dataset**: It includes a dataset consisting of images. This is mostly used to differentiate the types of diseases, heart conditions and so on.
**Ordered Dataset**: These datasets contain data that are ordered in ranks, for example, customer reviews, movie ratings and so on.
**Partitioned Dataset**: These datasets have data points segregated into different members or different partitions.
**File-Based Datasets**: These datasets are stored in files, in Excel as .csv, or .xlsx files.
**Bivariate Dataset**: In this dataset, 2 classes or features are directly correlated to each other. For example, height and weight in a dataset are directly related to each other.
**Multivariate Dataset**: In these types of datasets, as the name suggests 2 or more classes are directly correlated to each other. For example, attendance, and assignment grades are directly correlated to a student’s overall grade.

#### Features of a Dataset
The features of a dataset may allude to the columns available in the dataset. The features of a dataset are the most critical aspect of the dataset, as based on the features of each available data point, will there be any possibility of deploying models to find the output to predict the features of any new data point that may be added to the dataset.

It is only possible to determine the standard features from some datasets since their functionalities and data would be completely different when compared to other datasets. Some possible features of a dataset are:

**Numerical Features**: These may include numerical values such as height, weight, and so on. These may be continuous over an interval, or discrete variables.
**Categorical Features**: These include multiple classes/ categories, such as gender, colour, and so on.
**Metadata**: Includes a general description of a dataset. Generally in very large datasets, having an idea/ description of the dataset when it’s transferred to a new developer will save a lot of time and improve efficiency.
**Size of the Data**: It refers to the number of entries and features it contains in the file containing the Dataset.
**Formatting of Data**: The datasets available online are available in several formats. Some of them are JSON (JavaScript Object Notation), CSV (Comma Separated Value), XML (eXtensible Markup Language), DataFrame, and Excel Files (xlsx or xlsm). For particularly large datasets, especially involving images for disease detection, while downloading the files from the internet, it comes in zip files which will be needed to extract in the system to individual components.
**Target Variable**: It is the feature whose values/attributes are referred to to get outputs from the other features with machine learning techniques.
**Data Entries**: These refer to the individual values of data present in the Dataset. They play a huge role in data analysis.

### Methods Used in Datasets
Many methods are applied when it involves working with Datasets. It depends on the reason you work with your given dataset. Some of the common methods that are applied to datasets are:

**1. Loading and Reading Datasets:**
Set of methods that are used in loading and reading the datasets initially to execute the required tasks.

`Eg – read_csv(), read_json(), read_excel() etc.`

**2. Exploratory Data Analysis:**
To perform Data Analysis and visualize it, we use these functions on a dataset to work.

`Eg – head(), tail(), groupby() etc`

**3. Data Preprocessing:**
Before analyzing a dataset, it is preprocessed to remove erroneous values, and mislabeled data points by using specific methods.

`Eg – drop(), fillna(), dropna(), copy() etc`

**4. Data Manipulation:**
Data points in the dataset are arranged/ rearranged to manipulate the features. At some points, even features of the dataset are manipulated to decrease computational complexity and so on. This may involve methods or functions merging columns, adding new data points, and so on.

`Eg – merge(), concat(), join() etc`

**5. Data Visualization:**
Methods used to explain the dataset to people not in the technical field like – the use of bar graphs and charts to provide a pictorial representation of the dataset of the company/ business.

`Eg – plot()`

**6. Data Indexing, Data Subsets:**
Methods that are used to refer to a particular feature in a dataset, we use data indexing or create definitive subsets.

`Eg – iloc()`

**7. Export Data:**
Methods that are used in exporting the data you’ve worked on in different formats as required.

`Eg – to_csv(), to_json() etc`

### Data splits
Go to the below link:
[Dataset splits - Training, Validation, and Test sets](https://mlu-explain.github.io/train-test-validation/#:~:text=It%20is%20best%20practice%20in,final%20evaluation%20of%20the%20model.)

### What is Underfitting and Overfitting; Bias-Variance Tradeoffs

[Underfitting and Overfitting](https://medium.com/geekculture/overfitting-underfitting-and-bias-variance-tradeoff-9e83f4a147c)

### Concept on Hyper-parameters
[Hyper-parameters](https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac)

### Classification Algorithms
[Classification and Algorithms](https://monkeylearn.com/blog/classification-algorithms/)