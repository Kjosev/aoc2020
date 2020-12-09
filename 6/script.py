def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def parse_groups(lines):
    groups = [[]]

    for line in lines:
        is_new_line = len(line.strip()) == 0

        if not is_new_line:
            groups[-1].append(line)
        else:
            groups.append([])
    
    return groups


def get_counts(groups):
    parsed_groups = []
    for group in groups:
        current_parsed_group = {
            "responses": group,
            "counts": {}
        }

        for response in group:
            for letter in response:
                current_count = current_parsed_group["counts"].get(letter, 0)
                current_parsed_group["counts"][letter] = current_count + 1
        
        parsed_groups.append(current_parsed_group)
    
    return parsed_groups


def get_count_unanymous_answers(groups):
    for group in groups:
        group["count_unanymous_answers"] = 0
        for letter, count in group["counts"].items():
            if count == len(group["responses"]):
                current_count = group["count_unanymous_answers"]
                group["count_unanymous_answers"] = current_count + 1
    
    return groups


def main():
    lines = read_input()

    groups = parse_groups(lines)  # returns [["abc", "ab"], ["abcd"]]
    # print("Groups: {}".format(groups))
    group_counts = get_counts(groups)  # return [{"responses": groups[0], "counts", {"a": 2, "b": 2, "c": 1}}, ...]
    # print("Group counts: {}".format(group_counts))
    result = sum([len(group["counts"]) for group in group_counts])

    print("Sum is {}".format(result))

    get_count_unanymous_answers(group_counts)

    result_2 = sum(group["count_unanymous_answers"] for group in group_counts)

    print("Sum 2 is: {}".format(result_2))

if __name__ == "__main__":
    main()