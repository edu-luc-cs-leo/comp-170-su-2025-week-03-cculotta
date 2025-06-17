def draw_diamond(height: int):
    if height % 2 == 0:
        print("Please use an odd number for height.")
        return

    mid = height // 2

    for i in range(height):
        if i <= mid:
            # Top half and middle line
            spaces = mid - i
            hashes = 2 * i + 1
        else:
            # Bottom half
            spaces = i - mid
            hashes = 2 * (height - i - 1) + 1

        line = " " * spaces + "#" * hashes
        print(line)
draw_diamond(5)

def draw_right_triangle(height: int):
    for i in range(height):
        print("#" * (i + 1))
draw_right_triangle(5)
draw_right_triangle(3)
draw_right_triangle(7)

def compound_interest(principal: float, rate: float, years: int):
    year = 0
    while year < years:
        interest = principal * rate
        principal += interest
        year += 1
    print(f"Final amount after {years} years: ${principal:.2f}")
compound_interest(1000, 0.05, 5)

def draw_hollow_square(size: int, thickness: int):
    row = 0
    while row < size:
        if row < thickness or row >= size - thickness:
            # Top or bottom border rows
            print("#" * size)
        else:
            # Middle rows with hollow center
            middle_spaces = size - 2 * thickness
            print("#" * thickness + " " * middle_spaces + "#" * thickness)
        row += 1
draw_hollow_square(8, 2)
