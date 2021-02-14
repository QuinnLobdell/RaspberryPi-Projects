import serial, time
from Adafruit_IO import Client

aio = Client("my username here", "my code goes here")
 
ser = serial.Serial('/dev/ttyUSB0')

print("made it to while loop") 
#worked
while True:
    data = []
    print("data list created")
    #this one also works
    for index in range(0,10):
        datum = ser.read()
        data.append(datum)
        print("in the index loop")
        #I never see this
    print("escaped index loop")
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    aio.send("2-dot-5-aqi", pmtwofive)
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    aio.send("10-aqi", pmten)
    print("about to sleep")
    time.sleep(10)
