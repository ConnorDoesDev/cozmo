import cozmo

name = input("What is your name? ")


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text(
        f"Hi! My name is Cozmo. How are you, {name}?").wait_for_completed()


cozmo.run_program(cozmo_program)
