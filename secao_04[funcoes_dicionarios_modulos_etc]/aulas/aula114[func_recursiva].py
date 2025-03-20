def factorial(num):
    if num <= 1:
        return 1
    
    # função recursiva   
    return num * factorial(num - 1)

print(100 * "=")
print(factorial(1))
print(factorial(5))
print(100 * "=")