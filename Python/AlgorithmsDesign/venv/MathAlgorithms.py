import math

class MathAlgorithms:

    @staticmethod
    def GradeSchoolMultiplication(firstNum, secondNum):

        S_SecondNum = str(secondNum)

        sum = 0

        i = len(S_SecondNum)-1
        j = 0
        while i >= 0:
            sum += (firstNum * int(S_SecondNum[i])) * math.pow(10, j)
            i -= 1
            j += 1
            pass

        return int(sum)

    @staticmethod
    def KaratsubaMultiplication(firstNum, secondNum):

        # Find the min size of two integers
        n = min(len(str(firstNum)), len(str(secondNum)))

        # Base case
        if n == 1:
            return firstNum * secondNum

        n = int(n / 2)

        # The power for calculating a, b, c, d

        p = math.pow(10, n)

        a = int(firstNum / p)
        b = int(firstNum % p)
        c = int(secondNum / p)
        d = int(secondNum % p)

        # Performing Karatsuba equation = > ac * 10 ^ n + (10 ^ ((n + 1) / 2)) * (ad + bc) + bd
        ac = MathAlgorithms.KaratsubaMultiplication(a, c)
        bd = MathAlgorithms.KaratsubaMultiplication(b, d)
        f = MathAlgorithms.KaratsubaMultiplication(a + b, c + d)
        return int((math.pow(10, 2 * n) * ac) + bd + ((f - bd - ac) * p))
