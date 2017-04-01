from csvReader import CsvReader

class Validator:

    def __init__(self, filename):

        # Parse the csv file that contains the data set
        csvParser = CsvReader(filename)

        # Get the targetAttribute value vector from the data set
        self.targetAttribute = csvParser.targetAttribute
        
        # Get the attribute value matrix from the data set
        self.data = csvParser.data

    def calculateAccuracy(self, root):

        # If the decision tree or the data set is empty, return accuracy as 0
        if root == None or len(self.data) == 0:
            return 0

        # Count the total number of correct predictions made by the decision tree
        count = 0
        for i in range(len(self.data)):
            if self.getPredictedValue(root, self.data[i]) == self.targetAttribute[i]:
                count += 1

        # Calculate and return the prediction accuracy
        self.accuracy = 1.0 * count / len(self.data)
        return self.accuracy

    def getPredictedValue(self, root, row):

        # Return the predicted class value if reaches at a leaf node
        if root.val == -1:
            return root.label

        # If an attribute value is 0, search in the left subtree
        if row[root.val] == 0:
            return self.getPredictedValue(root.left, row)

        # If an attribute value is 1, search in the right subtree
        else:
            return self.getPredictedValue(root.right, row)

    def displayAccuracy(self):

        print "The testing accuracy is = {0:.2f}%".format((self.accuracy) * 100)
