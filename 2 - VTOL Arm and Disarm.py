import time
from pymavlink import mavutil

# Create the connection
vtol = mavutil.mavlink_connection("COM13", baud= 57600)
# Wait a heartbeat before sending commands
vtol.wait_heartbeat()

# https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM

# Arm
# vtol.arducopter_arm() or:
vtol.mav.command_long_send(
    vtol.target_system,
    vtol.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# wait until arming confirmed (can manually check with vtol.motors_armed())
print("Waiting for the vehicle to arm")
vtol.motors_armed_wait()
print('Armed!')
time.sleep(5)
# Disarm
# vtol.arducopter_disarm() or:
vtol.mav.command_long_send(
    vtol.target_system,
    vtol.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)

# wait until disarming confirmed
vtol.motors_disarmed_wait()
print('disArmed!')