#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
     new_list = []
    for q in range(list_length):
        try:
            new_list.append(my_list_1[q] / my_list_2[q])
        except IndexError:
            new_list.append(0)
            print('out of range')
        except TypeError:
            new_list.append(0)
            print('wrong type')
        except ZeroDivisionError:
            new_list.append(0)
            print('division by 0')
        finally:
            pass

    return new_list
