class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        isPrime = [False] * n
        count = n // 2

        for i in range(3, int(n ** 0.5) + 1, 2):
            if not isPrime[i]:
                for j in range(i * i, n, 2 * i):
                    if not isPrime[j]:
                        isPrime[j] = True
                        count -= 1

        return count
        