<div align="center">
  <h1> 🎩 dslr
  </h1>
</div>

---

Data Science × Logistic Regression.<br>
In this project, we will continue our journey of the machine learning.<br>
We will learn how to read a data set, visualize it in different ways, and select and clean unnecessary information.
& we will train logistic regression model that will solve classification problem.

![Static Badge](https://img.shields.io/badge/language-python_3-yellow)

## Summary

- [Installation](#installation)
- [Programs](#programs)
- [Documentation](#documentation)
  - [Data Analysis](#data-analysis)
    - [Describe](#describe)
  - [Data Visualization](#data-visualization)
    - [Histogram](#histogram)
    - [Scatter Plot](#scatter-plot)
    - [Pair Plot](#pair-plot)
- [Sources](#sources)


## Installation

Clone the project

```bash
  git clone https://github.com/drabiot/dslr.git
```

Go to the project directory

```bash
  cd dslr
```

Generate the environment

```bash
  ./setup.sh
```

## Programs

| Programs | Description | Arguments |
| -------- | ----------- | --------- |
| [describe.py](#describe) | Take a dataset and return the dataset with pandas.description() | *.csv |
| [histogram.py](#histogram) | Take a dataset & display an histogram of the most homogeneous score distribution between all four houses | *.csv |
| [scatter_plot.py](#scatter-plot) | Take a dataset & display a scatter plot of the two feature that are the most similar | *.csv |
| [pair_plot.py](#pair-plot) | Take a dataset & display his pair plot | *.csv |
|  |  |  |
|  |  |  |

## Documentation

## Data Analysis

All the data analysis programs are in the file `data_analysis`

### DESCRIBE
Take a dataset and return the dataset with pandas.description().

```bash
./data_analysis/describe.py <dataset>
./data_analysis/describe.py datasets/dataset_test.csv
```

For example, here what you're supposed to have in result:
```
                Arithmancy    Astronomy    Herbology  Defense Against the Dark Arts   Divination  Muggle Studies  Ancient Runes  History of Magic  Transfiguration      Potions  Care of Magical Creatures       Charms       Flying
Total Count    1600.000000  1600.000000  1600.000000                    1600.000000  1600.000000     1600.000000    1600.000000       1600.000000      1600.000000  1600.000000                1600.000000  1600.000000  1600.000000
Count          1566.000000  1568.000000  1567.000000                    1569.000000  1561.000000     1565.000000    1565.000000       1557.000000      1566.000000  1570.000000                1560.000000  1600.000000  1600.000000
Mean          49634.570243    39.797131     1.141020                      -0.387863     3.153910     -224.589915     495.747970          2.963095      1030.096946     5.950373                  -0.053427  -243.374409    21.958012
Std           16679.806036   520.298268     5.219682                       5.212794     4.155301      486.344840     106.285165          4.425775        44.125116     3.147854                   0.971457     8.783640    97.631602
Min          -24370.000000  -966.740546   -10.295663                     -10.162119    -8.727000    -1086.496835     283.869609         -8.858993       906.627320    -4.697484                  -3.313676  -261.048920  -181.470000
25%           38511.500000  -489.551387    -4.308182                      -5.259095     3.099000     -577.580096     397.511047          2.218653      1026.209993     3.646785                  -0.671606  -250.652600   -41.870000
50%           49013.500000   260.289446     3.469012                      -2.589342     4.624000     -419.164294     463.918305          4.378176      1045.506996     5.874837                  -0.044811  -244.867765    -2.515000
75%           60811.250000   524.771949     5.419183                       4.904680     5.667000      254.994857     597.492230          5.825242      1058.436410     8.248173                   0.589919  -232.552305    50.560000
Max          104956.000000  1016.211940    11.612895                       9.667405    10.032000     1092.388611     745.396220         11.889713      1098.958201    13.536762                   3.056546  -225.428140   279.070000
```

## Data Visualization

All the data visualization programs are in the file `data_visualization`

### HISTOGRAM
Take a dataset & display an histogram of the most homogeneous score distribution between all four houses.

```bash
./data_visualization/histogram.py <dataset>
./data_visualization/histogram.py datasets/dataset_train.csv
```
<div align="center">
	<img width="639" height="475" alt="histogram" src="https://github.com/user-attachments/assets/a199bcbe-92b8-4a68-a077-6d9353cce4d5" />
</div>

The histogram need to have minimun one house entered.

To find the histogram we need to answer our problem, the algorithm compute every student course's note for each house & turn into his mean score.
Then he stock the variance of every course of each house, sort every variance & take the first one in the array to display the most homogeneous course between all four houses.

### SCATTER PLOT
Take a dataset & display a scatter plot of the two feature that are the most similar.

```bash
./data_visualization/scatter_plot.py <dataset>
./data_visualization/scatter_plot.py datasets/dataset_train.csv
```

<div align="center">
	<img width="639" height="475" alt="scatter_plot" src="https://github.com/user-attachments/assets/e9769997-7111-4d37-9f0c-9e89cf600578" />
</div>

The scatter plot need to have minimun one score entered.

To find the scatter plot we need to answer our problem, the algorithm loop to check every not checked course combo.
Then he extracts the correlation value between course 1 and course 2. If the new correction value is higher, modify course value by the new one & so on.

### PAIR PLOT
Take a dataset & display his pair plot.

```bash
./data_visualization/pair_plot.py <dataset>
./data_visualization/pair_plot.py datasets/dataset_train.csv
```

<div align="center">
	<img width="1198" height="918" alt="pair_plot" src="https://github.com/user-attachments/assets/acccd0b4-ba8b-4aca-8707-12eac29f8c18" />
</div>

## Sources
- Describe function https://www.expertpython.fr/lexique/describe()
- Matplotlib https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
- Histogram in Matplotlib https://www.w3schools.com/python/matplotlib_histograms.asp
- Pair Plot in Matplotlib https://www.geeksforgeeks.org/python/pairplot-in-matplotlib/
- Multiclass logistic regression One-vs-rest explanation https://youtu.be/EYXSve6T5BU
- Create One-vs-rest algo https://youtu.be/3lwicUTEgHs