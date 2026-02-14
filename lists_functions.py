# Calculate average, max, min from user input

def analyze_data(data):
    return sum(data)/len(data), max(data), min(data)

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]

avg, mx, mn = analyze_data(nums)

print("Average:", avg)
print("Max:", mx)
print("Min:", mn)
