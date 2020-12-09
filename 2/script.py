def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def main():
    lines = read_input()

    correct_count = 0 
    correct_count_2 = 0 
    for line in lines:
        [range, letter, password] = line.split()
        
        [lower, upper] = range.split('-')
        letter = letter[0]
        
        # part 1
        letter_count = {}
        for c in password:
            if c not in letter_count:
                letter_count[c] = 0
            
            letter_count[c] = letter_count[c] + 1

        if letter in letter_count and letter_count[letter] >= int(lower) and letter_count[letter] <= int(upper):
            correct_count += 1
    
        # part 2

        first_match = int(lower) <= len(password) and password[int(lower) - 1] == letter
        second_match = int(upper) <= len(password) and password[int(upper) - 1] == letter

        match_count = 1 if first_match else 0
        match_count += 1 if second_match else 0

        if match_count == 1:
            correct_count_2 += 1


    print(correct_count)
    print(correct_count_2)
    


if __name__ == "__main__":
    main()