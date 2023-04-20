import time
from pymavlink import mavutil

vtol = mavutil.mavlink_connection("COM13", baud= 57600)

# Make sure the connection is valid
vtol.wait_heartbeat()

# Get some information !
while True:
    try:
        print(vtol.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)