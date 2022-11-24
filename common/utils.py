def _ring_generator(size, max_step):
    _ = list(range(size))
    i = 0
    for s in range(max_step):
        yield _[i]
        i = 0 if i + 1 == size else i + 1


def get_element_from_dict(target_dict, num):
    """
    {
        "a": [1, 4, 7],
        "b": [2, 5],
        "c": [3, 6]
    }
    get 4
    [1, 2, 3, 4]
    :param target_dict:
    :param num: element number
    :return:
    """
    two_dimensional_arr = []
    v_len_list = []
    for v in target_dict.values():
        if v:
            two_dimensional_arr.append(v)
            v_len_list.append(len(v))

    arr_len = len(v_len_list)
    element_total_count = sum(v_len_list)
    result = []
    index_record = [0 for _ in range(arr_len)]
    max_step = arr_len * max(v_len_list) if v_len_list else 0
    rg = _ring_generator(arr_len, max_step)
    if not two_dimensional_arr:
        return result
    for i in range(num):
        index = next(rg)
        while index_record[index] >= v_len_list[index]:
            index = next(rg)
        result.append(two_dimensional_arr[index][index_record[index]])
        index_record[index] += 1
        if element_total_count <= i + 1:
            break
    return result