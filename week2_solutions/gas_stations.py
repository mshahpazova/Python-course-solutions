def gas_stations(distance, tank_size, stations):
    passsed_klm = 0
    passed_stations = []
    station_indexes = range(0, len(stations) - 1)
    reachable_distance = tank_size
    while passsed_klm <= distance:
        for index in station_indexes:
            if reachable_distance >= stations[index]:
                 
                continue
            print(stations[index])
            passsed_klm += stations[index]
            reachable_distance += stations[index]
            passed_stations.append(stations[index])
    return passed_stations

def can_reach_next_station(tank, next_station):
        if tank >= next_station:
            return True
        else:
            return False
  
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

# Test Example
# >>> gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
# [80, 140, 220, 290]
# >>> gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
# [70, 140, 210, 280, 350]
[90, 140, 210, 240, 280, 350]
[70, 90, 140, 210, 240, 280, 350]
# assert(prime_factorization(10)== [(2, 1), (5, 1)]) # This is 2^1 * 5^1
# assert(prime_factorization(14) == [(2, 1), (7, 1)])
# assert(prime_factorization(356) == [(2, 2), (89, 1)])
# assert(prime_factorization(89) == [(89, 1)]) # 89 is a prime number
# assert(prime_factorization(1000) == [(2, 3), (5, 3)])