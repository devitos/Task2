import hashlib
import os
import sys


def read_sum_file(sum_file='sum_file.txt'):
    sumfile_list = list()
    with open(sum_file, 'r') as sum1:
        data = list(sum1.read().split('\n'))
        for line in data:
            if line:
                sumfile_list.append({'file_name': line.split(' ')[0],
                                     'hash_method': line.split(' ')[1],
                                     'file_sum': line.split(' ')[2]
                                     })
    return sumfile_list


def scan_file(dir_path, input_file, hash_method):
    file_dir = os.listdir(dir_path)
    if input_file['file_name'] in file_dir:
        for file in file_dir:
            if file == input_file['file_name']:
                with open(os.path.join(dir_path, file), 'rb') as f:
                    if input_file['file_sum'] == hashlib.new(hash_method, f.read()).hexdigest():
                        result = 'OK'
                    else:
                        result = 'FAIL'
    else:
        result = 'NOT FOUND'
    return result


def check_sum_file(sum_file, dir_path):
    sum_file_list = read_sum_file(sum_file)
    for file in sum_file_list:
        result = scan_file(dir_path, file, file['hash_method'])
        print(file['file_name'], result)
    return


if __name__ == '__main__':
    if len(sys.argv) == 3:
        check_sum_file(sys.argv[1], sys.argv[2])
    else:
        print('Неверное количество аргументов!')
    check_sum_file('D:\\NEW_Project\\Task2\\sum_file.txt', 'D:\\NEW_Project\\Task2')
