def solution(A, F, M):
    current_sum = sum(A)
    total_sum = M * (len(A) + F)
    required_sum = total_sum - current_sum

    if required_sum > F * 6 or required_sum < F:
        return [0]

    result = [1] * F
    required_sum -= F

    for i in range(F):
        add = min(required_sum, 5)
        result[i] += add
        required_sum -= add

    return result

# Test
print(solution([3, 2, 4, 3], 2, 4))  # Returns [6, 6] 
print(solution([1, 2, 3, 4], 4, 6)) # return [0].

