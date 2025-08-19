class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        flag = True

        for num in range(left, right + 1):
            current_num = num
    
            while current_num > 0:
                current_digit = current_num % 10

                if current_digit != 0:
                    if num % current_digit != 0:
                        flag = False
                else:
                    flag = False

                current_num = current_num // 10

            if flag == True:
                res.append(num)
            else:
                flag = True

        return res
