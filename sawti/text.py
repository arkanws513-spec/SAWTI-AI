from __future__ import annotations
import unicodedata

_ALEF = str.maketrans({"أ":"ا","إ":"ا","آ":"ا","ٱ":"ا"})
_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹","٠١٢٣٤٥٦٧٨٩")

def normalize_arabic_text(value: str, *, remove_diacritics: bool = False) -> str:
    """Conservative normalization for transcript comparison; source text is untouched."""
    value = unicodedata.normalize("NFC", value).replace("ـ","").translate(_ALEF).translate(_DIGITS)
    if remove_diacritics:
        value = "".join(c for c in unicodedata.normalize("NFD", value) if unicodedata.category(c) != "Mn")
        value = unicodedata.normalize("NFC", value)
    return " ".join(value.split())
