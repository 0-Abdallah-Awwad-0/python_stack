# Assignment: Functions Basic II


# 1. Countdown
def countdown(num):
    result = []

    for i in range(num, -1, -1):
        result.append(i)

    return result


print(countdown(5))  # [5, 4, 3, 2, 1, 0]


# 2. Print and Return
def print_and_return(nums):
    print(nums[0])
    return nums[1]


print(print_and_return([1, 2]))
# prints 1
# returns 2


# 3. First Plus Length
def first_plus_length(nums):
    return nums[0] + len(nums)


print(first_plus_length([1, 2, 3, 4, 5]))  # 6


# 4. Values Greater than Second
def values_greater_than_second(nums):
    if len(nums) < 2:
        return False

    result = []

    for i in range(len(nums)):
        if nums[i] > nums[1]:
            result.append(nums[i])

    print(len(result))
    return result


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
# prints 3
# returns [5, 3, 4]

print(values_greater_than_second([3]))
# returns False


# 5. This Length, That Value
def length_and_value(size, value):
    result = []

    for i in range(size):
        result.append(value)

    return result


print(length_and_value(4, 7))  # [7, 7, 7, 7]
print(length_and_value(6, 2))  # [2, 2, 2, 2, 2, 2]