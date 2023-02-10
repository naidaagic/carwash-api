"""
    Having an array of integers, such as: [3,1,2,5,1,2] and an array of equal size consisted of
    zeros [0,0,0,0,0,0] calculate how many operations will be required to match the arrays,
    given that you can increment any sub array by one (consecutive elements, for example,
    you can increment the first, second and third element but cannot increment the first
    element, skip the second and increment the third).

    Example:
    [3,1,2,5,1,2], [0,0,0,0,0,0]
    [3,1,2,5,1,2], [1,1,1,1,1,1] // First iteration
    [3,1,2,5,1,2], [1,1,2,2,1,1] // Second iteration
    [3,1,2,5,1,2], [1,1,2,3,1,1] // Third iteration
    [3,1,2,5,1,2], [1,1,2,4,1,1] // Fourth iteration
    [3,1,2,5,1,2], [1,1,2,5,1,1] // Fifth iteration
    [3,1,2,5,1,2], [2,1,2,5,1,1] // Sixth iteration
    [3,1,2,5,1,2], [3,1,2,5,1,1] // Seventh iteration
    [3,1,2,5,1,2], [3,1,2,5,1,2] // Eighth iteration
"""

if __name__ == "__main__":
    starting_array = [3, 1, 2, 5, 1, 2]

    final_num_operations = starting_array[0]
    shared_operations = starting_array[0]

    for i in range(1, len(starting_array)):
        if starting_array[i] <= shared_operations:
            shared_operations = starting_array[i]
        else:
            final_num_operations += starting_array[i] - shared_operations
            shared_operations = starting_array[i]

    print(final_num_operations)

