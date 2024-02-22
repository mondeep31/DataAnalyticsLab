def is_empty_by_deletion(s, target):
    while s != target:
        s = s[:-1]
        if not s:
            return False
    return True

# Example
source_string = "abcabc"
target_string = ""
result = is_empty_by_deletion(source_string, target_string)
print(result)
