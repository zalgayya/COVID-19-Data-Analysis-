#Author(s): Jake McAuley
import sys
import csv
#command line format: 

#argv[1] is filename.
#argv[2]... argv[n], are all the columns that are to be extracted and saved by the program.
#include "> your_file_name_here.csv" after the above command statements to generate the csv file that you need. 
def main(argv):

  filename = argv[1]
  rel_columns = []
  last_index = int(argv[len(argv) - 1])

  #grabs relevant index(s) from the command line.
  for index in range(2, len(argv), 1):
    rel_columns.append(int(argv[index]))

  try:
    file_handle = open(filename)
  except IOError as error:
    print("Could not open "+filename+". Exiting...\nCode: "+error)
    sys.exit(1)
  
  csv_reader = csv.reader(file_handle)
  
  for row in csv_reader:
    for index in rel_columns:
      #Some csv files include commas inside of numbers, which can mess with later processing.
      #.replace just replaces those characters with an empty space (effectivly deleting them)
      row[index] = row[index].replace(',','')
      if(index == last_index):
        print(row[index],end="\n")
      else:
        print(row[index]+",",end ="")
  

main(sys.argv)


