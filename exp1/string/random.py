import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_until_match(target_string):
    generated_string = ""
    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
    return generated_string

# Example
target_string = "hello"
result = generate_until_match(target_string)
print(result)
