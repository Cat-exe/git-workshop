

# List of oceanic vs. continental plate speeds
oceanic = [7.87, 7.74, 6.11, 7.69, 4.16, 4.0]
continental = [1.71, 4.34, 2.00, 3.35, 1.96, 2.14]

print("Oceanic plates move faster than continental plates.")


# Find the averages
oceanic_avg = sum(oceanic)/len(oceanic)
continental_avg = sum(continental)/len(continental)


plt.bar(['oceanic','continental'],[oceanic_avg,continental_avg])
plt.xlabel('type')
plt.ylabel('average')
plt.title("Comparing Plates' Average Speeds")

plt.show()

