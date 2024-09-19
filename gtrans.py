from TranslatorSemchuk.module1 import TransLate, LangDetect, LanguageList, CodeLang

print(TransLate("Good morning", "es"))
print(CodeLang("de"))
detected, confidence = LangDetect("Buen día")
print(f"Detected lang: {CodeLang(detected)} in probability {confidence}")
print(LanguageList("Дякую"))
print("Запис у файл...")
LanguageList("Студент", "file")