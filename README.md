# car-builder

## Estimated time

45 minutes

## Level of difficulty

Medium

## Objectives

1. Improving the student's skills in operating with inheritance and composition

## Scenario

Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :
1. Define classes representing:
     - Tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
     - Engine; methods available: start(), stop(), get_state(); attribute available: fuel type
     - Vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
2. Based on the classes defined above, create the following objects:
     - Two sets of tires: city tires (size: 15), off-road tires (size: 18)
     - Two engines: electric engine, petrol engine
3. Instantiate two objects representing cars:
     - The first one is a city car, built of an electric engine and city tires
     - The second one is an all-terrain car build of a petrol engine and off-road tires

Play with the cars by calling methods responsible for interaction with components.
