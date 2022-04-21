import serial
ser = serial.Serial('/dev/tty.usbserial-1410')

print("Enter total amount of titrant added")

# inputting the total volume
volume = input("Volume:")
print("Volume: {0} mL".format(volume))

while volume != ""
  ser.write(b'R\r')
  float(ser.read(8))

```{r}
import csv
with open('_____', 'w', newline='') as csvfile:
    _____ = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
   ______.writerow(['_____'] * 5 + ['_____'])
    _____.writerow(['_____', '______', '_____'])
```

  volume = input("Volume:")
