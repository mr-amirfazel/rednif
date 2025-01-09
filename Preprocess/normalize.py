import re

from hazm import Normalizer as HNormalizer


class Normalizer:
    def __init__(self):
        self.abbreviations = {
            "ا.م.": "استاندار محترم",
            "د.ک.": "دکتری",
            "ص.ن.": "صبحانه ناهار",
            "پ.ن.": "پاورقی نویسنده",
            "ق.ا.": "قانون اساسی",
            "ه.ش.": "هجری شمسی",
            "ه.ق.": "هجری قمری",
            "م.م.": "معاون مدیر",
            "ت.ت.": "تحقیق و توسعه",
            "ر.ک.": "رجوع کنید",
            "خ.ه.": "خارج از حوزه",
            "ن.م.": "نامعلوم",
            "ب.ن.": "به نظر",
            "ت.ش.": "تحقیق شده",
            "م.ه.": "محل همایش"
        }
        self.__normalizer = HNormalizer()

    def apply(self, text):
        if text is not None:
            text = self.__remove_punctuations(text)
            text = self.__hazm_normalize(text)
            text = self.__correct_spacing(text)
            text = self.__remove_abbreviations(text)
            return text
        else:
            raise Exception("No content entered.")

    def __hazm_normalize(self, text):
        text = self.__normalizer.normalize(text)
        text = self.__normalizer.correct_spacing(text)
        text = self.__normalizer.remove_diacritics(text)
        text = self.__normalizer.remove_specials_chars(text)
        text = self.__normalizer.decrease_repeated_chars(text)
        text = self.__normalizer.persian_style(text)
        text = self.__normalizer.persian_number(text)
        text = self.__normalizer.unicodes_replacement(text)
        text = self.__normalizer.seperate_mi(text)
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

    def __remove_abbreviations(self, text):
        for abbr, full_form in self.abbreviations.items():
            text = text.replace(abbr, full_form)
        return text