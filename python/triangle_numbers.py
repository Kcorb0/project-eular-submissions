import requests

# Load file
url = 'https://projecteuler.net/project/resources/p042_words.txt'
req = requests.get(url, allow_redirects=True).text.replace("\"", "").split(',')


def is_tringle_word(word):
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    tri_nums = [int(i/2*(i+1)) for i in range(1, 20)]

    num = sum([alpha.index(i)+1 for i in word.lower()])

    return True if num in tri_nums else False

count = 0
for i in req:
    if is_tringle_word(i):
        count+=1
    
print(count)
