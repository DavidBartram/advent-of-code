days = range(1, 26)
parts = ["1", "2"]

for day in days:
    for part in parts:
        print(day)
        two_digit_day = f"{day:02}"

        try:
            f = open(f"day{two_digit_day}-{part}.py", "x")
            f.close()
        except:
            pass
