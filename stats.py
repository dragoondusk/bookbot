def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    lowercase = text.lower()
    for letter in lowercase:
         if letter not in character_count:
             character_count[letter] = 1
         else:
             character_count[letter]=character_count[letter]+1
    return character_count

def sort_on(d):
    return d["num"]


def character_count_to_sorted_list(num_character_count):
    sorted_list = []
    for ch in num_character_count:
        sorted_list.append({"char": ch, "num": num_character_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
