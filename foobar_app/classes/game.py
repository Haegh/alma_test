"""
Game class definition file.
"""
import asyncio
import logging
from typing import List, Type

from foobar_app.classes.robot import Robot


class Game:
    """
    Game class.
    """

    def __init__(self, robots: List[Type[Robot]]):
        self.robots = robots
        self.foo = 0
        self.bar = 0
        self.foobar = 0
        self.money = 0

    def __repr__(self):
        return "Game"

    async def play(self):
        """
        Core method launching the game.
        """
        logging.info("Game launched.")
        foo_lock = asyncio.Lock()
        bar_lock = asyncio.Lock()
        foobar_lock = asyncio.Lock()
        money_lock = asyncio.Lock()
        tasks = []
        for robot in self.robots:
            task = asyncio.create_task(
                self.__robot_logic(robot, foo_lock, bar_lock, foobar_lock, money_lock)
            )
            tasks.append(task)
        await asyncio.gather(*tasks)
        print("Congratulations ! You have 30 robots !")

    async def __robot_logic(
        self,
        robot: Type[Robot],
        foo_lock: asyncio.Lock,
        bar_lock: asyncio.Lock,
        foobar_lock: asyncio.Lock,
        money_lock: asyncio.Lock,
    ):
        """
        Robot rules for choosing actions.

        Parameters
        ----------
        robot : Type[Robot]
            a Robot
        foo_lock : asyncio.Lock,
            async lock for foo materials
        bar_lock : asyncio.Lock,
            async lock for bar materials
        foobar_lock : asyncio.Lock,
            async lock for foobar materials
        money_lock : asyncio.Lock,
            async lock for money materials
        """
        while len(self.robots) < 30:
            if self.money >= 3 and self.foo >= 6:
                async with foo_lock, money_lock:
                    new_foo, new_money, new_robot = await robot.buy_robot(
                        self.foo, self.money
                    )
                    self.foo += new_foo
                    self.money += new_money
                if new_robot:
                    self.robots.append(new_robot)
                    # Add new robot task in existing asyncio loop
                    asyncio.ensure_future(
                        self.__robot_logic(
                            new_robot, foo_lock, bar_lock, foobar_lock, money_lock
                        ),
                        loop=asyncio.get_event_loop(),
                    )
            elif self.foobar > 0:
                async with foobar_lock, money_lock:
                    foobar_num_to_sell = self.foobar
                    if self.foobar > 5:
                        foobar_num_to_sell = 5
                    new_foobar, new_money = await robot.sell_foobar(foobar_num_to_sell)
                    self.foobar += new_foobar
                    self.money += new_money
            elif self.foo > 0 and self.bar > 0:
                async with foo_lock, bar_lock, foobar_lock:
                    new_foo, new_bar, new_foobar = await robot.assemble_foobar(
                        self.foo, self.bar
                    )
                    self.foo += new_foo
                    self.bar += new_bar
                    self.foobar += new_foobar
            elif self.foo < 6:
                async with foo_lock:
                    new_foo = await robot.mine_foo()
                    self.foo += new_foo
            else:
                async with bar_lock:
                    new_bar = await robot.mine_bar()
                    self.bar += new_bar
            logging.debug(
                f"foo : {self.foo}, bar : {self.bar}, foobar : {self.foobar}, money : {self.money}"
            )
