def merge_sort_asc(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort_asc(left)
        merge_sort_asc(right)
        merge_asc(nums, left, right)


def merge_asc(nums, left, right):

    i = 0   # index into the left input sequence
    j = 0   # index into the right input sequence
    k = 0   # index into the output sequence

    # while the input from the left and inputs from the right
    #   are not exhausted
    while i < len(left) and j < len(right):

        # left input is less than right input so it's next
        #   in the sort
        if left[i] < right[j]:
            nums[k] = left[i]
            i = i+1
        else:   # right input is less than left
            nums[k] = right[j]
            j = j+1

        k = k+1

    # copy in the remaining nums from left into
    #   actual array (if any)
    while i < len(left):
        nums[k] = left[i]
        i = i+1
        k = k+1

    # copy in the remaining nums from right into
    #   actual array (if any)
    while j < len(right):
        nums[k] = right[j]
        j = j+1
        k = k+1



def merge_sort_dsc(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort_dsc(left)
        merge_sort_dsc(right)
        merge_dsc(nums, left, right)


def merge_dsc(nums, left, right):

    i = 0   # index into the left input sequence
    j = 0   # index into the right input sequence
    k = 0   # index into the output sequence

    # while the input from the left and inputs from the right
    #   are not exhausted
    while i < len(left) and j < len(right):

        # left input is less than right input so it's next
        #   in the sort
        if left[i] > right[j]:
            nums[k] = left[i]
            i = i+1
        else:   # right input is less than left
            nums[k] = right[j]
            j = j+1

        k = k+1

    # copy in the remaining nums from left into
    #   actual array (if any)
    while i < len(left):
        nums[k] = left[i]
        i = i+1
        k = k+1

    # copy in the remaining nums from right into
    #   actual array (if any)
    while j < len(right):
        nums[k] = right[j]
        j = j+1
        k = k+1


### main program
nums = [54,26,93,17,77,31,44,55,20]
merge_sort_asc(nums)
print(nums)


nums1 = [54,26,93,17,77,31,44,55,20]
merge_sort_dsc(nums1)
print(nums1)