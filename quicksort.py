'''
    Quicksort is a sorting algorithm in which a "pivot" is chosen at random and numbers less than the pivot
    are added to the left of the pivot and numbers greater than the pivot are added to the right of the pivot.
    These exchanges occur recursively on the subarrays until the entire array is sorted.
'''

def quicksort(nums):

    quicksort(nums, 0, len(nums)-1)



def quicksort(nums, first, last):
    if first < last:
        int pivot_index = partition(nums, first, last)
        quicksort(nums, first, pivot_index-1)
        quicksort(nums, pivot_index+1, last)


def partition(nums, first, last):




nums = [54,26,93,17,77,31,44,55,20]
quicksort(nums)
print(nums)