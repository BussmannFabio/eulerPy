def is_palindrome(n):
    
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_product())
