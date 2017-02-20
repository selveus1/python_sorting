'''Heap sort an be thought of as an improved selection sort: like that algorithm, it divides
its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region
by extracting the largest element and moving that to the sorted region. The improvement consists
of the use of a heap data structure rather than a linear-time search to find the maximum.'''


def heapsort(nums):

    # convert array into heap
    N = 1
    while N < len(nums):
        N += 1
        child = N-1
        parent = (child-1) / 2

        while parent >= 0 and nums[parent] < nums[child]:
            swap(nums, parent, child)
            child = parent
            parent = (child-1)/2

    shrink_heap(nums)



def shrink_heap(nums):
    N = len(nums)

    while N > 0:
        N -= 1
        swap(nums, 0, N)

        parent = 0

        while True:
            left = 2 * parent + 1
            if left >= N:
                break

            right = left + 1
            max = left
            if right < N and nums[left] < nums[right]:
                max = right

            if nums[parent] < nums[max]:
                swap(nums,parent,max)
                parent = max
            else:
                break


def swap(nums, parent, child):
    tmp = nums[parent]
    nums[parent] = nums[child]
    nums[child] = tmp


nums = [54,26,93,17,77,31,44,55,20]
heapsort(nums)
print(nums)