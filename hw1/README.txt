/** 
* Name: Liang Shi
*UTD ID : 2021245632
*Net ID : lxs143430
*/

(I) Purpose

1. Implement and test the decision tree learning algorithm using Gain Ratio formula for deciding on the best attribute for tree branching.

2. Fully grow the tree to fit training data and apply following post pruning algorithm. Take two integer numbers L and K as input.

3. Implement a function to print the decision tree to standard output.

4. Input parameters for your program are following:
       L K training-dataset validation-dataset test-dataset

(II) File List

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

output1/ 
    summary.txt  --- A summary file that report the accuracy on test dataset 1 using the post-pruned decision tree. 5 different combinations of L and K values are tried.
    tree_before_pruning.txt  --- The original decision tree built on training data 1.
    tree_after_pruning.txt   --- The decision tree which produces best accuracy on test data 1.
    pruned_trees/  --- The pruned decision trees generated by 5 different combinations of L and K values.

output2/ 
    summary.txt  --- A summary file that report the accuracy on test dataset 2 using the post-pruned decision tree. 5 different combinations of L and K values are tried.
    tree_before_pruning.txt  --- The original decision tree built on training data 2.
    tree_after_pruning.txt   --- The decision tree which produces best accuracy on test data 2.
    pruned_trees/  --- The pruned decision trees generated by 5 different combinations of L and K values

(III) How to Run the Program

To test the program, you need python 2.7.X installed on your PC.
8 
Open a terminal, go to the current path. (Mac OS X)Type in:

    python main.py 10 5 training_set.csv validation_set.csv test_set.csv 

The program will print the prediction accuracy before and after post pruning, as well as the decision tree after post pruning.

Note: 
    To export the decision tree, uncomment line 26 and 48 in main.py.
    To print the decision tree before pruning, uncomment line 27 in main.py.
    To switch data set, change the dataDir from './data1/' to './data2/'