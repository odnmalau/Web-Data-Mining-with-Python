import math

class Node:
    def __init__(self, name):
        self.name = name
        self.label = None
        self.decisionAttr = None
        self.decisionGain = None
        self.decisionValue = None
        self.branches = []

    def printTree(self):
        self.printTreeRecurse(0)

    def printTreeRecurse(self, level):
        print ('\t' * level + self.name),
        if self.decisionAttr and self.decisionGain:
            print ('split by ' + str(self.decisionAttr) + ' for a gain of ' + str(self.decisionGain)),
        if self.label:
            print (' ' + self.label),
        
        level += 1
        for branch in self.branches:
            branch.printTreeRecurse(level)

    def predictOutcome(self, cases, a):
        predictions = []
        for c in cases:
            outcome = self.predictOutcomeRecurse(c, attributes)
            predictions.append(outcome)
        return predictions

    def predictOutcomeRecurse(self, case, a):
        if self.name == '':

            
            if self.label == '+':
                return 'Yes'
            elif self.label == '-':
                return 'No'

        index = a.index(self.decisionAttr)

        if self.decisionValue == case[index]:
            return self.branches[0].predictOutcomeRecurse(case, a)

        if self.decisionGain:
            
            for b in self.branches:
                if b.decisionValue == case[index]:
                    return b.predictOutcomeRecurse(case, a)



def constructDecisionTree(examples, targetAttribute, attributes):
    root = Node('')

    
    

    if all(isPositive(example[-1]) for example in examples):
        root.label = '+'
        return root

    
    elif all(not isPositive(example[-1]) for example in examples):
        root.label = '-'
        return root

    
    elif not attributes:
        root.label = getMostCommonLabel(examples)
        return root
    else:
        result = getHighestInfoGainAttr(attributes, examples)
        attr = result[0]
        gain = result[1]
        attrIndex = result[2]

        root.decisionAttr = attr
        root.decisionGain = gain

        possibleValues = uniqueValues(attrIndex, examples)

        for value in possibleValues:
            newBranch = Node(attr + ' = ' + value)
            newBranch.decisionAttr = attr
            newBranch.decisionValue = value
            root.branches.append(newBranch)
            branchExamples = sorted(row for row in examples if row[attrIndex] == value)

            if not branchExamples:
                leaf = Node(getMostCommonValue(targetAttribute, examples, possibleValues))
                newBranch.branches.append(leaf)
            else:
                newExamples = []
                for example in branchExamples:
                    newExample = []
                    for i in range(len(example)):
                        if not i == attrIndex:
                            newExample.append(example[i])
                    newExamples.append(newExample)

                newBranch.branches.append(constructDecisionTree(newExamples, targetAttribute, [a for a in attributes if not a == attr]))

    return root



def isPositive(word):
    word = word.lower()
    return word == 'yes' or word == 'true' or word == 'y' or word == 't'



def getMostCommonLabel(nodes):
    pCount = 0
    nCount = 0

    for node in nodes:
        if node.label == '+':
            pCount += 1
        elif node.label == '-':
            nCount += 1

    if pCount >= nCount:
        return '+'
    else:
        return '-'



def getHighestInfoGainAttr(attributes, examples):
    totalRows = len(examples)
    
    posExamples = sorted(row for row in examples if isPositive(row[-1]))
    negExamples = sorted(row for row in examples if not isPositive(row[-1]))

    
    allExpectedInfo = computeExpectedInfo(len(posExamples), len(negExamples))

    valuesGain = []

    
    for i, attr in enumerate(attributes):

        
        if attributes[-1] == attributes[i]:
            break

        values = uniqueValues(i, examples)

        
        valuesExpectedInfo = []
        valuesProbability = []

        
        for value in values:
            
            posExamplesOfValue = sorted(row for row in posExamples if row[i]==value)
            negExamplesOfValue = sorted(row for row in negExamples if row[i]==value)
            numPos = len(posExamplesOfValue)
            numNeg = len(negExamplesOfValue)
            
            valueExpectedInfo = computeExpectedInfo(numPos, numNeg)
            valueProbability = float(numPos + numNeg) / float(totalRows)
            valuesExpectedInfo.append(valueExpectedInfo)
            valuesProbability.append(valueProbability)

        
        valueEntropy = computeEntropy(valuesExpectedInfo, valuesProbability)
        valueGain = allExpectedInfo - valueEntropy
        valuesGain.append(valueGain)

    
    index = valuesGain.index(max(valuesGain))

    return [attributes[index], valuesGain[index], index]





def computeExpectedInfo(count1, count2):
    count1 = float(count1)
    count2 = float(count2)
    total = count1 + count2
    prob1 = count1/total
    prob2 = count2/total

    
    if prob1 > 0.0 and prob2 > 0.0:
        return -prob1 * math.log(prob1, 2.0) - prob2 * math.log(prob2, 2.0)
    elif prob1 > 0.0:
        return -prob1 * math.log(prob1, 2.0)
    elif prob2 > 0.0:
        return -prob2 * math.log(prob2, 2.0)
    else:
        print ('There was an error computing expected info.')
        return 0




def computeEntropy(p, e):
    entropy = 0.0
    for i in range(len(p)):
        entropy += p[i] * e[i]
    return entropy



def uniqueValues(attrIndex, examples):
    values = []
    for e in examples:
        if e[attrIndex] not in values:
            values.append(e[attrIndex])
    return values




def getMostCommonValue(attr, examples, values):
    valueCounts = []

    for value in values:
        valueCount = 0
        for example in examples:
            if example[attr] == value:
                valueCount += 1
        valueCounts.append(valueCount)

    maxIndex = valueCounts.index(max(valueCounts))
    return values[maxIndex]





def constructTreeFromFile(filepath):
    f = open(filepath, 'r')
    attrLine = f.readline()
    attributes = [a.strip() for a in attrLine.split(',')]
    examples = []
    for line in f:
        example = [item.strip() for item in line.split(',')]
        examples.append(example)

    
    return constructDecisionTree(examples, attributes[-1], attributes)



def parseTestCases(filepath):
    f = open(filepath, 'r')
    cases = []
    for line in f:
        case = [item.strip() for item in line.split(',')]
        cases.append(case)

    return cases


def getAttributesFromFile(filepath):
    f = open(filepath, 'r')
    attrLine = f.readline()
    return [a.strip() for a in attrLine.split(',')]


trainingPath = input('Please enter the path to a file containing training data:\n')
tree = constructTreeFromFile(trainingPath)
tree.printTree()

attributes = getAttributesFromFile(trainingPath)
attributes.pop(-1)

testingPath =   input('Please enter the path to a file containing cases to be tested:\n')
testCases = parseTestCases(testingPath)
outcomes = tree.predictOutcome(testCases, attributes)
print (outcomes)