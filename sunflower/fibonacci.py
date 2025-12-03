def fibonacci(rank):
    rank = int(rank)

    if rank < 0:
        raise ValueError("Fibonacci has a natural number domain.")
    if rank == 0:
        return 0

    prev, curr = 0, 1
    for _ in range(rank - 1):
        next = prev + curr
        prev = curr
        curr = next

    return curr
