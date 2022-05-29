words = ['Apple', 'Oranges', 'Tomatoes', 'Beans',
         'Peanuts', 'Celery', 'Cabbage', 'Coconut', 'Lemon']


def remove_vowels(words):
    vowel_removed_words = []
    vowel_removed_word = []
    for word in words:
        for letter in word:
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                continue
            else:
                vowel_removed_word.append(letter)
        vowel_removed_words.append(''.join(vowel_removed_word))
        vowel_removed_word.clear()

    return vowel_removed_words


print(remove_vowels(words))
