class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = [[0 for i in xrange(len(word2)+1)] for j in xrange(len(word1)+1)]
        for i in xrange(len(word1)+1):
            distance[i][0] = i
        for j in xrange(len(word2)+1):
            distance[0][j] = j

        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    distance[i][j] = distance[i-1][j-1]
                else:
                    distance[i][j] = min(distance[i-1][j]+1, distance[i][j-1]+1, distance[i-1][j-1]+1)

        return distance[-1][-1]