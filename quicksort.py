'''
    Quicksort is a sorting algorithm in which a "pivot" is chosen at random and numbers less than the pivot
    are added to the left of the pivot and numbers greater than the pivot are added to the right of the pivot.
    These exchanges occur recursively on the subarrays until the entire array is sorted.
'''

def quicksort(nums):

    quick_sort(nums, 0, len(nums)-1)



def quick_sort(nums, first, last):
    if first < last:
        pivot_index = partition(nums, first, last)
        quick_sort(nums, first, pivot_index-1)
        quick_sort(nums, pivot_index+1, last)


def partition(nums, first, last):
    pivot = nums[first]     # make pivot the first element in subarray
    low = first
    high = last

    while True:
        # find first element from right less than pivot
        while nums[high] > pivot:
            high = high - 1

        # find first element from left greater than pivot
        while nums[low] < pivot:
            low = low + 1

        # as long as low index is less than high index, swap elements
        if low < high:
            temp = nums[low]
            nums[low] = nums[high]
            nums[high] = temp
        else:
            return high


def quicksort_dsc(nums):

    quick_sort_dsc(nums, 0, len(nums)-1)


def quick_sort_dsc(nums, first, last):
    if first < last:
        pivot_index = partition_dsc(nums, first, last)
        quick_sort_dsc(nums, first, pivot_index-1)
        quick_sort_dsc(nums, pivot_index+1, last)


def partition_dsc(nums, first, last):
    pivot = nums[first]     # make pivot the first element in subarray
    low = first
    high = last

    while True:
        # find first element from right greater than pivot
        while nums[high] < pivot:
            high = high - 1

        # find first element from left less than pivot
        while nums[low] > pivot:
            low = low + 1

        # as long as low index is less than high index, swap elements
        if low < high:
            temp = nums[low]
            nums[low] = nums[high]
            nums[high] = temp
        else:
            return high





nums = [54,26,93,17,77,31,44,55,20]
quicksort(nums)
print(nums)




nums2 = [54,26,93,17,77,31,44,55,20]
quicksort_dsc(nums2)
print(nums2)