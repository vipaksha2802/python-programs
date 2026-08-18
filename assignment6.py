
def knapsack_bottom_up(values, weights, W):
    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Top-Down Approach using Memoization
def knapsack_top_down(values, weights, W):
    n = len(values)

    # Memoization table
    dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def solve(i, w):

        # Base case
        if i == 0 or w == 0:
            return 0

        # Return already calculated result
        if dp[i][w] != -1:
            return dp[i][w]

        # If current item can be included
        if weights[i - 1] <= w:
            dp[i][w] = max(
                solve(i - 1, w),
                values[i - 1] + solve(i - 1, w - weights[i - 1])
            )

        # If current item cannot be included
        else:
            dp[i][w] = solve(i - 1, w)

        return dp[i][w]

    return solve(n, W)


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Bottom-Up Approach:")
print("Maximum value =", knapsack_bottom_up(values, weights, W))

print("\nTop-Down Approach:")
print("Maximum value =", knapsack_top_down(values, weights, W))