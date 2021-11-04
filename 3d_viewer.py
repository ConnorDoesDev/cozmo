import asyncio

import cozmo


async def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        await asyncio.sleep(1)


cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)