# Function to perform Insertion Sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Get the list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
# Convert the string input to a list of integers
arr = list(map(int, user_input.split()))

# Print the unsorted list
print("Unsorted list:", arr)
# Sort the list using Insertion Sort
sorted_arr = insertion_sort(arr)
# Print the sorted list
print("Sorted list:", sorted_arr)
