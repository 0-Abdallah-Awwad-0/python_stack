# Assignment: For Loop Basic II


# 1. Biggie Size
def biggie_size(nums):
    for i in range(0, len(nums)):
        if nums[i] > 0:
            nums[i] = "big"
    return nums


print(biggie_size([-1, 3, 5, -5]))


# 2. Count Positives
def count_positives(nums):
    count = 0

    for i in range(0, len(nums)):
        if nums[i] > 0:
            count += 1

    nums[len(nums) - 1] = count
    return nums


print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))


# 3. Sum Total
def sum_total(nums):
    total = 0

    for i in range(0, len(nums)):
        total += nums[i]

    return total


print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))


# 4. Average
def average(nums):
    total = 0

    for i in range(0, len(nums)):
        total += nums[i]

    return total / len(nums)


print(average([1, 2, 3, 4]))


# 5. Length
def length(nums):
    count = 0

    for i in nums:
        count += 1

    return count


print(length([37, 2, 1, -9]))
print(length([]))


# 6. Minimum
def minimum(nums):
    if len(nums) == 0:
        return False

    min_num = nums[0]

    for i in range(0, len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]

    return min_num


print(minimum([37, 2, 1, -9]))
print(minimum([]))


# 7. Maximum
def maximum(nums):
    if len(nums) == 0:
        return False

    max_num = nums[0]

    for i in range(0, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]

    return max_num


print(maximum([37, 2, 1, -9]))
print(maximum([]))


# 8. Ultimate Analysis
def ultimate_analysis(nums):
    total = sum_total(nums)
    count = length(nums)
    avg = total / count
    min_num = minimum(nums)
    max_num = maximum(nums)

    return {
        "sumTotal": total,
        "average": avg,
        "minimum": min_num,
        "maximum": max_num,
        "length": count
    }


print(ultimate_analysis([37, 2, 1, -9]))


# 9. Reverse List
def reverse_list(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

        left += 1
        right -= 1

    return nums


print(reverse_list([37, 2, 1, -9]))