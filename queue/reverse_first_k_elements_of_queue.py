def reverse_queue(queue, k):
    """
    Reverse the first k elements of the queue.
    
    :param queue: The input queue (list).
    :param k: The number of elements to reverse.
    :return: The modified queue with the first k elements reversed.
    """
    if k <= 0 or k > len(queue):
        return queue

    # Step 1: Dequeue the first k elements
    stack = []
    for _ in range(k):
        stack.append(queue.pop(0))

    # Step 2: Enqueue the elements back in reverse order
    while stack:
        queue.append(stack.pop())

    # Step 3: Move the remaining elements to the back of the queue
    for _ in range(len(queue) - k):
        queue.append(queue.pop(0))

    return queue


if __name__ == "__main__":
    # Example usage
    queue = [1, 2, 3, 4, 5]
    k = 3
    print("Original queue:", queue)
    modified_queue = reverse_queue(queue, k)
    print("Modified queue after reversing first", k, "elements:", modified_queue)