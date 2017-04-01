Hi,
	1.To run this program input following command:

	python main.py K training_set.csv validation_set.csv test_set.csv 1


	
	python main.py 0 training_set.csv validation_set.csv test_set.csv 1


	
	python main.py 2 training_set.csv validation_set.csv test_set.csv 1


	
	python main.py 3 training_set.csv validation_set.csv test_set.csv 1



	python main.py 6 training_set.csv validation_set.csv test_set.csv 1



	python main.py 10 training_set.csv validation_set.csv test_set.csv 1



	K represent the number of node you want to prune after generating the decision tree. The end number "1" represent whether to print the pruned tree or not.
	
	2.For the code files:
	
	main.py is the entrance of the program; csvReader.py is used for reading data from csv files; validator.py is used for validating the decision tree formed by
	using trainning data; decisionTree is the function that forming the DT and using ID3 algorithm to create the compact tree.

	3.Please make sure the data1/ and data2/ are at the same directory with the code file.

	4.For the out put, sometimes pruned accuracy is better than original decision tree, however, sometimes it sucks.
	If you want to change dataset1 to dataset2, please open main.py using Notepad change the "dataDir = './data_sets1/'" to "dataDir = './data_sets2/'" at 16 line.

	Thank you for you patient and have a good day!

	Fan Chen 				2021277377   fxc151230