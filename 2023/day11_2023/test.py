with open("test.txt", "r") as file:
    galaxy_map = [list(line) for line in file.read().splitlines()]

galaxies = [(row, col) for row, line in enumerate(galaxy_map)
            for col, char in enumerate(line) if char == '#']

# print(galaxies)
for row in range(3,7):
    print(row)