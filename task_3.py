# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def hashable_dicts(**kwargs):
    animals = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        animals[v] = k
    return animals


print(hashable_dicts(cat='Jack', leopard={'Leopold': 3, 'Murka': 1}, leon=['bill', 'jack', 'anatoliy'],
                     elephant={'edward', 'murka'}))
