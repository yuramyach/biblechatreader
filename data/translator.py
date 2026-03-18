import json
import os

# Словари названий книг
RU_MAP = {
    "Genesis": "Бытие", "Exodus": "Исход", "Leviticus": "Левит", "Numbers": "Числа", "Deuteronomy": "Второзаконие",
    "Joshua": "Иисус Навин", "Judges": "Судьи", "Ruth": "Руфь", "1 Samuel": "1 Царств", "2 Samuel": "2 Царств",
    "1 Kings": "3 Царств", "2 Kings": "4 Царств", "1 Chronicles": "1 Паралипоменон", "2 Chronicles": "2 Паралипоменон",
    "Ezra": "Ездра", "Nehemiah": "Неемия", "Esther": "Есфирь", "Job": "Иов", "Psalms": "Псалтирь", "Psalm": "Псалтирь",
    "Proverbs": "Притчи", "Ecclesiastes": "Екклесиаст", "Song of Solomon": "Песня песней",
    "Song of Songs": "Песня песней",
    "Isaiah": "Исайя", "Jeremiah": "Иеремия", "Lamentations": "Плач Иеремии", "Ezekiel": "Иезекиль", "Daniel": "Даниил",
    "Hosea": "Осия", "Joel": "Иоиль", "Amos": "Амос", "Obadiah": "Авдий", "Jonah": "Иона", "Micah": "Михей",
    "Nahum": "Наум", "Habakkuk": "Аввакум", "Zephaniah": "Софония", "Haggai": "Аггей", "Zechariah": "Захария",
    "Malachi": "Малахия",
    "Matthew": "Матфея", "Mark": "Марка", "Luke": "Луки", "John": "Иоанна", "Acts": "Деяния", "Romans": "Римлянам",
    "1 Corinthians": "1 Коринфянам", "2 Corinthians": "2 Коринфянам", "Galatians": "Галатам", "Ephesians": "Ефесянам",
    "Philippians": "Филиппийцам", "Colossians": "Колоссянам", "1 Thessalonians": "1 Фессалоникийцам",
    "2 Thessalonians": "2 Фессалоникийцам",
    "1 Timothy": "1 Тимофею", "2 Timothy": "2 Тимофею", "Titus": "Титу", "Philemon": "Филимону", "Hebrews": "Евреям",
    "James": "Иакова", "1 Peter": "1 Петра", "2 Peter": "2 Петра", "1 John": "1 Иоанна", "2 John": "2 Иоанна",
    "3 John": "3 Иоанна", "Jude": "Иуды", "Revelation": "Откровение"
}

UK_MAP = {
    "Genesis": "Буття", "Exodus": "Вихід", "Leviticus": "Левит", "Numbers": "Числа", "Deuteronomy": "Повторення Закону",
    "Joshua": "Ісус Навин", "Judges": "Судді", "Ruth": "Рут", "1 Samuel": "1 Самуїла", "2 Samuel": "2 Самуїла",
    "1 Kings": "1 Царів", "2 Kings": "2 Царів", "1 Chronicles": "1 Хронік", "2 Chronicles": "2 Хронік",
    "Ezra": "Ездра", "Nehemiah": "Неємія", "Esther": "Естер", "Job": "Йов", "Psalms": "Псалми", "Psalm": "Псалми",
    "Proverbs": "Приповісті", "Ecclesiastes": "Екклезіяст", "Song of Solomon": "Пісня пісень",
    "Song of Songs": "Пісня пісень",
    "Isaiah": "Ісая", "Jeremiah": "Єремія", "Lamentations": "Плач Єремії", "Ezekiel": "Єзекіїль", "Daniel": "Даниїл",
    "Hosea": "Осія", "Joel": "Йоїл", "Amos": "Амос", "Obadiah": "Овадія", "Jonah": "Йона", "Micah": "Михей",
    "Nahum": "Наум", "Habakkuk": "Авакум", "Zephaniah": "Софонія", "Haggai": "Огій", "Zechariah": "Захарія",
    "Malachi": "Малахія",
    "Matthew": "Матвія", "Mark": "Марка", "Luke": "Луки", "John": "Івана", "Acts": "Дії", "Romans": "Римлян",
    "1 Corinthians": "1 Коринтян", "2 Corinthians": "2 Коринтян", "Galatians": "Галатів", "Ephesians": "Ефесян",
    "Philippians": "Филип'янам", "Colossians": "Колосян", "1 Thessalonians": "1 Солунян",
    "2 Thessalonians": "2 Солунян",
    "1 Timothy": "1 Тимофія", "2 Timothy": "2 Тимофія", "Titus": "Тита", "Philemon": "Филимону", "Hebrews": "Євреїв",
    "James": "Якова", "1 Peter": "1 Петра", "2 Peter": "2 Петра", "1 John": "1 Івана", "2 John": "2 Івана",
    "3 John": "3 Івана", "Jude": "Юди", "Revelation": "Об'явлення"
}

