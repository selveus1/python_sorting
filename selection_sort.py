''' Selection sort is a simple sort in which an array or list is divided into 2 sectons : sorted and unsorted. The
minimum value is searched for and found in the unsorted section and added to the sorted section. '''

# simple selection sort for ascending order
def selection_sort_asc(nums):

    N = len(nums)
    for i in range(0, N):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                # exchange elements
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp


# simple selection sort for descending order
def selection_sort_dsc(nums):
    N = len(nums)
    for i in range(0, N):
        for j in range(i + 1, N):
            if nums[i] < nums[j]:
                # exchange elements
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp


# more efficient selection sort in ascending order
# this remembers the index of the min value and makes only one swap
def better_selection_sort_asc(nums):
    N = len(nums)
    for i in range(0, N):
        min_val = i
        for j in range(i + 1, N):
            if nums[min_val] > nums[j]:
                # remember the index
                min_val = j

        if min_val is not i:
            temp = nums[i]
            nums[i] = nums[min_val]
            nums[min_val] = temp


# more efficient selection sort in descending order
# this remembers the index of the min value and makes only one swap
def better_selection_sort_dsc(nums):
    N = len(nums)
    for i in range(0, N):
        min_val = i
        for j in range(i + 1, N):
            if nums[min_val] < nums[j]:
                min_val = j # remember the index

        if min_val is not i:
            temp = nums[i]
            nums[i] = nums[min_val]
            nums[min_val] = temp


nums = [54,26,93,17,77,31,44,55,20]
selection_sort_asc(nums)
print(nums)


nums2 = [54,26,93,17,77,31,44,55,20]
selection_sort_dsc(nums2)
print(nums2)


nums3 = [54,26,93,17,77,31,44,55,20]
better_selection_sort_asc(nums3)
print(nums3)


nums4 = [54,26,93,17,77,31,44,55,20]
better_selection_sort_dsc(nums4)
print(nums4)