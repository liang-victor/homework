"""https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

There are n employees, each with a unique id from 0 to n - 1.

You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:

idi is the id of the employee that worked on the ith task, and
leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.

Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.

"""


def hardest_worker(n, logs):
    # the value of n seems to be irrelevant to this problem?

    start = 0
    max_duration = 0
    id_with_max = None

    for [id, end] in logs:
        duration = end - start
        if duration > max_duration:
            max_duration = duration
            id_with_max = id
        elif duration == max_duration and id < id_with_max:
            id_with_max = id

        start = end

    return id_with_max
