''' Shell sort is a more efficient version of insertion sort. It utilizes a "divide and conquer" approach to insertion sort. Because insertion sort becomes more efficient when it is slightly or mostly sorted, shell sort uses this information and performs insertion sort on portion of the array. The subarrays are created by the use of a number called a "gap." The gap partitions the full array into subarrays and when the insertion sort is performed on those subarrays, the gap is then divided by 2.2 and the array is sectioned into larger subarrays. As the gap is continuously divided, the array becomes more and more sort until the gap is 1 and one final insertion sort is performed.'''


def shell_sort_asc(nums):

    gap = int(len(nums)/2)

    while gap > 0:
        next_position = gap
        for next_position in range(0, len(nums)):

            next_value = nums[next_position]

            # while position isn't at the element before gap and current value is greater than the saved value
            # shift the current element to the right and decrease the index.
            while next_position > gap-1 and nums[next_position-gap] > next_value:
                nums[next_position] = nums[next_position-gap]
                next_position = next_position - gap


            nums[next_position] = next_value


        if gap == 2:
            gap = 1
        else:
            gap = int(gap/2.2)



def shell_sort_dsc(nums):

    gap = int(len(nums)/2)

    while gap > 0:
        next_position = gap
        for next_position in range(0, len(nums)):

            next_value = nums[next_position]

            while next_position > gap-1 and nums[next_position-gap] < next_value:
                nums[next_position] = nums[next_position-gap]
                next_position = next_position - gap


            nums[next_position] = next_value


        if gap == 2:
            gap = 1
        else:
            gap = int(gap/2.2)


nums = [54,26,93,17,77,31,44,55,20]
shell_sort_asc(nums)
print(nums)

nums = [54,26,93,17,77,31,44,55,20]
shell_sort_dsc(nums)
print(nums)