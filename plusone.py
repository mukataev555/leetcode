class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1): #Начинаем с последнего элемента в массиве, так как его будем на +1 менять
            if digits[i] < 9: 
                digits[i] += 1 #в наш последний элемент прибавляем +1 и выводим целый массив
                return digits
            digits[i] = 0 
        return [1] + digits

