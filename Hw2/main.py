import sys
from decisionTree import DecisionTree
from validator import Validator
    
def main():
	
	# Check if the number of command line arguments is correct
	if len(sys.argv) < 6:
	  print("-- python --|-- main.py -- |-- K --|-- training_set.csv --|-- validation_set.csv --|-- test_set.csv --|--print--")
	  sys.exit(1)

	# The program takes two integer L and K as input to prune the decision tree
	K = int(sys.argv[1])

	# Get the file path of the training data, validation data and test data
	dataDir = './data_sets1/'
	training_set = dataDir + sys.argv[2]
	validation_set = dataDir + sys.argv[3]
	test_set = dataDir + sys.argv[4]
	L = int(sys.argv[5])

	# Build a decision tree on training data
	decisionTree = DecisionTree(training_set)

	#############################################
	# decisionTree.exportTree('tree.txt')
        if L == 1:
            print decisionTree
	#############################################

	# Create a validator using test data to calculate the prediction accuracy of a given decision tree 
	validator = Validator(test_set)

	# Calculate the prediction accuracy of the original decision tree on test data
	validator.calculateAccuracy(decisionTree.root)

	# Display the prediction accuracy before pruning
	print "\nA decision tree is fully grown to fit the training data." 
	validator.displayAccuracy()

	# Post pruning the decision tree
	print "\nPost prunning", '.' * 30
#print K =", K, ", the pruned decision tree is:\n"

	# Prune the original decision tree using K and validation data as inputs
	decisionTree.pruneTree(1, K, validation_set)

	##############################################
	# decisionTree.exportTree('pruned_tree.txt')
	##############################################
    
	# print the decision tree to standard output
	print decisionTree  # Override the __str__ method in DecisionTree class

	# Calculate the prediction accuracy of the pruned decision tree on test data
	validator.calculateAccuracy(decisionTree.root)

	# Display the prediction accuracy after pruning
	validator.displayAccuracy()

# Boiler plate function
if __name__ == '__main__':
    main()

