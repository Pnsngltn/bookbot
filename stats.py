def word_count(text):
    words = text.split()
    wrd_cnt = len(words)
    return wrd_cnt

def letters(text):
    lower_text = text.lower()
    quantities = {ch:0 for ch in lower_text}
    for char in lower_text:
        quantities[char] += 1
    return quantities

def dictionary(data):
    sorted_list = sorted(
        [{"char": k, "num": v} for k, v in data.items()],
        key=lambda x: x["num"],
        reverse=True
    )
    return sorted_list
