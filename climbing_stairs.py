"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(n):
    cache = {}
    return climb(n, cache)


def climb(n, cache):
    if n <= 1:
        return 1
    else:
        if n in cache:
            return cache[n]
        result = climb(n - 1, cache) + climb(n - 2, cache)
        cache[n] = result
        return result
