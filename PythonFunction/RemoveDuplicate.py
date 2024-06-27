def remove_duplicates(input):
    tracking = set()
    output_list = []
    for i in input:
        if i not in tracking:
            output_list.append(i)
            tracking.add(i)
    return output_list

number_list = [1, 2, 3, 2, 1, 4, 5, 4]
cars_list = ['Toyota', 'BMW', 'Mercedes', 'Tesla', 'BMW', 'Toyota']
output_number = remove_duplicates(number_list)
output_cars = remove_duplicates(cars_list)
print(output_number)
print(output_cars)