def calculate_sequence_value(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    elif n == 3:
        return 8
    else:
        a = 2
        b = 5
        c = 8
        for i in range(4, n + 1):
            if i % 2 == 0:
                next_number = c + 6
            else:
                next_number = c + 3
            a = b
            b = c
            c = next_number
        return c

n = int(input("Provide position number (n): "))
result = calculate_sequence_value(n)
print(f"value of  {n} is: {result}")


# Counting values for sequence: 2, 5, 8, 14, 17, ... 
