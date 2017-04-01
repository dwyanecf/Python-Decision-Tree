/*
* Name: Ximeng Zhao
*UTD ID : 2021240896
*Net ID : xxz145830
*/

(I) Run the command line:
 
Format: python main.py k training_set.csv validation_set.csv test_set.csv 1

where k is the number of nodes to prune and 1 is to print the original decision tree and the decision tree after post pruning. If you enter zero, it will not print the original decision tree.


(II) File content

main.py --- The main program to test the decision tree learning algorithm and post pruning algorithm.

csvParser.py --- A python class that parses a csv file that contains the data set and retrieve the attribute names, attribute values, and class values in the data set.

validator.py --- A python class that calculates the prediction accuracy of a given decision tree on either validation data or test data.

decisionTree.py --- A python class that implements the decision tree learning and post pruning algorithms as well as the decision tree data structure.

README.txt --- A description of the file.

data1/   
    training_set.csv
    validation_set.csv
    test_set.csv

data2/  
    training_set.csv
    validation_set.csv
    test_set.csv


(III) Output result and summary:

Please take a look at the output and result summary folder, which contains original decision tree plot and decision tree after applying post pruning based on five different nodes to prune. And it also covers the analysis of accuracy result for both dataset1 and dataset2.

The program will print the prediction accuracy before and after post pruning, as well as the decision tree after post pruning.

Note: 
    To switch data set, change the dataDir in main.py from './data1/' to './data2/'