"""
Created by: Jordan Edward Shea <jes7923>
Creation Date: 3/6/17
This program is used to analyze the speech features of a given wav file and output
a Euclidean distance
"""

import scipy.spatial.distance as sci

def main():
    # Generates table of values for template file
    templateName = input("Please enter a name for the template file: ")
    template = []
    templateLength = 0
    for line in open(templateName):
        line = line.split()
        frameList = []
        templateLength += 1
        for feature in line:
            frameList.append(float(feature))
        template.append(frameList)

    # Generates table of values for sample file
    sampleName = input("Please enter a name for the file to be compared: ")
    sample = []
    sampleLength = 0
    for line in open(sampleName):
        line = line.split()
        frameList = []
        sampleLength += 1
        for feature in line:
            frameList.append(float(feature))
        sample.append(frameList)
    # Creates a two-dimensional distance table that is filled with all zeros to begin with
    distance = [[0 for i in range(sampleLength)] for j in range(templateLength)]
    # Sets the first value of the distance table
    distance[0][0] = sci.euclidean(sample[0], template[0])
    for j in range(sampleLength):
        for i in range(templateLength):
            if(i > 0 and j > 0):
                distance[i][j] = min(distance[i-1][j], distance[i][j-1], distance[i-1][j-1]) \
                                 + sci.euclidean(sample[j],template[i])
            elif(i > 0 and j == 0):
                distance[i][j] = distance[i-1][j] + sci.euclidean(sample[j],template[i])
            elif(i == 0 and j > 0):
                distance[i][j] = distance[i][j-1] + sci.euclidean(sample[j],template[i])

    # Outputs the minimum Euclidean distance
    print(distance[templateLength -1][sampleLength -1])

main()