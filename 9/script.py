def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def check_sum(arr, num):
    # print(arr)
    # print(num)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == num:
                return True
    
    return False


def find_wrong_num(numbers, preamble_lenght):
    current_idx = preamble_lenght

    while current_idx < len(numbers):
        if not check_sum(numbers[current_idx-preamble_lenght:current_idx], numbers[current_idx]):
            print("Wrong number: {} at {}".format(numbers[current_idx], current_idx))
            return numbers[current_idx]
        
        current_idx += 1


def find_weakness(numbers, wrong_number):

    forward_sum = [0 for n in numbers]

    for idx in range(len(numbers)):
        previous_sum = forward_sum[idx - 1] if idx > 0 else 0
        forward_sum[idx] = numbers[idx] + previous_sum

    for i in range(len(numbers)):
        for j in range(i + 1, (len(numbers))):
            current_sum = forward_sum[j]
            previous_sum = forward_sum[i - 1] if i > 0 else 0

            # print("{} to {}: {} sum to {}".format(i, j, str(numbers[i:j+1]), current_sum - previous_sum))
            if  current_sum - previous_sum == wrong_number:
                print(numbers[i:j+1])
                print("Result {}".format(max(numbers[i:j+1]) + min(numbers[i:j+1])))
                break





def main():
    lines = read_input()

    numbers = [int(x) for x in lines]

    preamble_lenght = 25

    wrong_number = find_wrong_num(numbers, preamble_lenght)

    find_weakness(numbers, wrong_number)

    



if __name__ == "__main__":
    main()
