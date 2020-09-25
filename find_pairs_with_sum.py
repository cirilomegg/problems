# Given an array and a sum, find all pairs that add up to the sum.
# Time complexity: O(n)

def find_pairs(arr, sum):
    dict = {}
    pairs = []

    for i, n in enumerate(arr):
        if sum - n in dict:
            pairs.append((dict.get(sum - n), i))

        dict[n] = i

    return pairs


if __name__ == "__main__":
    print(find_pairs([1, 5, 3, 8, 3, 2, 9, 7], 10))
    print(find_pairs([1, 5, 3, 8, 3, 2, 9, 7], 6))
    print(find_pairs([1, 5, 3, 8, 3, 2, 9, 7], 100))
    print(find_pairs([1], 10))
    print(find_pairs([], 100))
