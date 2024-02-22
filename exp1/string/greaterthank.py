def words_greater_than_length(s, k):
    words = s.split()
    result = [word for word in words if len(word) > k]
    return result

# Example
my_string = "Python programming is fun and interesting"
k = 4
result = words_greater_than_length(my_string, k)
print(result)
