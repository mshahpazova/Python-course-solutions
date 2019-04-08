def gas_stations(distance, tank_size, stations):
    reachable = tank_size
    last_station = 0;
    passed_stations = []
    index = 0
    while reachable <= distance:
        while index < len(stations):
            print("try with ", stations[index])
            if reachable >= stations[index]:
                last_station = stations[index]
                # index += 1
            else:
                print("Cannot reach ", stations[index])
                print("But reached ", last_station)
                passed_stations.append(last_station)
                reachable = last_station + tank_size
                print("Could reach up to ", reachable)
            index += 1
        # if last_station != passed_stations[-1]:
        #     print("Last reached ", last_station)
        #     passed_stations.append(last_station)
        #     reachable = last_station + tank_size
            # if reachable < distance: print "Cant reach destination"
    return passed_stations

print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
# assert(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])==[70, 140, 210, 280, 350])
# assert(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290])