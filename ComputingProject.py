import serial
import csv
ser = serial.Serial('/dev/tty.usbserial-1420')

print("Enter total amount of titrant added")

# inputting the total volume
volume = input("Volume:")
print("Volume: {0} mL".format(volume))

with open('ComputingProject.csv', 'w', newline='') as csvfile:
  compwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
  compwriter.writerow(['Volume', 'pH'])
  

  while volume != "":
    ser.write(b'R\r')
    pH = float(ser.read(6))
  
    compwriter.writerow([volume, pH])

    volume = input("Volume:")
