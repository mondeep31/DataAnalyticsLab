def join_tuples_if_similar_initial(tuples_list):
    result = []
    current_tuple = tuples_list[0]
    for next_tuple in tuples_list[1:]:
        if current_tuple[0] == next_tuple[0]:
            current_tuple = (current_tuple[0], current_tuple[1] + next_tuple[1])
        else:
            result.append(current_tuple)
            current_tuple = next_tuple
    result.append(current_tuple)
    return result

# Example
tuples_list = [(1, 10), (2, 20), (1, 30), (3, 40)]
result = join_tuples_if_similar_initial(tuples_list)
print(result)
