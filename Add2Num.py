class MyBigNumber:
    num = 0
    def __init__(self):
        self.num = 0

    def sum_core(self, n1, n2): 
        remainder = 0
        num_str = []
        end_of_str_remainder = False
        for i in range(len(n1)):
            # Self explanatory sum
            digit = int(n1[i]) + int(n2[i]) + remainder
            remainder = 0

            # Storing remainder
            if digit >= 10:
                if i == len(n1) - 1:
                    end_of_str_remainder = True
                digit %= 10
                remainder += 1

            num_str.append(digit)
            # Check to see if sum of the last digits still has a remainder
            if end_of_str_remainder:
                num_str.append(1)
        
        # Reverse the array and return it
        return num_str[::-1]

            
    # Note: len of each array is stored in memory for python, therefore len() does not iterate 
    def sum(self, num_1, num_2):
        temp = ''
        # Flip both digits
        rev_n1 = num_1[::-1]
        rev_n2 = num_2[::-1]
        result = []
        
        # Doing extra steps such as adding zeros to the end of the string so that they have equal length
        # When the length of both numbers aren't equal
        if len(num_1) != len(num_2):
            # Swapping the first number with the second one
            if len(num_2) > len(num_1):
                temp = rev_n1
                rev_n1 = rev_n2
                rev_n2 = temp

            num_to_fill = len(rev_n1) - len(rev_n2)
            # Zero fill the shorter number to match the length of the first one
            rev_n2 += "0" * num_to_fill
            result = self.sum_core(rev_n1, rev_n2)
        else:
            result = self.sum_core(rev_n1, rev_n2)

        # Turning the array of number back to a string
        self.num = ''.join(str(num) for num in result) 
        return str(self.num)



        