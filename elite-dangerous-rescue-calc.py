def find_closest_numbers(numbers):
    target = 126
    numbers.sort()
    closest_sum = float('inf')
    closest_numbers = []

    for i in range(len(numbers)):
        left = i + 1
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]

            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                closest_numbers = [numbers[i], numbers[left], numbers[right]]

            if current_sum == target:
                return closest_numbers

            elif current_sum < target:
                left += 1

            else:
                right -= 1

    return closest_numbers

input_numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
closest_numbers = find_closest_numbers(input_numbers)

print("The closest numbers that add up to 126 are:", closest_numbers)
