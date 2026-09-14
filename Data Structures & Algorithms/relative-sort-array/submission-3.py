class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = [0] * len(arr1)
        j = 0
        count = Counter(arr1)

        for i in range(len(arr2)):
            for k in range(count[arr2[i]]):
                res[j] = arr2[i]
                j += 1
            count[arr2[i]] = 0

        for num in sorted(count):
            for k in range(count[num]):
                res[j] = num
                j += 1

        return res