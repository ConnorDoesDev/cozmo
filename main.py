import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("My name is Cozmo, what about you and why did you help me?").wait_for_completed()


cozmo.run_program(cozmo_program)