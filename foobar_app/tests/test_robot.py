"""
Test file for robot class.
"""
import random
import re

import pytest

from foobar_app.classes.robot import Robot


@pytest.fixture
def robot():
    """Fixture defining a Robot instance."""
    return Robot()


# Robot special method
def test_robot_init(robot):
    """Test robot initialization."""
    assert robot.status == "stand_by"


def test_robot_repr(robot):
    """Test __repr__ method."""
    assert re.match("^Robot [0-9]*$", str(robot))


# Robot working methods
@pytest.mark.asyncio
async def test_mine_foo(robot):
    """Test method mine_foo."""
    res = await robot.mine_foo()
    assert res == 1


@pytest.mark.asyncio
async def test_mine_bar(robot):
    """Test method mine_bar."""
    res = await robot.mine_bar()
    assert res == 1


@pytest.mark.asyncio
async def test_assemble_foobar(robot):
    """Test method assemble_foobar(."""
    # Random seed to always have the same result
    random.seed(0)
    foo = 1
    bar = 1
    res = await robot.assemble_foobar(foo, bar)
    assert res == (-1, -1, 1)
    foo = 0
    bar = 1
    res = await robot.assemble_foobar(foo, bar)
    assert res == (0, 0, 0)
    foo = 1
    bar = 0
    res = await robot.assemble_foobar(foo, bar)
    assert res == (0, 0, 0)


@pytest.mark.asyncio
async def test_sell_foobar(robot):
    """Test method sell_foobar."""
    foobar = 1
    res = await robot.sell_foobar(foobar)
    assert res == (-foobar, foobar)
    foobar = 0
    res = await robot.sell_foobar(foobar)
    assert res == (0, 0)
    foobar = 8
    res = await robot.sell_foobar(foobar)
    assert res == (0, 0)


@pytest.mark.asyncio
async def test_buy_robot(robot):
    """Test method buy_robot."""
    foo = 6
    money = 3
    res = await robot.buy_robot(foo, money)
    assert res[0] == -foo
    assert res[1] == -money
    assert isinstance(res[2], Robot)
    foo = 5
    money = 3
    res = await robot.buy_robot(foo, money)
    assert res == (0, 0, None)
    foo = 6
    money = 2
    res = await robot.buy_robot(foo, money)
    assert res == (0, 0, None)


# Robot utilities methods
def test_is_status_new(robot):
    """Test method is_status_new."""
    assert robot._Robot__is_status_new("status", "status") is False
    assert robot._Robot__is_status_new("status", "status2") is True


@pytest.mark.asyncio
async def test_await_new_status(robot):
    """Test mehod await_new_status."""
    status_old = "status"
    status_new = "status"
    res = await robot._Robot__await_new_status(status_old, status_new)
    assert res is None
