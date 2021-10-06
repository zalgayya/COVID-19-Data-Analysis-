'''
Author(s): Zaid Al-gayyali (1156621)
Earlier contributors(s):

  Project: Final Project
  Date of Last Update: 2021-03-31

  Functional Summary
      The program takes the ages of people infected with COVID-19 and calculates the number of cases in each age group, the amount of cases resolved in each age group and the amount of fatal cases in each age group

      Command line parameters:
        argv[1]: filename
  Refrences: 
      Confirmed positive cases of COVID-19 in Ontario:  https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario
'''


import sys
import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def main(argv):
  filename = argv[1] #assigning argv[1] to filename

  #opening file and error checking if file could not be opened
  try:
    file_csv = open(filename, encoding="utf-8-sig")
  except IOError as error:
    print("Could not open "+filename+". Exiting...\nCode: "+error)
    sys.exit(1)
  
  csv_reader = csv.reader(file_csv)

  #declaration of variables for age groups
  under_twenty_age = int(0)
  twenties_age = int(0)
  thirties_age = int(0)
  fourties_age = int(0)
  fifties_age = int(0)
  sixties_age = int(0)
  seventies_age = int(0)
  eighties_age = int(0)
  nighties_and_higher_age = int(0)
  # declaration of variables for resolved cases for each age group
  under_twenty_resolved = int(0)
  twenties_resolved = int(0)
  thirties_resolved = int(0)
  fourties_resolved = int(0)
  fifties_resolved = int(0)
  sixties_resolved = int(0)
  seventies_resolved = int(0)
  eighties_resolved = int(0)
  nighties_and_higher_resolved = int(0)
  # declaration of variables for fatal cases for each age group
  under_twenty_fatal = int(0)
  twenties_fatal = int(0)
  thirties_fatal = int(0)
  fourties_fatal = int(0)
  fifties_fatal = int(0)
  sixties_fatal = int(0)
  seventies_fatal = int(0)
  eighties_fatal = int(0)
  nighties_and_higher_fatal = int(0)

  # loop to go through file and check each age group, if found, increaments age group variable and then checks if the case was resolved or fatal
  for row in csv_reader:
    age_group = row[0]
    resolved_of_case = row[1]
    if age_group == "<20":
      under_twenty_age += 1
      if resolved_of_case == "Resolved":
        under_twenty_resolved += 1
      elif resolved_of_case == "Fatal":
        under_twenty_fatal += 1
    elif age_group == "20s":
      twenties_age += 1
      if resolved_of_case == "Resolved":
        twenties_resolved += 1
      elif resolved_of_case == "Fatal":
        twenties_fatal += 1
    elif age_group == "30s":
      thirties_age += 1
      if resolved_of_case == "Resolved":
        thirties_resolved += 1
      elif resolved_of_case == "Fatal":
        thirties_fatal += 1
    elif age_group == "40s":
      fourties_age += 1
      if resolved_of_case == "Resolved":
        fourties_resolved += 1
      elif resolved_of_case == "Fatal":
        fourties_fatal += 1
    elif age_group == "50s":
      fifties_age += 1
      if resolved_of_case == "Resolved":
        fifties_resolved += 1
      elif resolved_of_case == "Fatal":
        fifties_fatal += 1
    elif age_group == "60s":
      sixties_age += 1
      if resolved_of_case == "Resolved":
        sixties_resolved += 1
      elif resolved_of_case == "Fatal":
        sixties_fatal += 1
    elif age_group == "70s":
      seventies_age += 1
      if resolved_of_case == "Resolved":
        seventies_resolved += 1
      elif resolved_of_case == "Fatal":
        seventies_fatal += 1
    elif age_group == "80s":
       eighties_age += 1
       if resolved_of_case == "Resolved":
         eighties_resolved += 1
       elif resolved_of_case == "Fatal":
          eighties_fatal += 1
    elif age_group == "90+":
      nighties_and_higher_age += 1
      if resolved_of_case == "Resolved":
        nighties_and_higher_resolved += 1
      elif resolved_of_case == "Fatal":
        nighties_and_higher_fatal += 1

    
  #printing of output
  print("\nThere is %d cases of people infected with COVID-19 under the age of twenty, %d of them survived and %d died\n"% (under_twenty_age, under_twenty_resolved, under_twenty_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 20 and 30, %d of them survived and %d died\n"% (twenties_age, twenties_resolved, twenties_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 30 and 40, %d of them survived and %d died\n"% (thirties_age, thirties_resolved, thirties_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 40 and 50, %d of them survived and %d died\n"% (fourties_age, fourties_resolved, fourties_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 50 and 60, %d of them survived and %d died\n"% (fifties_age, fifties_resolved, fifties_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 60 and 70, %d of them survived and %d died\n"% (sixties_age, sixties_resolved, sixties_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 70 and 80, %d of them survived and %d died\n"% (seventies_age, seventies_resolved, seventies_fatal))
  print("There is %d cases of people infected with COVID-19 between the ages of 80 and 90, %d of them survived and %d died\n"% (eighties_age, eighties_resolved, eighties_fatal))
  print("There is %d cases of people infected with COVID-19 at the age of 90 and above, %d of them survived and %d died\n"% (nighties_and_higher_age, nighties_and_higher_resolved, nighties_and_higher_fatal))

  #plotting of the graph

  # array of all the age groups
  data_ages = [under_twenty_age,twenties_age, thirties_age, fourties_age, fifties_age, sixties_age, seventies_age,eighties_age,nighties_and_higher_age]

  # array of all the age groups resolved cases
  data_resolved = [under_twenty_resolved, thirties_resolved, thirties_resolved, fourties_resolved, fifties_resolved, sixties_resolved, seventies_resolved, eighties_resolved, nighties_and_higher_resolved]

  # array of all the age groups fatal cases
  data_fatal = [under_twenty_fatal, twenties_fatal, thirties_fatal, fourties_fatal, fifties_fatal, sixties_fatal, seventies_fatal, eighties_fatal, nighties_and_higher_fatal]
  #labeling of x-axis of graph
  labels = ["<20", "20s", "30s", "40s", "50s", "60s", "70s", "80s", "90+"]

  #elements of the legend 
  blue_patch = mpatches.Patch(color='blue', label='Total cases')
  orange_patch = mpatches.Patch(color='orange', label='Resolved cases')
  green_patch = mpatches.Patch(color='green', label='Fatal cases')
  #creating the bars for the graph
  plt.xticks(range(len(data_ages)), labels)
  plt.xticks(range(len(data_resolved)), labels)
  plt.xticks(range(len(data_fatal)), labels)
  
  plt.xlabel('Age groups')#label for the x-axis
  plt.ylabel('Cases')#label for the y-axis
  plt.title('Cases And Outcome Of Each Group')#title for the graph
  plt.legend(handles = [blue_patch, orange_patch, green_patch])#creating the legend
  # creating the range for the bars
  plt.bar(range(len(data_ages)), data_ages)
  plt.bar(range(len(data_resolved)), data_resolved) 
  plt.bar(range(len(data_fatal)), data_fatal) 
  # saves the bar graph to a specific file
  plt.savefig("Images/age_group.pdf")

main(sys.argv)