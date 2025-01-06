def hazm_normalizer(text):
    from hazm import Normalizer
    normalizer = Normalizer()
    text = normalizer.normalize(text)
    text = normalizer.correct_spacing(text)
    text = normalizer.remove_diacritics(text)
    text = normalizer.remove_specials_chars(text)
    text = normalizer.decrease_repeated_chars(text)
    text = normalizer.persian_style(text)
    text = normalizer.persian_number(text)
    text = normalizer.unicodes_replacement(text)
    text = normalizer.seperate_mi(text)

    return text


def parsivar_normalizer(text: str):
    from parsivar import Normalizer
    normalizer = Normalizer()
    return normalizer.normalize(text)
