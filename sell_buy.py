# Python Program to solve stock buy and sell 
# using one traversal

def maxProfit(prices):
    """
    Calculates the maximum possible profit from a list of stock prices by identifying
    the minimum price and subtracting it from the highest price encountered so
    far. It returns the maximum potential gain.

    Args:
        prices (List[int]): 1-indexed; it represents an array of non-negative
            integers where each integer is a stock price at a given time. It has
            at least one element.

    Returns:
        int: The maximum possible profit that can be achieved by buying and selling
        a stock once. The profit is calculated as the difference between the highest
        price and the lowest price encountered during the process.

    """
    minSoFar = prices[0]
    res = 0

    # Update the minimum value seen so far 
    # if we see smaller
    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])
        
        # Update result if we get more profit                
        res = max(res, prices[i] - minSoFar)
    
    return res

if __name__ == "__main__":
    prices = [7, 25, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))