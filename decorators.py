

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print('check the correctness of the information and try again')
        except KeyError:
            print('check the correctness of the information and try again')
        except IndexError:
            print('check the correctness of the information and try again')
        except TypeError:
            pass
    return wrapper
