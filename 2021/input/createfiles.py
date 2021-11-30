days = range(1,26)
parts = ["1","2"]

for day in days:
    for part in parts:
        print(day)
        two_digit_day = f"{day:02}"

        try:
            f = open(f"input{two_digit_day}-{part}", "x")
            f.close()
        except:
            pass
