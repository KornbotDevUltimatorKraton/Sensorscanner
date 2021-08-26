import os 
import subprocess 
#output  = subprocess.check_output("i2csense",shell=True) #Scanning for the i2c devices and sensor on the robotics 
#decoder = output.decode() #Getting the decode byte mode into the string 
#Convert string into the list 
#data_split = decoder.split(" ") #Split the data output from the data splitter 
listdata = ['Running', 'i2cdetect', 'utility', 'in', 'i2c', 'bus', '1:\nThe', 'command', "'/usr/sbin/i2cdetect", '-y', "1'", 'has', 'returned:\n', '', '', '', '', '0', '', '1', '', '2', '', '3', '', '4', '', '5', '', '6', '', '7', '', '8', '', '9', '', 'a', '', 'b', '', 'c', '', 'd', '', 'e', '', 'f\n00:', '', '', '', '', '', '', '', '', '', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '\n10:', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '\n20:', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '\n30:', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '\n40:', '40', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '\n50:', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '\n60:', '--', '--', '--', '--', '--', '--', '--', '--', '68', '--', '--', '--', '--', '--', '--', '--', '\n70:', '--', '--', '--', '--', '--', '--', '--', '77', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n\n3', 'sensors', 'detected', 'in', '0x40,', '0x68,', '0x77\n']
Sensor_array = [] #Sensor array input  
converted_list = [] #Using the converted list for simplify the address sensor to be able to use with smbus connection on hardware communication 

if "detected" in listdata: 
           getting_sensor_address = listdata.index("detected")
           print(getting_sensor_address)
           for i in range(getting_sensor_address+2,len(listdata)):
                   print(listdata[i].split(",")[0])
                   print(listdata[i].strip()[0])

                   Sensor_array.append(listdata[i].split(",")[0])

print("Sensor address array:",Sensor_array)

for element in Sensor_array: 
           converted_list.append(element.strip())
print(converted_list)
