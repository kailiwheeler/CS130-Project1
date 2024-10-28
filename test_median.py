#test median Project 1

import stats



def test_median_1():
    data = [1,2,3,4,5]
    assert stats.median(data) == 3


def test_median_2():
    data = [1,2,3,4]
    assert stats.median(data) == 2.5
