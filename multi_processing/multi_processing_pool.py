import multiprocessing as mp


def main_map(i):
    result = i*i
    print(result)
    return result


# if __name__ == '__main__':
#     inputs = [0,1,2,3,4,5,6,7,8,9]
#     pool = mp.Pool(4)
#     pool_output = pool.map(main_map, inputs)
#     print('IOESJRLKJOI J')
#     print(pool_output)

if __name__ == '__main__':
    inputs = [0,1,2,3,4,5,6,7,8,9]
    pool = mp.Pool(4)
    pool_output = pool.map_async(main_map, inputs)
    print('IOESJRLKJOI J')

    pool.close()
    pool.join()