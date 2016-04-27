class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        sortNums = sorted(nums)
        twoSum = {}
        cnt = {}
        res = []
        for i in xrange(len(sortNums)):
            if sortNums[i] in cnt: cnt[sortNums[i]] += 1
            else: cnt[sortNums[i]] = 1

        for i in xrange(len(sortNums)-1):
            for j in xrange(i+1,len(sortNums)):
                if twoSum.has_key(sortNums[i] + sortNums[j]):
                    twoSum[sortNums[i] + sortNums[j]].add((sortNums[i], sortNums[j]))
                else:
                    twoSum[sortNums[i] + sortNums[j]] = set()
                    twoSum[sortNums[i] + sortNums[j]].add((sortNums[i], sortNums[j]))

        for first in sorted(twoSum.keys()):
            if (target - first) < first: break
            if (target - first) in twoSum:
                for a in twoSum[first]:
                    for b in twoSum[target - first]:
                        temp = sorted(a+b)
                        tempNums = {}
                        for n in temp:
                            if n in tempNums: tempNums[n] += 1
                            else: tempNums[n] = 1
                        flag = 1
                        for n in tempNums:
                            if tempNums[n] > cnt[n]:
                                flag = 0
                                break
                        if flag and temp not in res: res.append(temp)

        return res

    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        nums = sorted(nums)
        res = []
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums)-2):
                m = j+1
                k = len(nums) - 1
                while m < k:
                    if nums[i] + nums[j] + nums[m] + nums[k] == target:
                        res.append((nums[i], nums[j], nums[m], nums[k]))
                    if nums[i] + nums[j] + nums[m] + nums[k] < target: m += 1
                    else: k -= 1

        return [list(l) for l in {}.fromkeys(res).keys()]

print Solution().fourSum2([2,1,0,-1], 2)