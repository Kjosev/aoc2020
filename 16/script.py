import re

def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def check_rule(num, rule):
    return (
        (num >= rule['range1_start'] and num <= rule['range1_end']) or 
        (num >= rule['range2_start'] and num <= rule['range2_end'])
    )


def main():
    lines = read_input()
    
    my_ticket_idx = lines.index("your ticket:") + 1
    nearby_ticket_idx = lines.index("nearby tickets:") + 1

    rules = lines[:my_ticket_idx - 2]
    my_ticket = lines[my_ticket_idx]
    nearby_tickets = lines[nearby_ticket_idx:]

    parsed_rules = {}

    for rule in rules:
        m = re.match(r'([\w\s]+)\:\s+(\d+)\-(\d+)\s+or\s+(\d+)\-(\d+)', rule)
        rule_name, range1_start, range1_end, range2_start, range2_end = m.groups()

        parsed_rules[rule_name] = {
            "rule_name": rule_name, 
            "range1_start": int(range1_start),
            "range1_end": int(range1_end),
            "range2_start": int(range2_start),
            "range2_end": int(range2_end)
        }
    

    valid_nearby_tickets = []
    nearby_tickets = [[int(num) for num in ticket.split(',')] for ticket in nearby_tickets]
    my_ticket = [int(num) for num in my_ticket.split(',')]

    wrong_numbers = []

    for nearby_ticket in nearby_tickets:
        has_invalid_number = False
        for num in nearby_ticket:
            matches_rules = False
            for name, rule in parsed_rules.items():
                if check_rule(num, rule):
                    matches_rules = True
            
            if not matches_rules:
                wrong_numbers.append(num)
                has_invalid_number = True

        if not has_invalid_number:
            valid_nearby_tickets.append(nearby_ticket)

    # part 1 solution
    print(sum(wrong_numbers))
    
    num_fields = len(my_ticket)

    rule_matches = {rule_name: [] for rule_name in parsed_rules.keys()}

    for idx in range(num_fields):
        nums_to_check = [ticket[idx] for ticket in valid_nearby_tickets] + [my_ticket[idx]]
        for name, rule in parsed_rules.items():
            is_valid = True
            for num in nums_to_check:
                if not check_rule(num, rule):
                    is_valid = False
            
            if is_valid:
                rule_matches[name].append(idx)

    idx_matches = {idx: [] for idx in range(num_fields)}
    for name, idxs in rule_matches.items():
        for idx in idxs:
            idx_matches[idx].append(name)

    matched_rules = []

    while len(matched_rules) < num_fields:
        rule_to_resolve = None
        idx_to_resolve = None

        for rule, idxs in rule_matches.items():
            if len(idxs) == 1:
                rule_to_resolve = rule
                idx_to_resolve = idxs[0]
                break

        for idx, rules in idx_matches.items():
            if len(rules) == 1:
                rule_to_resolve = rules[0]
                idx_to_resolve = idx
                break

        matched_rules.append((rule_to_resolve, idx))
        del rule_matches[rule_to_resolve]
        del idx_matches[idx_to_resolve]

        for idx in idx_matches.keys():
            if rule_to_resolve in idx_matches[idx]:
                idx_matches[idx].remove(rule_to_resolve)

        for rule in rule_matches.keys():
            if idx_to_resolve in rule_matches[rule]:
                rule_matches[rule].remove(idx_to_resolve)


    departure_fields = [idx for (rule, idx) in matched_rules if rule.startswith('departure')]
    answer = 1
    for idx in departure_fields:
        answer *= my_ticket[idx]

    # part 2
    print(answer)

if __name__ == "__main__":
    main()