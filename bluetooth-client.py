import bluetooth

# insert here the address of the Pi that you noted earlier
bd_addr = '00:1A:7D:DA:71:11'
# port must be consistent with server
port = 3

nearby_devices = bluetooth.discover_devices()
print nearby_devices

print nearby_devices[0]

print type(nearby_devices[0])

print nearby_devices == bd_addr

print bd_addr

print (type(bd_addr))

# bd_addr = nearby_devices[0]

# create a socket and connect to the server
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print "Trying to connect"
# sock.connect((nearby_devices[0], port))
sock.connect((bd_addr, port))

print "was connected"

# we're now ready to send data!

# This will repeatedly send what a user types, you will probably want to
# decide a format and check for it here so it can be easily decoded the
# other side

while True:
    msg = raw_input("What would you like to send? ")
    if msg == "exit":
        sock.send(msg)
        break
    else:
        sock.send(msg)
# close up when finished
print "Exiting"





sock.close()
