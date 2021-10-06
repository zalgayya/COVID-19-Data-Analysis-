'''
Author(s): Mazen Bahgat (1157821), Jake McAuley(1060842)

Project: Final Project
Last updated: 2021-04-01

Main functionality:
The algorithm takes a date as a command line argument and outputs 
the 5 cities with the most cases up untill that point. It also outputs the
cases as a percentage of the city's total population and plots all the data
in a pdf file in a bar chart format. 

Command line argument: 
argv[1] : the end date of counting cases

Refrences: 

Confirmed positive cases of COVID-19 in Ontario: https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario
  Relevant Columns: 2 and 13
Canada Cities Database: https://simplemaps.com/data/canada-cities
  Relevant Columns: 0 and 6
'''

import sys
import csv
import matplotlib.pyplot as plt


def main(argv):

  endDate = argv[1]
  endDate = endDate.rstrip() # gets rid of any spaces
  endDate = int(endDate.replace('-', '')) # gets rid of the '-' chars in the date and casts the date to int

  #opens the file of the covid cases data set
  try:
    dataFile = open("SORTED_CSV_FILES/criticalCities.csv", encoding = "utf-8-sig")
  except IOError as error:
    print("Unable to open file {}: {}".format("SORTED_CSV_FILES/criticalCities.csv", error), file=sys.stderr)
    sys.exit(-1)

  # opens the file of the city populations data set
  try:
    populationFile = open("SORTED_CSV_FILES/population_can.csv", encoding = "utf-8-sig")
  except IOError as error:
    print("Unable to open file {}: {}".format("population_can.csv", error), file=sys.stderr)
    sys.exit(-1)

  # creates a csv.reader object for each of the files opened (lines 13- 24)
  readFile = csv.reader(dataFile)
  readFile2 = csv.reader(populationFile)

  lineCount = int(0)
  cities = [] # list for the city names
  caseCount = [] # list for amount of cases in each city
  foundCity = int(0)
  for currentLine in readFile: #iterates through every line in readFile object
    #branch skips the headers line
    if lineCount == 0:
      lineCount += 1
      continue
    
    # this replaces all the slashes in the currentLine's date and casts it to int
    currentLine[0] = int(currentLine[0].replace('-', ''))
    
    #this branch compares the casted to int dates (endDate and currentLine date) 
    #only enters if the currentLine date isn't higher than the endDate
    if endDate >= currentLine[0]:
        i = int(0)
        for city in cities: # iterates for length cities
          # branch checks for the city name in the city field of currentLine
          if currentLine[1] == city:
            caseCount[i] += 1
            foundCity = 1 # variable indicates the currentLine city already had a previous covid case
          i += 1
        # branch appends the name of the city and 1 case once it appears for the first time in readFile
        if foundCity == 0:
          cities.append(currentLine[1])
          caseCount.append(int(1))
        foundCity = 0 # resets foundCity for the next line
        lineCount += 1
  
  
  # sorting both lists by the case count in descending order
  for i in range (1, len(cities), 1):
    j = i -1
    while j >= 0: # iterates for prior indices to index i
      # branch enters if a prior index of caseCount is lower than index i
      if caseCount[j] < caseCount[j + 1]:
        # temp variables are assigned to save lower count 
        #variable and assign it to its proper index
        temp = caseCount[j]
        tempCity = cities[j]
        caseCount[j] = caseCount[j + 1]
        caseCount[j + 1] = temp
        cities[j] = cities[j + 1]
        cities[j + 1] = tempCity
      j = j - 1

  # cityCount is assigned 5 when there are 5 cities or more
  # assigned the amount of cities there are if less
  if len(cities) < 5:
    cityCount = len(cities)
  else:
    cityCount = 5
  
  populationList = [] # list for city populations
  foundCity = 0
  # this loop iterates through each city name and
  # looks for its population in readFile2 and appends it to a list
  for i in range (0, cityCount, 1):
    populationFile.seek(0) # resets the cursor to the beginning of the csv file
    for currentLine in readFile2:
      # this branch breaks out of the second loop if the city was already found
      if foundCity == 1:
        foundCity = 0
        break

      # branch appends the population in the line if the city name is equal to cities index i
      elif cities[i] == currentLine[0]:
        populationList.append(int(currentLine[1]))
        foundCity = 1

  # print statements based on the cityCount
  if cityCount == 1:
    print("\nOntario's only COVID Affected City is:")
  elif cityCount == 0:
    print("\nOntario has no confirmed cases.")
  else:
    print("\nOntario's {} Most Critically COVID Affected Cities are:" .format(cityCount))
  
  pctList = [] # list for case percentages of the city population
  plotData = [] # list for data to be plotted
  labels = [] # list for data labels 
  
  # this loop calculates the city case count as a percentage of its population
  # and outputs the name/caseCount/population case percentage of the current city
  # iteration. line 116 and 117 append the caseCount to the data to be plotted and
  # appends the city name to the labels
  for i in range (0, cityCount, 1):
    pctList.append(float(100 * caseCount[i]/populationList[i])) 
    print("  {}) {} with {} cases ({:.2f}% of its population)".format(i + 1, cities[i], caseCount[i], pctList[i]))
    plotData.append(caseCount[i])
    labels.append(cities[i])
  
  # prompts user for choice of plotting the data
  if cityCount > 0:
    print("\nWould you like to plot a graph of this data?\nPress 'Y' to plot or any button to exit: ")
    userChoice = input()
    if userChoice == 'y' or userChoice =='Y':
      # specifies range of x axis and plots the labels list as element labels
      plt.xticks(range(len(plotData)), labels) 
      # specifies axes labels
      plt.xlabel("Cities")
      plt.ylabel("Cases")
      plt.title("Ontario's Most Critical Cities")
      plt.bar(range(len(plotData)), plotData) # plots the bars of each city and specifies range of y axis
      # loop outputs the population percentage of cases on top of the city bar by 1% of its vertical length
      for i in range (0, cityCount, 1):
        plt.annotate("{:.2f}%".format(pctList[i]), (i - 0.15, caseCount[i] + caseCount[i] * 0.01))

      plt.savefig("Images/criticalCities.pdf") # saves figure to the output file

#executes main function
main(sys.argv) 