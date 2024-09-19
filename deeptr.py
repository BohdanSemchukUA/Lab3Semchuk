from TranslatorSemchuk.module2 import TransLate, LangDetect, LanguageList, CodeLang

print(TransLate("Good morning", "es", "en"))
print(CodeLang("de"))
detected, confidence = LangDetect("Buen día")
print(f"Detected lang {CodeLang(detected)} in prob {confidence}")
print(LanguageList("Дякую"))
print("Запис у файл...")
LanguageList("Студент", "file")