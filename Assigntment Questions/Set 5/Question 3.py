def check_double(number):
    double = 2 * number
    double = str(double)
    n = str(number)
    count = 0
    if len(double) == len(n):
        for i in double:
            if i in n:
                count += 1
        if count == len(n):
            return True
        else: 
            return False
    else:
        return False

print(check_double(125874))