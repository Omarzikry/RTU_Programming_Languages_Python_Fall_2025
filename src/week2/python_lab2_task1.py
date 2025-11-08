"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Dataset definitions
temperatures = [67, 70, 68, 65, 72, 74, 69]
city_population = {
    "Riga": 613486,
    "Daugavpils": 80269,
    "Liepaja": 68262,
    "Jelgava": 55572,
    "Ventspils": 33432,
}

# Aggregate computations
average_temperature = sum(temperatures) / len(temperatures)
largest_city, largest_population = max(city_population.items(), key=lambda item: item[1])
smallest_city, smallest_population = min(city_population.items(), key=lambda item: item[1])
total_population = sum(city_population.values())

# Formatted output
print(f"Average temperature: {average_temperature:.1f} degrees")
print(f"Largest city by population: {largest_city} ({largest_population:,})")
print(f"Smallest city by population: {smallest_city} ({smallest_population:,})")
print(f"Total population: {total_population:,}")
