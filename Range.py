"""
Print the difference between the highest and the lowest number
in the list.
"""


def get_range(nums):
    sort_list = list(sorted(nums))
    return sort_list[-1] - sort_list[0]


numbers = [10, 60, 23, 47, 35]
print(get_range(numbers))