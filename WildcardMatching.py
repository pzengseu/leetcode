class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, star_match_pos, last_star_pos, len_s, len_p = 0, 0, 0, -1, len(s), len(p)
        while i < len_s:
            if j < len_p and p[j] in (s[i], '?'):
                i, j = i+1, j+1
            elif j < len_p and p[j] == '*':
                star_match_pos, last_star_pos = i, j
                j += 1
            elif last_star_pos > -1:
                i, star_match_pos = star_match_pos + 1, star_match_pos + 1
                j = last_star_pos + 1
            else:
                return False
        while j < len_p and p[j] == '*': j += 1
        return j == len_p

print Solution().isMatch('asdfasdf', 'asd*g')
