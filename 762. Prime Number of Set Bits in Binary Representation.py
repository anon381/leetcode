
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2,3,5,7,11,13,17,19}
        ## simple but not accurate for long digits.
        return sum(1 for x in range(left, right+1) if bin(x).count('1') in primes)
## or 

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n<=1:
                return False
            if n==2:
                return True
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        c=0
        for i in range(left,right+1):
            val=bin(i)
            x=val.count('1')
            if isPrime(x):
                c+=1
        return c
