import csv

# Specify the CSV file name
csv_file = "C:/Users/Gurinder/Desktop/neuron from scratch/snacks.csv"

# Initialize empty lists to store the data
snacks_data = []
try:
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            snacks_data.append(row)
except FileNotFoundError:
    print(f"File '{csv_file}' not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Separate liked and disliked snacks
liked_snacks = [snack for snack in snacks_data if snack[3] == "Like"]
disliked_snacks = [snack for snack in snacks_data if snack[3] == "Dislike"]

# Extract spiciness and saltiness data and convert to float
liked_spiciness = [float(snack[1]) for snack in liked_snacks]
liked_saltiness = [float(snack[2]) for snack in liked_snacks]
disliked_spiciness = [float(snack[1]) for snack in disliked_snacks]
disliked_saltiness = [float(snack[2]) for snack in disliked_snacks]

# Calculate the mean of spiciness and saltiness for liked and disliked snacks
mean_liked_spiciness = sum(liked_spiciness) / len(liked_spiciness)
mean_liked_saltiness = sum(liked_saltiness) / len(liked_saltiness)
mean_disliked_spiciness = sum(disliked_spiciness) / len(disliked_spiciness)
mean_disliked_saltiness = sum(disliked_saltiness) / len(disliked_saltiness)

# Calculate the slope and intercept using manual calculations
numerator = sum((x - mean_liked_spiciness) * (y - mean_liked_saltiness) for x, y in zip(liked_spiciness, liked_saltiness))
denominator = sum((x - mean_liked_spiciness) ** 2 for x in liked_spiciness)
slope = numerator / denominator
intercept = mean_liked_saltiness - slope * mean_liked_spiciness
