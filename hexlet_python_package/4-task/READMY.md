## src/solution.py

Реализуйте функцию `length_of_last_word()`, которая возвращает длину последнего слова переданной на вход строки.
Словом считается любая последовательность не содержащая пробелы, символы перевода строки `\n`и табуляции `\t`.

```python
length_of_last_word('') # 0
length_of_last_word('man in Black') # 5
length_of_last_word('hello, world!     ') # 6
length_of_last_word('hello\t\nworld') # 5
```

## Решение

1. Превращение строки в список слов [Справочник Python-строки](https://code.mu/ru/python/manual/)
   > Метод [split](https://code.mu/ru/python/manual/string/split/)
2. Как учесть все три разделителя?
 - По умолчанию метод `split()` считает все последовательные пробелы за один и убирает их разом. [документация](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split)
2. Выделение последнего слова - идем в теорию --> использую срезы

### Мысль

> А если использовать срезы
