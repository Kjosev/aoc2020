import re

def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def parse_expr(line):
    return re.findall('[\d.]+|[()*+]', line)


def evaluate_expr(expr):
    idx = 0
    result = 0
    curr_operator = '+'
    while idx < len(expr):
        curr_expr = expr[idx]
        
        if curr_expr == '(':
            closing_idx = find_closing_bracket(expr, idx)
            expr_value = evaluate_expr(expr[idx + 1: closing_idx])
            result = eval("{} {} {}".format(result, curr_operator, expr_value))
            idx = closing_idx
        elif curr_expr.isnumeric():
            result = eval("{} {} {}".format(result, curr_operator, curr_expr))
        elif curr_expr in ['*', '+']:
            curr_operator = curr_expr
            
        idx += 1

    return result


def find_closing_bracket(expr, start_idx):
    bracket_count = 1

    for idx in range(start_idx + 1, len(expr)):
        if expr[idx] == '(':
            bracket_count += 1
        elif expr[idx] == ')':
            bracket_count -= 1
        
        if bracket_count == 0:
            return idx


def evaluate_expr_2(expr):
    result = 0
    expr = resolve_brackets(expr)
    result = apply_operators(expr, operator_order=['+', '*'])
    return result


def resolve_brackets(expr):
    resolved_expr = []

    idx = 0
    while idx < len(expr):
        if expr[idx] == '(':
            closing_idx = find_closing_bracket(expr, idx)
            resolved_expr.append(evaluate_expr_2(expr[idx + 1:closing_idx]))
            idx = closing_idx
        else:
            resolved_expr.append(expr[idx])
        idx += 1
    return resolved_expr


def apply_operators(expr, operator_order=None):
    if operator_order:
        for op in operator_order:
            idx = 1
            while idx < len(expr):
                if expr[idx] == op:
                    curr_result = eval("{} {} {}".format(expr[idx - 1], expr[idx], expr[idx + 1]))
                    expr = expr[:idx -1] + [curr_result] + expr[idx + 2:]
                else:
                    idx += 2
        else:
            idx = 1
            while idx < len(expr):
                curr_result = eval("{} {} {}".format(expr[idx - 1], expr[idx], expr[idx + 1]))
                expr = expr[:idx -1] + [curr_result] + expr[idx + 2:]



    return int(expr[0])


def main():
    lines = read_input()

    results = []
    results_2 = []
    for line in lines:
        expr = parse_expr(line)
        result = evaluate_expr(expr)
        result_2 = evaluate_expr_2(expr)

        results.append(result)
        results_2.append(result_2)

    print(sum(results))
    print(sum(results_2))

if __name__ == "__main__":
    main()