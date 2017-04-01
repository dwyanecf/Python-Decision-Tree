import csv

class CsvReader:

    def __init__(self, filename):

        # Create a matrix to store the attribute values
        self.data = []

        # Retrieve attribue names and values from the csv file
        with open(filename,'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ',')
            count = 0
            for row in csvreader:
                # Retrieve the attribute names from the header of the csv file 
                if count == 0:
                    self.attributeNames = row[:-1]
                # Retrieve the attribute values in the following rows
                else: 
                    self.data.append([int(i) for i in row])
                count += 1
                
        # Create a list to record the column index of the attributes
        self.attributes = range(len(self.attributeNames))

        # Create a list to record the row index of the example instances [[],[]...[]]
        self.examples = range(len(self.data))

        # Create a vector of the class values in the data set: class values[]
        self.targetAttribute = [row[-1] for row in self.data]
