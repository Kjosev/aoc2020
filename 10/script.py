def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def main():
    nums = [int(x) for x in read_input()]

    nums = sorted(nums)
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)

    diffs = []

    for idx in range(len(nums) - 1):
        diffs.append(nums[idx + 1] - nums[idx])

    diff_3 = [x for x in diffs if x == 3]
    diff_1 = [x for x in diffs if x == 1]
    print(len(diff_1) * len(diff_3)) 

    dp = [0 for n in nums]

    for idx in range(len(dp)):
        if idx == 0:
            dp[idx] = 1
            continue

        backwards_iter = idx - 1
        while backwards_iter >= 0 and nums[backwards_iter] + 3 >= nums[idx]:
            dp[idx] += dp[backwards_iter]
            backwards_iter -= 1
        
    print(dp[-1])
        

if __name__ == "__main__":
    main()