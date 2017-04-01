import math
import random
import copy
from collections import deque
from csvReader import CsvReader
from validator import Validator

class TreeNode:

    def __init__(self, val, left=None, right=None):

        self.val = val
        self.label = -1
        self.left  = left
        self.right = right

class DecisionTree:

    def __init__(self, filename):

        # get the csv file that contains the training data, extract the attributes names, 
        # attribute values, and class values.
        csvParser = CsvReader(filename)

        self.attributeNames = csvParser.attributeNames
        self.data = csvParser.data
        self.attributes = csvParser.attributes
        self.examples = csvParser.examples
        self.targetAttribute = csvParser.targetAttribute

        # Build a decision tree using ID3 algorithm.
        self.root = self.ID3(self.examples, self.targetAttribute, self.attributes)
    
    def ID3(self, Examples, Target_Attribute, Attributes):

        # If training Examples is empty, return null
        if len(Examples) == 0:
            return None
        
        # Create a root node for the tree
        root = TreeNode(-1)
        
        # Calculate the entropy of the Examples
        Entropy = self.getEntropy(Examples, Target_Attribute)

        # Let the label of the root node be the most common value of the
        # Target_Attribute in Examples
        root.label = self.getMostCommonValue(Target_Attribute)
        
        # If all Examples are positive, Return the single-node tree Root, with label = +
        # If all Examples are negative, Return the single-node tree Root, with label = -
        # If Attributes is empty, Return the single-node tree Root, with label = most common value 
        # of Target_Attribute in Examples
        if Entropy == 0 or len(Attributes) == 0:
            return root

        # Otherwise, choose the attribute from Attributes that best* classifies Examples
        else:
            bestAttribute = self.chooseBestAttribute(Examples, Target_Attribute, Attributes, Entropy)
            
            # If all attributes have a split info of zero(cannot be further splited), reutrn Root
            if bestAttribute == -1:
                return root

            # Otherwise, let bestAttribute be the decision attribute for Root
            root.val = bestAttribute

            # Get the list of other attributes that may be tested by the learned decision tree.
            # Attributes - {bestAttribute}
            newAttributes = []
            for attribute in Attributes:
                if attribute != bestAttribute:
                    newAttributes.append(attribute)
            Attributes = newAttributes

            # For each possible value, vi, of bestAttribute, Add a new tree branch below Root, 
            # corresponding to the test bestAttribute = vi
            branch = self.split(Examples, Target_Attribute, bestAttribute)
            # Add a subtree below each branch
            root.left = self.ID3(branch[0][0], branch[0][1], Attributes)
            root.right = self.ID3(branch[1][0], branch[1][1], Attributes)

            return root        

    def chooseBestAttribute(self, Examples, Target_Attribute, Attributes, Entropy):

        # Initialize the maximum Gain Ratio and best attribute as -1.
        maxGainRatio = -1
        bestAttribute = -1

        # print '['
        # Select the best attribute from the attributes list using Gain Ratio formula.
        for attribute in Attributes:

            # Calculate the split information for each attribute
            splitInfo = self.getSplitInfo(Examples, attribute)
            
            # If the attribute can be further splited, calculate the gain ratio of the attribute
            if splitInfo > 0:
                gainRatio = self.getInfoGain(Examples, Target_Attribute, Entropy, attribute) / splitInfo
                # print '(X', str(unichr(66 + attribute)), ',', Decimal(gainRatio), ')'
                if gainRatio > maxGainRatio:
                    maxGainRatio = gainRatio
                    bestAttribute = attribute
        # print ']'
        # print '--->>> X', str(unichr(66 + bestAttribute)), 'is selected!\n'

        # Return the best attribute using Gain Ratio measure
        return bestAttribute

    def getMostCommonValue(self, Target_Attribute):

        # If there is only one training example, return its corresponding class value.
        if len(Target_Attribute) == 1:
            return Target_Attribute[0]

        # Otherwise return the most common class value in the training example.
        count = 0
        for i in range(len(Target_Attribute)):
            if Target_Attribute[i] == 1:
                count += 1

        if count >= len(Target_Attribute) / 2:
            return 1
        else:
            return 0 

    def split(self, Examples, Target_Attribute, attribute):

        # Split the training example by their values for a given attribute.
        example_v0 = []
        example_v1 = []
        targets_v0 = []
        targets_v1 = []

        for i in range(len(Examples)):
            if self.data[Examples[i]][attribute] == 0:
                example_v0.append(Examples[i])
                targets_v0.append(Target_Attribute[i])
            else:
                example_v1.append(Examples[i])
                targets_v1.append(Target_Attribute[i])

        return [(example_v0, targets_v0), (example_v1,targets_v1)]

    def getSplitInfo(self, Examples, attribute):

        # Count the total number of examples
        rows = len(Examples)

        # Count the number of examples whose value for the given attribute is 0.
        s0 = 0
        for instance in Examples:
          if self.data[instance][attribute] == 0:
              s0 += 1

        # Calculate the percentage of the examples whose value for a given attribute is 0 or 1.
        percentage_s0 = 1.0 * s0 / rows
        percentage_s1 = 1 - percentage_s0
        
        # Define log 0 = 0 
        if percentage_s0 == 0 or percentage_s1 == 0:
            return 0

        # Return the split information
        return -(percentage_s0 * math.log(percentage_s0, 2) + percentage_s1 * math.log(percentage_s1, 2))

    def getEntropy(self, Examples, Target_Attribute):

        # Count the total number of examples
        rows = len(Examples)

        # Count the number of examples whose class value is positive.
        pcount = 0
        for i in range(len(Examples)):
          if Target_Attribute[i] == 1:
              pcount += 1
        
        # Calculate the percentage of the examples whose class value is negative or positive.
        pos = 1.0 * pcount / rows
        neg = 1 - pos
        
        # Define log 0 = 0
        if pos == 0 or neg == 0:
            return 0

        # Return te entropy
        return  - (pos * math.log(pos, 2) + neg * math.log(neg, 2))

    def getInfoGain(self, Examples, Target_Attribute, Entropy, attribute):
        
        # Count the total number of examples
        rows = len(Examples)
        
        # Calculate the entropy for each Examples_vi whose value = vi
        branch = self.split(Examples, Target_Attribute, attribute)
        Entropy_v0 = self.getEntropy(branch[0][0], branch[0][1])
        Entropy_v1 = self.getEntropy(branch[1][0], branch[1][1])
        
        # Calculate the percentage for each Examples_vi whose value = vi in Examples
        percentage_v0 = 1.0 * len(branch[0][0]) / rows
        percentage_v1 = 1 - percentage_v0
        
        # Return the information gain
        infoGain = Entropy - percentage_v0 * Entropy_v0 - percentage_v1 * Entropy_v1
        return infoGain

    def pruneTree(self, L, K, validation_set):

        """Post prune the decision tree using K and the validation data.
        
        Args:

            K              : The seed to generate a random number of nodes to be pruned.
            validation_set : The validation data for post pruning.

        Returns:
                bestTree : The best decision tree after post pruning.

        """

        # Let the best decision tree D_Best be the current decision tree
        bestTree = self.root

        # Create a validator using the validation set to test decision tree models
        validator = Validator(validation_set)
        
        for i in range(1, L + 1):
            
            # Copy tree D into a new tree D'
            currTree = copy.deepcopy(bestTree)

            M = K # A random number between 1 and K.

            for j in range(1, M + 1):

                # Let N denote the number of non-leaf nodes in the decision tree D'.
                # Order the nodes in D' from 1 to N.
                nonLeafNodes = self.order(currTree)
                N = len(nonLeafNodes) - 1

                # Terminate pruning if there is no non-leaf node (except for Root) in the tree
                if N <= 0:
                    return bestTree
                
                # Let P be a random number between 1 and N.
                P = random.randint(1, N) 
                
                # Replace the subtree rooted at node P in D' by a leaf node
                # Assign the majority class of the subset of the data at P 
                # to the leaf node.
                replaceNode = nonLeafNodes[P]
                replaceNode.val = -1
                replaceNode.left = None
                replaceNode.right = None

            # Evaluate the accuracy of D' on the validation set
            oldAccuracy = validator.calculateAccuracy(bestTree)
            newAccuracy = validator.calculateAccuracy(currTree)
            
            # If D' is more accurate than D_Best, replace D_Best by D'
            if newAccuracy >= oldAccuracy:
                bestTree = currTree

        # Update the decision tree to be D_Best and return D_Best 
        self.root = bestTree
        return bestTree

    def order(self, root):

        # Let arr be a list that records all the non-leaf nodes in the current decision tree D.
        arr = []

        # If the current decision tree is empty or has a leaf node at root, return an empty list.
        if root == None or root.val == -1:
            return arr
        
        # Re-order the non-leaf node by BFS traversing the decision tree D
        queue = deque([root])
        while len(queue) > 0:
            curr = queue.popleft()
            arr.append(curr)
            if curr.left != None and curr.left.val != -1:
                queue.append(curr.left)
            if curr.right != None and curr.right.val != -1:
                queue.append(curr.right)
                
        # Return the ordered non-leaf nodes
        return arr

    def __str__(self):

        return self.treeToString(self.root, 0, self.attributeNames)

    def exportTree(self, filename):
        
        # Get a string representation of the decision tree
        treeStr = self.treeToString(self.root, 0, self.attributeNames)
        with open(filename, 'w') as f:
            f.write(treeStr)

    def treeToString(self, root, level, attributeNames):
        
        # Let string be the string reprenstation of the decision tree
        string = ''

        # If root is none, return
        if root == None: 
            return ''

        # If root node is a leaf, append the class value
        if root.left == None and root.right == None:
            string += str(root.label) + '\n'
            return string

        # Get the attribute name of the current node
        currNode = attributeNames[root.val]

        # Generate the level information for the current attribute
        levelBars = ''
        for i in range(0, level):
            levelBars += '| '

        # Preappend the level information to the attribute name
        string += levelBars
        # If left subtree is a leaf node, append the class value to the current line
        # Otherwise append the subtree to the next line.
        if root.left.left == None and root.left.right == None:
            string +=  currNode + "= 0 :"
        else:
            string +=  currNode + "= 0 :\n"
        string += self.treeToString(root.left, level + 1, attributeNames)

        # Preappend the level information to the attribute name
        string += levelBars
        # If right subtree is a leaf node, append the class value to the current line
        # Otherwise append the subtree to the next line.
        if root.right.left == None and root.right.right == None:
            string += currNode + "= 1 :"
        else:
            string += currNode + "= 1 :\n"
        string += self.treeToString(root.right, level + 1, attributeNames)

        # Return the string representation of the decision tree
        return string
