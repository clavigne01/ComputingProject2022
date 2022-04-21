import serial
ser = serial.Serial('/dev/tty.usbserial-1410')

print("Enter total amount of titrant added")

# inputting the total volume
volume = input("Volume:")
print("Volume: {0} mL".format(volume))

while volume != ""
  ser.write(b'R\r')
  float(ser.read(8))
  # add csv file stuff
  volume = input("Volume:")
