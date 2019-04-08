# def elevator_trips(weights_of_people, floors_to_go, elevator_floors, max_people, max_weight):
# # find the sequence in peoples weight that is less than 200 kilos
#     sum_kilos = 0
#     index = 0
#     current_arr = []
#     trips = 0
#     while index <= len(weights_of_people) - 1:
#         has_room = (sum_kilos + weights_of_people[index]) <=  max_weight and len(current_arr) < max_people
#         if (has_room):
#             sum_kilos += weights_of_people[index]
#             current_arr.append(weights_of_people[index])
#         if (has_room == False):
#             # calculate_trips
#             current_arr = []
#             sum_kilos = 0
#             current_arr.append(weights_of_people[index])
#             sum_kilos += weights_of_people[index]
#             print(current_arr)
#         print(current_arr)
#         index += 1
#     print(current_arr)
#     # if someone in current array calculate_trips


# elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200)


def elevator_trips(weights_of_people, floors_to_go, elevator_floors, max_people, max_weight):
# find the sequence in peoples weight that is less than 200 kilos
    sum_kilos = 0
    index = 0
    current_arr = []
    trips = 0
    while index <= len(weights_of_people) - 1:
        has_room = (sum_kilos + weights_of_people[index]) <=  max_weight and len(current_arr) < max_people
        if (has_room):
            sum_kilos += weights_of_people[index]
            current_arr.append(weights_of_people[index])
            index += 1
        if (has_room == False):
            print(current_arr)
            current_arr = []
            sum_kilos = 0
    print(current_arr)
    # if someone in current array calculate_trips


elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200)

# def elevator_trips2(weights_of_people, floors_to_go, elevator_floors, max_people, max_weight):
# # find the sequence in peoples weight that is less than 200 kilos
#    sum_kilos = 0
#    index = 0
#    current_arr = []
#    trips = 0
#    trip_count = 0
#    while index <= len(weights_of_people) - 1:
#        has_room = (sum_kilos + weights_of_people[index]) <=  max_weight and len(current_arr) < max_people
#        if (has_room):
#            sum_kilos += weights_of_people[index]
#            current_arr.append(floors_to_go[index])
#            index += 1
#        if (has_room == False):
#            print('inside:',current_arr)
#            trip_count += 1 + len(set(current_arr))
#            current_arr = []
#            sum_kilos = 0
#    print('after all:',current_arr)
#    trip_count += 1 + len(set(current_arr))
#    print trip_count