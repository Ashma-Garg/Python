def nonConstructibleChange(coins):
    # Write your code here.
	max_constructible = 0
    for a in sorted(coins):
        if a > max_constructible + 1:
            break
        max_constructible += a
    return max_constructible + 1
