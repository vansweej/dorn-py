from dorna import Dorna

robot = Dorna()

ports = robot.port_list()
print(ports)

print("robot connecting")
robot.connect()

status = robot.device()
print(status)

print("robot disconnecting")
robot.disconnect()

robot.terminate()
