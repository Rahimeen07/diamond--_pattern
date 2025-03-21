def draw_diamond(height):
    # Draw the upper pyramid
    for i in range(height):
        spaces = ' ' * (height - i - 1)  # Spaces before the stars
        stars = '*' * (2 * i + 1)        # Stars in the current row
        print(spaces + stars)             # Print the current row

    # Draw the inverted pyramid
    for i in range(height - 1):
        spaces = ' ' * (i + 1)           # Spaces before the stars
        stars = '*' * (2 * (height - i - 1) - 1)  # Stars in the current row
        print(spaces + stars)             # Print the current row

if __name__ == "__main__":
    try:
        height = int(input("Enter the height of the diamond: "))
        draw_diamond(height)
    except ValueError:
        print("Please enter a valid integer for the height.")