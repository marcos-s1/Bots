import asyncio
from Robos import textRobot, ImageRobot, VideoRobot, stateRobot
from Robos.inputRobot import askAndReturnPrefix, askAndReturnSeachTerm


async def start():
    content = {'SeachTerm': askAndReturnSeachTerm(), 'prefix': askAndReturnPrefix()}
    stateRobot.save(content)
    await textRobot.ActivateTextBoot()
    await ImageRobot.ActivateImageBoot()
    VideoRobot.ActivateVideoRobot()


asyncio.run(start())

