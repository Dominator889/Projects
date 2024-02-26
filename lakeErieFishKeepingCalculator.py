"""
Name: Dominic
Date: 10/25/2023
Purpose: calculate whether you can keep a lake erie fish or not depending on size
"""
# Define the size limits and restrictions for each fish type
fish_limits = {
    "largemouthbass": 12,
    "smallmouthbass": 12,
    "spottedbass": 12,
    "bluecatfish": 35,
    "flatheadcatfish": 35,
    "channelcatfish": 28,
    "musky": 0,
    "muskellunge": 0,
    "stripedbass": 15,
    "hybridstripedbass": 15,
    "whitebass": 15,
    "trout": 0,
    "walleye": 0,
    "sauger": 0,
    "saugeye": 0,
    "yellowperch": 0
}
while True:
  # Ask for size
  fishSize = int(input("What is the size of the fish in inches: "))

  print(""" 
  Here's the list of fish:
    largemouthbass 
    smallmouthbass
    spottedbass
    bluecatfish
    flatheadcatfish
    channelcatfish
    musky
    muskellunge
    stripedbass
    hybridstripedbass
    whitebass
    trout 
    walleye
    sauger
    saugeye
    yellowperch
  """)

  # Ask for type of fish
  typeOfFish = input("(Input in all lowercase with no spaces) What type of fish is it: ")

  try:
    # Check if the fish size meets the limit for the given type
    if fishSize >= fish_limits[typeOfFish]:
        print("You can keep the fish, but only limited amounts may apply.")
    else:
        print("You can't keep this fish. The size must be at least", fish_limits[typeOfFish], "inches.")

  except KeyError:
    print("That is not a valid fish type")
    continue