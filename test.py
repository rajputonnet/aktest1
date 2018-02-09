def user_input_list():
    list_string = raw_input("Enter list separated by , [a,b,c] :")
    list_string = list_string[1:len(list_string) - 1]
    list_ = list_string.split(",")
    final_list = []
    for value in list_:
        final_list.append(int(value))
    return final_list


def list_():
    List = [{'x': 100, 'y': 200}, {'x': 100, 'y': 300}, {'x': 120, 'y': 400}, {'x': 200, 'y': 500}]

    for data in List:
        for key, value in data.items():
            print(key, value)

if __name__ == '__main__':
    list_()