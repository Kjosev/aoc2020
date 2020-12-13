import re

def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def parse_bag_description(lines):
    bags = {}

    for line in lines:
        match = re.match(r"([\w\s]+)\sbags\scontain\s(.+)", line)

        (bag_color, contents) = match.groups()

        contents = contents[:-1]  # drop the . at the end

        content_parts = [part.strip() for part in contents.split(",")]

        child_bags = []

        for part in content_parts:
            if part == "no other bags":
                break
                
            content_match = re.match(r"(\d+)\s+([\w\s]+)\s+bags?", part)
            (child_bag_count, child_bag_color) = content_match.groups()

            child_bags.append(
                {
                    "color": child_bag_color,
                    "count": int(child_bag_count)
                }
            )
        
        bags[bag_color] = {
            "color": bag_color,
            "children": child_bags
        }
    
    for bag_color, bag in bags.items():
        if "parents" not in bag:
            bag["parents"] = []

        for child_bag_desc in bag['children']:
            child_bag = bags[child_bag_desc['color']]

            if "parents" not in child_bag:
                child_bag["parents"] = []
            
            child_bag["parents"].append(bag_color)


    return bags


def count_parents_of(color, bags):

    visited = set()
    visited.add(color)

    stack = []
    stack.append(color)

    while len(stack) > 0:
        current_color = stack.pop()
        current_bag = bags[current_color]

        for parent_color in current_bag["parents"]:
            if parent_color not in visited:
                visited.add(parent_color)
                stack.append(parent_color)

    return len(visited) - 1  # excluding the bag itself


MEMORY = {}


def count_child_bags_of(color, bags):
    current_bag = bags[color]

    if color in MEMORY:
        return MEMORY[color]

    if len(current_bag["children"]) == 0:
        MEMORY[color] = 0
        return MEMORY[color]
    else:
        child_bag_count = 0

        for child_bag in current_bag["children"]:
            child_bag_count += child_bag['count']
            child_bag_count += child_bag['count'] * count_child_bags_of(child_bag['color'], bags)

    MEMORY[color] = child_bag_count
    return MEMORY[color]


def main():

    lines = read_input()

    bags = parse_bag_description(lines)

    parent_count = count_parents_of("shiny gold", bags)


    print("Parents count: {}".format(parent_count))

    expected_answer = 126

    required_bag_count = count_child_bags_of("shiny gold", bags)

    print("Result: {} {}".format(required_bag_count, "PASS" if required_bag_count == expected_answer else "FAIL"))

if __name__ == "__main__":
    main()