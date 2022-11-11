def get_count_char(str_):
    symbol_dict = {}
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha():
            symbol_dict[symbol] = symbol_dict.get(symbol, 0) + 1
    return symbol_dict

def get_percent_char(dict_=None):
    if dict_ is None:
        dict_ = {}

    new_symbol_dict = {}
    total_symbol = sum(dict_.values())

    for symbol in dict_:
        new_symbol_dict[symbol] = round((dict_.get(symbol) / total_symbol) * 100, 2)
    return new_symbol_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percent_char(get_count_char(main_str)))
