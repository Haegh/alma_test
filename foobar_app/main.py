"""
Main of foobar application.
"""
import asyncio
import logging

from foobar_app.classes.game import Game
from foobar_app.classes.robot import Robot


def main():
    logging.basicConfig(
        format="%(asctime)s-%(process)d-%(levelname)s-%(message)s", level=logging.INFO
    )
    game = Game(robots=[Robot(), Robot()])
    asyncio.run(game.play())


if __name__ == "__main__":
    main()
