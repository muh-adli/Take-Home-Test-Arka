def remove_duplicates(input):
    tracking = set()
    output_list = []
    for i in input:
        if i not in tracking:
            output_list.append(i)
            tracking.add(i)
    return output_list