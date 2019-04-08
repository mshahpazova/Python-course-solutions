def gas_stations(distance, tank_size, stations):
    reachable_km = tank_size
    last_station = 0;
    passed_stations = []
    index = 0
    while reachable_km <= distance:
        if reachable_km >= stations[index]:
            last_station = stations[index]
            index += 1
        elif reachable_km < stations[index]:
            passed_stations.append(last_station)
            reachable_km = last_station + tank_size
        if index == len(stations):
            passed_stations.append(last_station)
            break
    return passed_stations

# [70, 140, 210, 280, 350]
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

