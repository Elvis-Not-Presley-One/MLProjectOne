import csv
import datetime


def log(function_name, error) -> None:
    """
    This function creates a log
    :param function_name: The function name where the log is place
    :param error: the error message
    :return: None
    """
    time = datetime.datetime.now()
    file = 'logs/log.txt'

    try:
        with open(file, 'a') as log_file:
            log_file.write(str(time) + 'Somthing Went Wrong In: ' + function_name + 'Causing Error: ' + error + '\n')
            log_file.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))


def to_csv(file_name, data) -> None:
    """
    This function creates a csv file to print data into
    :param file_name: the file name you want to append into
    :param data: list of data (index, value)
    :return: None
    """
    try:
        with open(file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))