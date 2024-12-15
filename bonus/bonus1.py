feet_inches = input("Enter the feet and inches")

def convert(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    metres = feet * 0.3048 + inches * 0.0254
    return metres

convert(feet_inches)

