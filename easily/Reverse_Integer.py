class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=list(str(x))
            x.reverse()
            x=''.join(x)
            x=int(x)
            if (x>2**31-1):
                return 0
            else:
                return x
        else:
            x=list(str(x))
            x=x[1:]
            x.reverse()
            x=''.join(x)
            result='-'+x
            result=int(result)
            if result<-2**31:
                return 0
            else:
                return result
