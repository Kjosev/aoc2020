def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    return lines


def validate(current_password):
    valid = 1
    for field in ["ecl", "pid","eyr", "hcl","byr","iyr", "hgt"]:
        if field not in current_password.keys():
            # # print("missing {}".format(field))
            return 0
    
    return valid


def validate2(current_password):
    valid = 1
    
    if "byr" in current_password.keys():
        try:
            parsed = int(current_password["byr"])
            valid = 1 if parsed >= 1920 and parsed <= 2002 and len(current_password["byr"]) == 4 else 0
            if valid == 0: return 0
        except:
            # print("invalid byr")
            return 0
    else:
        return 0

    if "iyr" in current_password.keys():
        try:
            parsed = int(current_password["iyr"])
            valid = 1 if parsed >= 2010 and parsed <= 2020 and len(current_password["iyr"]) == 4 else 0
            if valid == 0: return 0
        except:
            # print("invalid iyr")

            return 0
    else:
        return 0
    
    if "eyr" in current_password.keys():
        try:
            parsed = int(current_password["eyr"])
            valid = 1 if parsed >= 2020 and parsed <= 2030 and len(current_password["eyr"]) == 4 else 0
            if valid == 0: return 0

        except:
            # print("invalid eyr")

            return 0
    else:
        return 0

    if "hgt" in current_password.keys():
        try:
            parsed = int(current_password["hgt"][:-2])
            # print(parsed)
            measure = current_password["hgt"][-2:]
            # print(measure)
            if measure == 'cm':
                valid = 1 if parsed >= 150 and parsed <= 193 else 0
            elif measure == "in":
                valid = 1 if parsed >= 59 and parsed <= 76 else 0
            else:
                # print("invalid hgt")
                return 0

            if valid == 0: return 0
            
        except:
            # print("invalid hgt")
            return 0
    else:
        # print("invalid hgt")
        return 0

    if "hcl" in current_password.keys():
        # print(current_password['hcl'])
        if len(current_password['hcl']) != 7:
            # print("invalid hcl")
            return 0

        if current_password['hcl'][0] != "#":
            # print("invalid hcl")
            return 0

        for letter in current_password['hcl'][1:]:
            if letter not in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                ]:
                # print("invalid hcl")
            

                return 0
    else:
        # print("invalid hcl")

        return 0

    if "ecl" in current_password.keys():
        if current_password["ecl"] not in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]:
            # print("invalid ecl")

            return 0
    else:
        return 0

    if "pid" in current_password.keys():
        if len(current_password["pid"]) != 9:
            # print("invalid pid")
            
            return 0

        for letter in current_password["pid"]:
            if letter not in [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]:
                # print("invalid pid")
            
                return 0
    else:
        # print("invalid pid")

        return 0
        
    # print('final {}'.format(valid))
    return valid


def main():
    lines = read_input()
    
    count_valid = 0
    count_valid_2 = 0
    current_password = {}

    for line in lines:
        if (len(line.strip()) == 0):
            count_valid += validate(current_password)
            count_valid_2 += validate2(current_password)
            if count_valid_2 == 1: print(current_password)
            # # print(current_password)
            current_password = {}
        else:
            parts = line.split()
            for part in parts:
                [key, value] = part.split(":")
                current_password[key] = value


    count_valid += validate(current_password)
    count_valid_2 += validate2(current_password)


    print(count_valid)
    print(count_valid_2)



if __name__ == "__main__":
    main()