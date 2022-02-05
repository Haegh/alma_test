"""
Robot class definition file.
"""
from __future__ import annotations

import logging
from asyncio import sleep
from random import uniform
from typing import Type


class Robot:
    """
    Robot class.
    """

    next_id = 0
    # Time speed
    time_translation = 0.001

    def __init__(self):
        self.status = "stand_by"
        self.id = Robot.next_id
        Robot.next_id += 1

    def __repr__(self):
        return f"Robot {self.id}"

    # Working methods
    async def mine_foo(self) -> int:
        """
        Method for foo mining.
        
        Returns
        -------
        int
            number of foo mined
        """
        logging.info(f"Robot {self.id} mine a foo.")
        await self.__await_new_status(self.status, "mine_foo")
        self.status == "mine_foo"
        await sleep(1 * Robot.time_translation)
        return 1

    async def mine_bar(self) -> int:
        """
        Method for bar mining.
        
        Returns
        -------
        int
            number of bar mined
        """
        logging.info(f"Robot {self.id} mine a bar.")
        await self.__await_new_status(self.status, "mine_bar")
        self.status == "mine_bar"
        await sleep(uniform(0.5 * Robot.time_translation, 2 * Robot.time_translation))
        return 1

    async def assemble_foobar(self, foo: int, bar: int) -> tuple[int, int, int]:
        """
        Method for assembling a foobar from foo an bar materials.

        Parameters
        ----------
        foo : int
            number of foo materials
        bar : int
            number of bar materials
        
        Returns
        -------
        tuple[int, int, int]
            tuple of number of foo used, number of bar used and number of foobar created
        """
        logging.info(f"Robot {self.id} assemble a foobar.")
        if foo < 1 or bar < 1:
            logging.error(f"Robot {self.id} can't assemble a foobar.")
            return 0, 0, 0
        await self.__await_new_status(self.status, "assemble_foobar")
        self.status == "assemble_foobar"
        updated_foo = -1
        updated_bar = 0
        updated_foobar = 0
        if uniform(0, 100) > 60:
            updated_bar = -1
            updated_foobar = 1
        await sleep(2 * Robot.time_translation)
        return updated_foo, updated_bar, updated_foobar

    async def sell_foobar(self, foobar: int) -> tuple[int, int]:
        """
        Method for selling foobars materials.

        Parameters
        ----------
        foobar_num : int
            number of foobar materials
        
        Returns
        -------
        tuple[int, int]
            tuple of number of foobar sold and money obtained
        """
        logging.info(f"Robot {self.id} sell a foobar.")
        if foobar < 1 or foobar > 5:
            logging.error(f"Robot {self.id} can't sell a foobar.")
            return 0, 0
        await self.__await_new_status(self.status, "sell_foobar")
        self.status == "sell_foobar"
        await sleep(10 * Robot.time_translation)
        return -foobar, foobar

    async def buy_robot(self, foo: int, money: int) -> tuple[int, int, Type[Robot]]:
        """
        Method for buying robots.

        Parameters
        ----------
        foo : int
            number of foo materials
        money : int
            number of money materials
        
        Returns
        -------
        tuple[int, int, Type[Robot]]
            tuple of number of foo sold, money used and the robot bought
        """
        logging.info(f"Robot {self.id} buy a robot.")
        if money < 3 or foo < 6:
            logging.error(f"Robot {self.id} can't buy a robot.")
            return 0, 0, None
        await self.__await_new_status(self.status, "buy_robot")
        self.status == "buy_robot"
        return -6, -3, Robot()

    # Utils methods
    def __is_status_new(self, old_status: str, new_status: str) -> bool:
        """Check if 2 status are different."""
        if old_status == new_status:
            return False
        return True

    async def __await_new_status(self, old_status: str, new_status: str):
        """Method to wait if robot status is changed."""
        if self.__is_status_new(old_status, new_status):
            await sleep(5 * Robot.time_translation)
