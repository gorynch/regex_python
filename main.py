import re
import csv

from vars import file_name_raw, file_name_formated, pattern_all, str_replace, \
    str_pattern_empty_phone, index_from_diff


def read_file(f_n):
    with open(f_n) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def write_file(f_n, contact_list):
    with open(f_n, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contact_list)


def format_data(input_data):
    res_str = ','.join(input_data[0]) + '\n'
    input_data.pop(0)
    for data in input_data:
        if len(data) == len(input_data[0]):
            names = re.finditer(pattern_all,','.join(data))
            for n in names:
                sub_names = f'{n.group(1)},{n.group(3)},{n.group(5)}'
                pattern_names = rf'{sub_names},(.+\s)'
                str_new = re.sub(pattern_all, str_replace, n.group())
                if n.group(16) == None:
                    str_new = re.sub(str_pattern_empty_phone, '', str_new)
                elif 'доб.' not in n.group(16):
                    lst = str_new.split(',')
                    phone = lst[5][:-1]
                    lst[5] = phone
                    str_new = ','.join(lst)
                sub_str = re.search(pattern_names, res_str)
                if sub_str:
                    sub_data = res_str[sub_str.start():sub_str.end()][:-1].split(",")
                    data_2_mix = str_new.split(',')
                    for i in range(index_from_diff,len(sub_data)):
                        if data_2_mix[i] == '':
                            if sub_data[i] != '':
                                data_2_mix[i] = sub_data[i]
                    str_new = ','.join(data_2_mix)
                    index_end_row = -3
                    for i in range(sub_str.start(),len(res_str)):
                        if res_str[i] == '\n':
                            index_end_row = i
                            break
                    res_str = res_str[:sub_str.start()] + res_str[index_end_row:]
                if str_new[-1] == ',':
                    str_new = str_new[:-1]
                    str_new = str_new + f'\n'
                res_str = res_str + str_new
        else:
            print(f'Строка : {data} не соответствует входным требованиям, количество элементов отличается от остальных строк')

    res1 = [c for c in (s.split(',') for s in res_str.splitlines()) if c]
    return res1

if __name__ == '__main__':
    print("Let's start")
    print()
    contact_list_formated = format_data(read_file(file_name_raw))
    write_file(file_name_formated, contact_list_formated)
    print('Done.')