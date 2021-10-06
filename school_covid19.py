'''
commandline Parameters:
python school_covid19.py SORTED_CSV_FILES/studentCOVID.csv <Municipality>
  Author(s):  Hasen Romani (1096985)

  Project: COVID-19 Project
  Date of Last Update (data-set): March 31st 2021.

  Functional Summary
      school_covid19.py allows to extract relevant data that shortens the total amount of COVID information concerning date,school board, and total number of student(s) cases derived fom municipality/region based on the user's interest. 

     Commandline Parameters: 3
        argv[1] = schools with covid19 python file
        argv[2] = csv file containing the relevant columns
        argv[3] = Ontario municipality of choice

      Dataset Used:
        Download link:
          https://data.ontario.ca/dataset/b1fef838-8784-4338-8ef9-ae7cfd405b41/resource/8b6d22e2-7065-4b0f-966f-02640be366f2/download/schoolsactivecovid.csv
'''
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

def main(argv):

  #command line argument parameter verifier
  if len(argv) != 3:

    print("Usage: python school_covid19.py <data file> <municipality>")
    sys.exit(1)

  filename = argv[1] #school_covid19.py

  #file existence verifier
  try:
    file_csv = open(filename, encoding="utf-8-sig") 

  except IOError as error:
      print("Could not open " + filename + ". Exiting...\nCode: " + error)
      sys.exit(1)

  csv_read = csv.reader(file_csv, delimiter=',', skipinitialspace=True)
  
  dataSet = []

  municipality_user = argv[2]

  search_word = municipality_user

  #municipality verifier

  if search_word in open('SORTED_CSV_FILES/studentCOVID.csv').read():
    pass
  else:
    print ('***Not a valid municipality***\n')
    sys.exit(1)
    
  print("Data, School Board, Total Confirmed Case(s)")
 
  for row in csv_read:
      #print(row)
      #the columns pertaining to the prepressed csv files

      municipality_read = row[2] #municipality_read is on 3rd column
      school = row[1] #school board is on 2nd column
      report_date = row[0] #reporting date is the 1st column 
      total_cases = row[3] #total student cases is on 3rd column 
      
      if(municipality_user == municipality_read):
        #print(municipality_user)
        show_list = [report_date, school, total_cases]
        dataSet.append(show_list)     

  dataSet.sort() #sort the data-set in ascending order

  user_input = argv[2]
        
  total_cases = 0
  summation = 0

  setting_date = dataSet[0][0] 
  total_list = [] #list for total cases 
  total_schools=[] #list for school boards
  total_list_dates = [] #list for dates

  f = open("shorten_data.csv", "w")

  for data in dataSet:

    if(setting_date != data[0]): #until the condition statement reaches the last date in the file

      print(str(setting_date) + ", " + str(school) + ", "+ str(total_cases))

      total_schools.append(school)

      f.write (str(setting_date) + ", " + str(school) + ", "+ str(total_cases)) # the csv file 'f' written to the date set, school board, and total cases

      f.write("\n")

      summation += total_cases #iterates the total summation of student cases

      school = data[1]
      total_list.append(total_cases) #adding total cases to list

      total_cases = 0
      setting_date = data[0]  
      
      total_list_dates.append(setting_date) #adding dates to a list 
      
    if(user_input):

      data[1] = user_input #the municipality entered is the first "data" argument in the file
      total_cases += 1 #keeps iterating the cases 
      
  print(str(setting_date) + ", " + str(school) + ", "+ str(total_cases))

  total_schools.append(school) #adding school board to a list

  f.write (str(setting_date) + ", " + str(school) + ", "+ str(total_cases))
  total_list.append(total_cases)

  print("The total number of student cases:", summation) # the total sum of all of the total cases per school broad and date
  f.close() #closes the shorten data csv file so it would not interfere with other files

  max_value = max(total_list) #finds the maximum number of total cases
  max_index = total_list.index(max_value) #finds the school board with the most amount of cases
  print ("Greatest total case is: {}".format(max_value))
  print ("From the school: {}".format(total_schools[max_index]))

  try:
    file_csv2 = open("shorten_data.csv", encoding="utf-8-sig") 

  except IOError as error:
      print("Could not open shorten_data.csv. Exiting...\nCode: " + error)
      sys.exit(1)

  csv_read2 = csv.reader(file_csv2, delimiter=',', skipinitialspace=False) #reads the csv file alongside with considering other delimiters such as commas and spaces
  
  dictionary = {} #dictionary list that accounts all the school board names
  set_one = set()
  
  for row in csv_read2:
    for row_data_fields in csv_read2:
      school_name = row_data_fields[1] #considers the school board columns
      current_total = row_data_fields[2] #considers the total cases columns

      if (school_name in set_one):
        dictionary [school_name]+=int(current_total) #counts and adds the school board's numbers into the current total integer
          
      #if the date is not in the set, add it to the dictionary's key and set. Set
      else:
        set_one.add(school_name) #the set would add all school boards into one variable for the reason of plotting the data
        dictionary[school_name]=int(current_total)

  #plotting (Based on the user's input)

  print("\nWould you prefer a bar graph of this data?")
  print("Type 'Yes' if you would like to proceed Otherwise, type 'No' or any key\n")

  option = str(input())

  if((option == "Yes") or (option == "yes")): #if the user enters "Yes" as intended

    labels = dictionary.keys() 
    plotting = dictionary.values() #takes the values from the dictonary list

    x=np.arange(len(labels)) #arrange the length of labels
    width=0.50 #The spacing between the bars
    fig,ax=plt.subplots()

    ax.bar(x - width/2, plotting, width, label = "School Board", color = ['indigo']) # bar (x axis, y axis, width labelling as a whole)

    ax.set_ylabel('Number of Cases') # y labels
    plt.title('Number of cases of Ontario School Board in {}'.format(user_input)) # title

    ax.set_xticks(x)
    ax.set_xticklabels(labels) #school board labels
    ax.legend() #the display of variables
    fig.tight_layout()

    ax.set_ylim([0,max_value*50]) #limitation y label which is between 0 and maximum cases value times 50
    ax.set_xticklabels(labels, fontsize= 5 ) #the x-axis label and its font size to make it seeable
    ax.spines['bottom'].set_color('blue')
    ax.spines['left'].set_color('blue')
    ax.spines['right'].set_color('blue')
    ax.spines['top'].set_color('blue')

    ax.set_facecolor('mediumslateblue') #background graph colour

    fig.autofmt_xdate() #auto-formates the x axis variables
    
    plt.savefig("Images/students_with_COVID.pdf") #saves or overwrite the plot to a pdf
  

main(sys.argv)