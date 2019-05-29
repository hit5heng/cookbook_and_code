states_needed = set(["id", "nv", "ut", "wa", "mt", "or", "ca", "az"])

stations = {}
stations["k1"] = set(["id", "nv", "ut"])
stations["k2"] = set(["wa", "id", "mt"])
stations["k3"] = set(["or", "nv", "ca"])
stations["k4"] = set(["nv", "ut"])
stations["k5"] = set(["ca", "az"])

print(stations)
print(states_needed)

final_station = set()
best_station = None
states_covered = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_station.add(best_station)
    states_needed -= states_covered

print(final_station)
