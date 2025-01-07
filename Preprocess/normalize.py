import re

from hazm import Normalizer as HNormalizer


class Normalizer:
    def __init__(self):
        pass

    def apply(self, text):
        if text is not None:
            text = self.__remove_punctuations(text)
            text = self.__hazm_normalize(text)
            text = self.__correct_spacing(text)
            return text
        else:
            raise Exception("No content entered.")

    def __hazm_normalize(self, text):
        normalizer = HNormalizer()
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

    def __correct_spacing(self, text):
        cases = [
            "گری", "گر", "ام", "ات", "اش",
            "تر", "تری", "ترین", "ها", "های",
            "هایی", "هایم", "هایت", "هایش", "هایمان", "هایتان", "هایشان"
        ]

        for case in cases:
            text = re.sub(rf'(\w)({case})\b', r'\1‌\2', text)

        return text

    def __remove_punctuations(self, text):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        emails = re.findall(email_pattern, text)

        email_tokens = []
        for email in emails:
            email_token = re.sub(r'[^\w]', '', email)  # Remove @, ., etc.
            email_tokens.append(email_token)
            text = text.replace(email, email_token)

        text = re.sub(r'[^\w\s‌]', '', text)
        return text