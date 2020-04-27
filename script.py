destinations = ['Paris, France','Shanghai, China','Los Angeles, USA','São Paulo, Brazi','Cairo, Egypt']
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    return traveler_destination
traveler_destination_index = get_destination_index(get_traveler_location(test_traveler))
test_destination_index = get_traveler_location(test_traveler)
print(traveler_destination_index)