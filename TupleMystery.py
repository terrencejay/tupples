def get_user_itineraries():
    #create iteneraries list
    itineraries = []
    print("Enter flight itineraries (type 'done' to finish):")
    
    #While statement to enter multiple flight information
    while True:
        traveler_name = input("Enter traveler's name (or 'done' to finish): ")
        #Break statement
        if traveler_name.lower() == 'done':
            break
        origin = input("Enter origin city: ")
        destination = input("Enter destination city: ")
        #add all of the previous information to the itineraries list
        itineraries.append((traveler_name, origin, destination))
    
    #use return so we can manipulate it later
    return itineraries

def format_flight_itineraries(itineraries):
    #format the itineraries to display in the order I want
    #new formatted string list
    formatted = []
    #iterate through the information in itineraries
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted.append(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")
    return "\n".join(formatted)

# Main program
itineraries = get_user_itineraries()
if itineraries:
    result = format_flight_itineraries(itineraries)
    print("\nFormatted Itineraries:\n")
    print(result)
else:
    print("No itineraries entered.")
