class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            temp = i
            binary_num = ''
            while temp > 0:
                curr = temp % 2
                binary_num += str(curr)
                temp = int(temp / 2)

            reversed_string = binary_num[::-1]
            dp[i] = reversed_string.count('1')

        return dp


            



    
        





        