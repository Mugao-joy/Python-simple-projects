def casecounter(s):
    d = {"UPPER_CASE" : 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print(f"no of uppercase chars: {d['UPPER_CASE']}")
    print(f"no of lowercase chars: {d['LOWER_CASE']}")

casecounter('JOy mugaOJ')