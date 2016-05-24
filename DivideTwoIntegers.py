class Solution(object):
    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0
        sign1 = -1 if dividend < 0 else 1
        sign2 = -1 if divisor < 0 else 1
        sign = sign1 * sign2
        divisor = abs(divisor)
        denominator = abs(dividend)
        ret = 0
        if dividend >= 2 ** 32:
            if sign < 0: return -2 ** 32
            else: return 2 ** 32 - 1

        if divisor == 1: return dividend

        while denominator>0:
            denominator -= divisor
            if denominator >= 0:
                ret += 1

        return ret * sign

    def divide(self, dividend, divisor):
        if dividend == 0: return 0
        sign1 = -1 if dividend < 0 else 1
        sign2 = -1 if divisor < 0 else 1
        sign = sign1 * sign2
        divisor = abs(divisor)
        denominator = abs(dividend)
        ret = 0

        while denominator >= divisor:

            c = divisor
            i = 0
            while denominator >= c:
                denominator -= c
                ret += 1<<i
                i += 1
                c <<= 1

        ret = ret * sign
        if ret > 2 ** 31 - 1: return 2 ** 31 - 1
        if ret < -2 ** 31: return -2 ** 31

        return ret

print Solution().divide(10, -2)

 1 class Solution
 2 {
 3 public:
 4     vector<int> findSubstring(string S, vector<string> &L)
 5     {
 6         vector<int> vi;
 7         if(L.size() == 0)
 8             return vi;
 9
10         unordered_map<string, int> msi;
11         for (int i = 0; i < L.size(); ++ i)
12             ++ msi[L[i]];
13
14         for(int i = 0; i < L[0].size(); ++ i)
15         {
16             int b = i, cnt = 0;
17             unordered_map<string, int> tempmsi;
18             for(int j = i; j + L[0].size() <= S.size(); j += L[0].size())
19             {
20                 string str = S.substr(j, L[0].size());
21                 if(msi.find(str) != msi.end())
22                 {
23                     ++ tempmsi[str];
24                     ++ cnt;
25                     if(tempmsi[str] > msi[str])
26                     {
27                         while(tempmsi[str] > msi[str])
28                         {
29                             string s = S.substr(b, L[0].size());
30                             -- tempmsi[s];
31                             -- cnt;
32                             b += L[0].size();
33                         }
34                     }
35                     else if(cnt == L.size())
36                     {
37                         vi.push_back(b);
38                         -- tempmsi[S.substr(b, L[0].size())];
39                         -- cnt;
40                         b += L[0].size();
41                     }
42                 }
43                 else
44                 {
45                     tempmsi.clear();
46                     b = j + L[0].size();
47                     cnt = 0;
48                 }
49             }
50         }
51         return vi;
52     }
53 };