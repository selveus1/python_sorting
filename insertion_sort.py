''' Insertion sort is a quadratic sorting algorithm that, starting at the index 1, finds the min value and inserts in
its correct location of the sorted subarray.'''

def insertion_sort_asc(nums):
    N = len(nums)
    for i in range(1,N):
        next_position = i       # save index of where element is to be inserted
        next_value = nums[i]    # save value of element being moved

        # while position isn't at 0 and current value is greater than the saved value
        # shift the current element to the right and decrease the index.
        while next_position > 0 and nums[next_position - 1] > next_value:
            nums[next_position] = nums[next_position-1]
            next_position = next_position - 1

        nums[next_position] = next_value


def insertion_sort_dsc(nums):
    N = len(nums)
    for i in range(1, N):
        next_position = i
        next_value = nums[i]

        while next_position > 0 and nums[next_position - 1] < next_value:
            nums[next_position] = nums[next_position - 1]
            next_position = next_position - 1

        nums[next_position] = next_value


### main program
nums = [54,26,93,17,77,31,44,55,20]
insertion_sort_asc(nums)
print(nums)


nums2 = [54,26,93,17,77,31,44,55,20]
insertion_sort_dsc(nums2)
print(nums2)
