# Доработайте функцию ask_number() так, чтобы ее можно было вызывать
# еще с одним параметром - кратностью (величиной шага).
# Сделайте шаг по умолчанию равным 1.

def ask_number(question, low, high, step=1):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response
