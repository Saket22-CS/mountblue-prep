# Problem: Sales by Match
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / HashMap

# Time Complexity: O(n)
# Space Complexity: O(n)

def sockMerchant(n, ar):
    sock_count = {}
    pairs = 0

    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    for count in sock_count.values():
        pairs += count // 2

    return pairs


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)