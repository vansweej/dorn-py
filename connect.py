from dorna import Dorna

robot = Dorna()

ports = robot.port_list()
print(ports)

print("robot connecting")
robot.connect()

status = robot.device()
print(status)

# homing the robot
robot.home("j0")
robot.home("j1")
robot.home("j2")
robot.home("j3")
robot.home("j4")

homed = robot.homed()
print(homed)

# set units
robot.set_unit({"length": "mm"})

robot.play({"command": "move", "prm": {"movement": 1, "path": "joint", "j0": 190}})
robot.play({"command": "move", "prm": {"movement": 1, "path": "joint", "j1": -120}})

robot.play({"command": "move", "prm": {"movement": 1, "path": "line", "x": 20}})
robot.play({"command": "move", "prm": {"movement": 1, "path": "line", "z": 30}})
robot.play({"command": "move", "prm": {"movement": 1, "path": "line", "z": -30}})
robot.play({"command": "move", "prm": {"movement": 1, "path": "line", "x": -40}})

robot.play({"command": "move", "prm": {"movement": 1, "path": "line", "z": 30}})
robot.play({"command": "move", "prm": {"movement": 1, "path": "line", "z": -30}})


print("robot disconnecting")
#robot.disconnect()

#robot.terminate()
