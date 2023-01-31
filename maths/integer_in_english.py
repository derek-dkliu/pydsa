from collections import deque

def int_english(n):
    if n == 0:
        return 'Zero'

    negative = False
    if n < 0:
        n = -n
        negative = True

    units = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion']
    index = 0
    result = deque()
    while n > 0:
        if n % 1000 != 0:
            s = hundred(n % 1000)
            result.appendleft(s + ' ' + units[index])
        index += 1
        n //= 1000
        
    result = ', '.join(result)
    if negative:
        result = 'Negative ' + result
    return result

def hundred(n):
    smalls = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    result = []
    if n >= 100:
        result.append(smalls[n // 100] + ' Hundred')
        n %= 100
    if n < 20:
        result.append(smalls[n])
    else:
        result.append(tens[n // 10])
        if n % 10 != 0:
            result.append(smalls[n % 10])
    return ' '.join(result)

cases = [9, 10, 11, 31, 40, 100, 414, 123, 950, 1000, 1001, 1012, 1300, 1000100, 43215, 9876543210, -111111, 0]
for num in cases:
    print(int_english(num))
