class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        while j < n:
            nums1[m + j] = nums2[j]
            j += 1

        def merge(arr):
            if len(arr) > 1:
                mid = len(arr) // 2

                L = arr[:mid]
                R = arr[mid:]
                merge(L)
                merge(R)

                i = j = k = 0

                while i < len(R) and j < len(L):
                    if R[i] <= L[j]:
                        arr[k] = R[i]
                        i += 1
                    else:
                        arr[k] = L[j]
                        j += 1
                    k += 1

                while i < len(R):
                    arr[k] = R[i]
                    i += 1
                    k += 1

                while j < len(L):
                    arr[k] = L[j]
                    j += 1
                    k += 1
        merge(nums1)
