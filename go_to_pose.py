import cozmo
from cozmo.util import degrees, Pose


def cozmo_program(robot: cozmo.robot.Robot):
    robot.go_to_pose(Pose(0, 0, 0, angle_z=degrees(90)),
                     relative_to_robot=True).wait_for_completed()


cozmo.run_program(cozmo_program)
