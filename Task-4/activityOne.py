
def get_ranking(*grades):
    average = sum(grades) / len(grades)
    if average > 100 or average < 50:
        return "Invalid Grade"

    grade_boundaries = [
        {"lower": 98, "upper": 100, "rank": "With Highest Honors"},
        {"lower": 95, "upper": 97, "rank": "With High Honors"},
        {"lower": 90, "upper": 94, "rank": "With Honors"},
        {"lower": 75, "upper": 89, "rank": "Passed"},
        {"lower": 51, "upper": 74, "rank": "Failed"},
    ]

    for boundary in grade_boundaries:
        if average >= boundary["lower"] and average <= boundary["upper"]:
            return boundary["rank"]

    return "Invalid Grade"

if __name__ == '__main__':
    number_of_entries = 3
    try: 
        grades = [float(input(f"Enter Grade {i + 1}: ")) for i in range (number_of_entries)]
        print(get_ranking(*grades))
    
    except ValueError: 
        print("Must be a number.")
