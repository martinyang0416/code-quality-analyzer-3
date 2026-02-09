def arrange_words(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    indexed_words = [(len(word), idx, word) for idx, word in enumerate(words)]
    sorted_words = [word for _, _, word in sorted(indexed_words, key=lambda x: (x[0], x[1]))]
    processed = [sorted_words[0].capitalize()]
    for word in sorted_words[1:]:
        processed.append(word.lower())
    return ' '.join(processed)