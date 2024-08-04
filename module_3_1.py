calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string = str(string)
    kort = (len(string), string.upper(), string.lower())
    count_calls()
    return kort


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            list_ = True
        else:
            list_ = False
    return list_


print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False
print(calls)  # 4

