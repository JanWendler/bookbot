def get_num_words(text):
    return len(text.split())


def count_characters(text):
    count = {}
    for char in list(text.lower()):
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def sort_by_num(items):
    return items["num"]


def sort_characters(count):
    sorted = []
    for entry in count:
        sorted.append({"char": entry, "num": count[entry]})
    sorted.sort(reverse=True, key=sort_by_num)
    return sorted