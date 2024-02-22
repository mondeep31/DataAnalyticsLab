def uncommon_words(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    uncommon = set1.symmetric_difference(set2)
    return list(uncommon)

# Example
string1 = "Python is fun"
string2 = "Python is easy"
result = uncommon_words(string1, string2)
print(result)
