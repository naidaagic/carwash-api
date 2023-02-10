"""
    For a random array of structs of type {id, value }, return a new struct, with a unique
    id and a value such as the next positive integer, which isn't present in the existing
    structure list and with at least one smaller integer appearing at least twice in the
    same list.

    For example:
    a = [{id:1, value:3}, {id:2, value:7}, {id:3, value:3}, {id:4, value:1}, {id:5, value:4}]
    value 1 - appears once
    value 3 - appears 2 times
    value 4 - appears once
    value 7 - appears once
    Solution: {id: 6, value: 5}
"""

if __name__ == "__main__":

    input_list = [(1, 3), (2, 7), (3, 3), (4, 1), (5, 4)]

    id_list = [_id for _id, _ in input_list]
    value_list = [value for _, value in input_list]

    new_id = max(id_list) + 1

    value_list.sort()
    new_value = value_list[-1]+1
    reappearing_num = None
    for i in range(len(value_list)-1):
        if reappearing_num:
            diff = value_list[i + 1] - value_list[i]
            if diff > 1:
                new_value = value_list[i] + 1
                break
        elif value_list[i] == value_list[i+1]:
            reappearing_num = value_list[i]

    if not reappearing_num:
        print("There are no values that appear at least twice in the list")
    else:
        print(f"Solution: {{id={new_id}, value={new_value}}}")
