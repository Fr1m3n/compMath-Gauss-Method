from typing import List


class Vector:

    def __init__(self, nums: List[float] = None):
        if nums is None:
            nums = []
        self.nums: List[float] = list(map(float, nums))

    def set_num(self, num, x):
        self.nums[x] = num

    def __getitem__(self, item):
        return self.nums[item]

    def __setitem__(self, key, value):
        self.nums[key] = value

    def __str__(self):
        return ''.join(map(lambda x: '{:<10.3}'.format(x), map(float, self.nums)))