ES_MAP = {
    "Genesis": "Génesis", "Exodus": "Éxodo", "Leviticus": "Levítico", "Numbers": "Números",
    "Deuteronomy": "Deuteronomio",
    "Joshua": "Josué", "Judges": "Jueces", "Ruth": "Rut", "1 Samuel": "1 Samuel", "2 Samuel": "2 Samuel",
    "1 Kings": "1 Reyes", "2 Kings": "2 Reyes", "1 Chronicles": "1 Crónicas", "2 Chronicles": "2 Crónicas",
    "Ezra": "Esdras", "Nehemiah": "Nehemías", "Esther": "Ester", "Job": "Job", "Psalms": "Salmos", "Psalm": "Salmos",
    "Proverbs": "Proverbios", "Ecclesiastes": "Eclesiastés", "Song of Solomon": "Cantares", "Song of Songs": "Cantares",
    "Isaiah": "Isaías", "Jeremiah": "Jeremías", "Lamentations": "Lamentaciones", "Ezekiel": "Ezequiel",
    "Daniel": "Daniel",
    "Hosea": "Oseas", "Joel": "Joel", "Amos": "Amós", "Obadiah": "Abdías", "Jonah": "Jonás", "Micah": "Miqueas",
    "Nahum": "Nahúm", "Habakkuk": "Habacuc", "Zephaniah": "Sofonías", "Hageo": "Hageo", "Zechariah": "Zacarías",
    "Malachi": "Malaquías",
    "Matthew": "Mateo", "Mark": "Marcos", "Luke": "Lucas", "John": "Juan", "Acts": "Hechos", "Romans": "Romanos",
    "1 Corinthians": "1 Corintios", "2 Corinthians": "2 Corintios", "Galatians": "Gálatas", "Ephesians": "Efesios",
    "Philippians": "Filipenses", "Colossians": "Colosenses", "1 Thessalonians": "1 Tesalonicenses",
    "2 Thessalonians": "2 Tesalonicenses",
    "1 Timothy": "1 Timoteo", "2 Timothy": "2 Timoteo", "Titus": "Tito", "Filemón": "Filemón", "Hebrews": "Hebreos",
    "James": "Santiago", "1 Peter": "1 Pedro", "2 Peter": "2 Pedro", "1 John": "1 Juan", "2 John": "2 Juan",
    "3 John": "3 Juan", "Judas": "Judas", "Revelation": "Apocalipsis"
}

TASKS = {
    "ru_synodal.json": RU_MAP,
    "uk_ogienko.json": UK_MAP,
    "es_rv.json": ES_MAP
}


def process_bible(filename, mapping):
    # Ищем файл в текущей папке или в data/
    path = filename
    if not os.path.exists(path):
        path = os.path.join("data", filename)

    if not os.path.exists(path):
        print(f"⚠️ Файл {filename} не найден.")
        return

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Отрезаем лишнее
        if 'books' in data and len(data['books']) > 66:
            data['books'] = data['books'][:66]

        # Переводим
        for book in data.get('books', []):
            name = book.get('name', '').strip()
            if name in mapping:
                book['name'] = mapping[name]

        # СОХРАНЯЕМ С ОТСТУПАМИ (indent=2) — НЕ В ОДНУ СТРОКУ
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ {path}: Готово! Структура сохранена.")

    except Exception as e:
        print(f"❌ Ошибка в {filename}: {e}")


if __name__ == "__main__":
    for file, mapper in TASKS.items():
        process_bible(file, mapper)
    print("\n🏁 Все готово. Слушай проповедь спокойно!")