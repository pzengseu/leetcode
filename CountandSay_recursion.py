class Solution:
    # @param {integer} n
    # @return {string}
    def cands(self,n):
        if n==1:
            st="1"
            return st
        else:
            st=self.cands(n-1)
            count=1
            same=''
            se=''
            for i in range(len(st)):
                if same!=st[i]:
                    if same !='':
                        se+=str(count)
                        se+=same
                    same=st[i]
                    count=1
                else:
                    count+=1
            se+=str(count)
            se+=same
            return se
    def countAndSay(self, n):

        return self.cands(n)

print Solution().countAndSay(3)