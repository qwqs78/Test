def backtracking(sequence, selected, start, n, m):
    if selected == m:
        print(' '.join(map(str, sequence)))
        return

    last_selected = None
    for i in range(start, n):
        if numbers[i] != last_selected:
            sequence.append(numbers[i])
            backtracking(sequence, selected + 1, i, n, m)
            sequence.pop()
            last_selected = numbers[i]

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 입력 수열 정렬
numbers.sort()

backtracking([], 0, 0, n, m)
