import csv


#This algorithm lets the machine to find the highest pressure
pressures = []
num_of_lines_to_process = 20000
biggestNumber = 0
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')



#This algorithm lets the machine to find the highest temperature
temperature = []
biggestNumber1 = 0
with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber1 = float(row[1])

          #print(f'temperature: \t{row[1]}')
          temperature.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber1<float(row[1])):
            biggestNumber1 = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')



#This algorithm lets the machine to find the lowest temperature
Minpressure = []
SmallestNumber1 = 0
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            SmallestNumber1 = float(row[1])

          #print(f'pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is smaller than the previous SmallestNumber2, set SmallestNumber2 equal to the new data value.
          if(SmallestNumber1>float(row[1])):
            SmallestNumber1 = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')


#This algorithm lets the machine to find the lowest pressure
Mintemperature= []
SmallestNumber2 = 0
with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            SmallestNumber2 = float(row[1])

          #print(f'temperature: \t{row[1]}')
          temperature.append([row[1],row[3]])
          #If the current value of the data is smaller than the previous SmallestNumber2, set SmallestNumber2 equal to the new data value.
          if(SmallestNumber2>float(row[1])):
            SmallestNumber2 = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')




#print(len(pressures))
#print(SmallestNumber1)

#this prints the average values
print(f'Average pressure is {pressures[0][0]} hPa and {temperature[0][0]}*Celcius at {pressures[0][1]}' )

#this prints the highest values
print(f'The highest pressure is {biggestNumber} hPa at {pressures[14734][1]} and the highest temperature is {biggestNumber1}°Celcius at {temperature[3253][1]}')

#this prints the lowest values
print(f'The lowest pressure is {SmallestNumber1} hPa at {pressures[3047][1]} and the lowest temperature is {SmallestNumber2}°Celcius at {temperature[2241][1]}')
