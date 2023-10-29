# Ask for user's input (string)
# Calculate tip and take 2 decimals
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Convert strings into float
# Remove $
def dollars_to_float(d):
    dol = d.replace("$", "")
    dol = float (dol)
    return (dol)

# Convert strings into float
# Remove %
# Transform float value into real percentage value
def percent_to_float(p):
    per = p.replace("%", "")
    per = (float (per) / 100)
    return (per)

main()