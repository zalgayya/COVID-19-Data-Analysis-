'''
Author(s): Jake McAuley (1060842)
Earlier contributors(s):

  Project: Final Project
  Date of Last Update: 2021-03-31

  Functional Summary
      Reads in vaccine data from offical ontario csv file and creates a function
      out of the data trend using quadratic regression. The function is then made to
      reach an estimated amount of required doses, and showcase/explicity explain
      the amount of days remaining until this amount is reached.

      Command line parameters:
        argv[1]: Start date
        argv[2]: End date

     References
        COVID FILE: https://data.ontario.ca/dataset/covid-19-vaccine-data-in-ontario/resource/8a89caa9-511c-4568-af89-7f2174b4378c

      Citations:

        matplotlib quadratic regeression model insprired by:

        Title: "Machine Learning - Polynomial Regression"
        Author: w3schools
        Avalibility: https://www.w3schools.com/python/python_ml_polynomial_regression.asp 

'''


import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
  filename = argv[1]
  date_range = []
  start = False
  counter = 0
  current_date = 0
  x = []
  y = []
  days_needed = 0
  vacc_needed = 0
  vacc_estimate = 25803820

  #Grab date range variables
  for index in range(2, len(argv), 1):
    date_range.append(argv[index])

  try:
    file_handle = open(filename)
  except IOError as error:
    print("Could not open "+filename+". Exiting...\nCode: "+error)
    sys.exit(1)
  
  csv_reader = csv.reader(file_handle)

  for row in csv_reader:
    #find current date by counting entrys in csv file (assumes csv file is updated)
    current_date += 1
    #Preprocess the date data to remove "T00:00:00" (not sure what it even means)
    row[0] = row[0].replace('T', ' ')
    row[0] = row[0].strip("T00:00:00")
    row[0] = row[0].replace(' ', '')

    if(row[0] == argv[2]):
      start = True

    if(start):
      counter = counter + 1
      x.append(counter)
      y.append(int(row[1]))

    if(row[0] == argv[3]):
      start = False
      
  plt.scatter(x,y, label="Confirmed Doses")
  
  #Model holds the polynomial equation generated by Quadratic regression
  model = np.poly1d(np.polyfit(x, y, 2))

  #25803820 is my estimation of how many doses are needed to vaccinate all of ontario based on the assumptions outlined in Milestone II, it is contained in variable vacc_estimate.

  #This is a brute force method of figuring out how many days are needed for full vaccination (entering values into function).
  while(vacc_needed < vacc_estimate):
    vacc_needed = model(days_needed)
    days_needed += 1
     
  #Paramenter two here denotes the number of days needed to reach 24mill doses.
  polyline = np.linspace(1, days_needed, days_needed) 

  polyline_needed = np.linspace(vacc_estimate, vacc_estimate, days_needed)
  
  #Model(polyline) calculates the value of the function contained in model for the x values contained in polyline (1 -> needed)
  plt.plot(polyline, model(polyline), "b", label='Estimated Doses')

  plt.plot(polyline, polyline_needed, "r:", label='Needed Doses')

  plt.plot(current_date, model(current_date), "rD", label='Current Date')

  plt.annotate("Days Required From Today: " + str(days_needed - current_date), (5,24000000))

  plt.xlabel("Days")
  
  plt.ylabel("Vaccine Doses (Tens of Millions)")

  plt.title("Vaccine Timeline Estimate")

  plt.legend()

  plt.savefig("Images/vaccination_timeline_plot.pdf")

main(sys.argv)