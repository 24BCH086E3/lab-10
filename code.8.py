with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        filtered = [word for word in words if word.lower() not in ('a', 'an', 'the')]
        outfile.write(' '.join(filtered) + "\n")
print("Filtered file written to output.txt")
