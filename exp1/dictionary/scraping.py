import requests

def find_ordered_words(url):
    response = requests.get(url)
    words = response.text.split('\n')
    
    ordered_words = [word for word in words if ''.join(sorted(word)) == word]
    return ordered_words

# Example
url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
result = find_ordered_words(url)
print(result[:10])  # Displaying the first 10 ordered words for brevity
