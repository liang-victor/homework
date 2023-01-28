import pytest
from implement_queues_using_stacks import MyQueue


def test_example_1():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert obj.empty() is False
    assert obj.pop() == 2
    assert obj.empty() is True


def test_example_2():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    assert obj.pop() == 1
    assert obj.pop() == 2
    obj.push(1)
    obj.push(2)
    assert obj.pop() == 3
    assert obj.pop() == 4
