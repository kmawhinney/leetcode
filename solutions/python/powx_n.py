class Solution:
    def myPow(self, x: float, n: int) -> float:
        # When n is 0, result is always 1
        if n == 0:
            return 1

        # When n is negative, we can flip x
        if n < 0:
            return 1 / self.myPow(x, -n)

        # When n is odd, we want to factor x out once to make n even
        if n % 2 != 0:
            return x * self.myPow(x, n-1)

        # When n is even, we multiply x by itself and halve n
        # Justification: 2^8 == 256
        #          2*2 = 4^4 == 256
        #         4*4 = 16^2 == 256
        return self.myPow(x*x, n/2)
