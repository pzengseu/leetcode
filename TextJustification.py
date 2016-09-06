class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        width = len(words[0])
        num = 1
        last = 0

        for i in xrange(1, len(words)):
            width += len(words[i])
            num += 1
            if (width + num - 1) > maxWidth:
                width -= len(words[i])
                num -= 1

                temp = ''
                if num == 1:
                    temp = words[i-1] + (maxWidth - width) * ' '
                    res.append(temp)
                else:
                    maxGap = maxWidth - width
                    gap = 0
                    for j in xrange(last, i):
                        if j == i - 1: gap = 0
                        else:
                            gap = maxGap / (num - 1)
                            gap = gap + 1 if maxGap % (num - 1) > 0 else gap
                            maxGap -= gap
                        temp = temp + words[j] + gap * ' '
                        num -= 1
                    res.append(temp)

                last = i
                width = len(words[i])
                num = 1

        i = last
        temp = ''
        while i < len(words):
            if i != len(words) - 1:
                temp = temp + words[i] + ' '
            else:
                temp += words[i]
            i += 1
        res.append(temp+(maxWidth-len(temp))*' ')

        return res

print Solution().fullJustify(["a","b","c","d","e"], 3)


