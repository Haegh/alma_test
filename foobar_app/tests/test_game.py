"""
Test file for game class.
"""
import asyncio

import pytest

from foobar_app.classes.game import Game
from foobar_app.classes.robot import Robot


@pytest.fixture
def game():
    """Fixture defining a Game instance."""
    return Game(robots=[Robot(), Robot()])


# Game special method
def test_game_init(game):
    """Test game initialization."""
    assert len(game.robots) == 2
    assert isinstance(game.robots[0], Robot)
    assert game.foo == 0
    assert game.bar == 0
    assert game.foobar == 0
    assert game.money == 0


def test_game_repr(game):
    """Test __repr__ method."""
    assert str(game) == "Game"


# Game core methods
@pytest.mark.asyncio
async def test_robot_logic(game):
    """
    Test method __robot_logic with the case of 29 robots already created and
    enough ressources to buy the last robot.
    """
    foo_lock = asyncio.Lock()
    bar_lock = asyncio.Lock()
    foobar_lock = asyncio.Lock()
    money_lock = asyncio.Lock()
    game.foo = 6
    game.money = 3
    for _ in range(27):
        game.robots.append(Robot())
    await game._Game__robot_logic(
        game.robots[0], foo_lock, bar_lock, foobar_lock, money_lock
    )
    assert len(game.robots) == 30
    assert game.foo == 0
    assert game.bar == 0
    assert game.foobar == 0
    assert game.money == 0
