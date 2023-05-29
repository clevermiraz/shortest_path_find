import math

locations = {
    1: (23.8728568, 90.3984184, "Uttara Branch"),
    2: (23.8513998, 90.3944536, "City Bank Airport"),
    3: (23.8330429, 90.4092871, "City Bank Nikunja"),
    4: (23.8679743, 90.3840879, "City Bank Beside Uttara Diagnostic"),
    5: (23.8248293, 90.3551134, "City Bank Mirpur 12"),
    6: (23.827149, 90.4106238, "City Bank Le Meridien"),
    7: (23.8629078, 90.3816318, "City Bank Shaheed Sarani"),
    8: (23.8673789, 90.429412, "City Bank Narayanganj"),
    9: (23.8248938, 90.3549467, "City Bank Pallabi"),
    10: (23.813316, 90.4147498, "City Bank JFP")
}

def calculate_distance(loc1, loc2):
    """
    Calculate the distance (in kilometers) between two locations
    using the Haversine formula.
    """
    lat1, lon1 = loc1[0], loc1[1]
    lat2, lon2 = loc2[0], loc2[1]
    radius = 6371  # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance

def tsp_nearest_neighbor(start_location, locations):
    """
    Solve the Traveling Salesman Problem using the Nearest Neighbor Algorithm.
    Returns the optimized route as a list of location IDs.
    """
    unvisited = set(locations.keys())
    current_location = start_location
    route = [current_location]

    while unvisited:
        nearest_distance = float('inf')
        nearest_location = None

        for location in unvisited:
            distance = calculate_distance(locations[current_location], locations[location])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_location = location

        route.append(nearest_location)
        unvisited.remove(nearest_location)
        current_location = nearest_location

    return route

# Main program
start_location = 1  # City Bank Uttara Branch
optimized_route = tsp_nearest_neighbor(start_location, locations)

# Print the optimized route
print("Optimized Route: \n")
for location in optimized_route:
    print(f"{location}: {locations[location][2]}")
