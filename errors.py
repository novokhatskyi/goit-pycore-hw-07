def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Такого імені не існує в списку контактів"
        except IndexError:
            return "Не достатньо інформації для виконання запиту"


    return inner
