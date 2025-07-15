def sort_stack(stack):
    # given a stack of integers, sort them in ascending or descending order

    temp_stack = []
    
    while stack:
        item = stack.pop()
        while temp_stack:
            if temp_stack[-1] > item:
                stack.append(temp_stack.pop())
    
        temp_stack.append(item)
    
    return temp_stack
        