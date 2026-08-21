#!/usr/bin/python3
def weight_average(my_list=[]):
    if not list:
        return 0

    totalWeight = 0
    totalScore = 0

    for score, weight in my_list:
        totalWeight += weight
        totalScore += score * weight
    return totalScore / totalWeight if totalWeight else 0
