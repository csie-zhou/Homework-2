from collections import deque
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

fee = 0.003
gamma = 1 - fee
final_balance = 0

# Define the starting token and initial balance
start_token = "tokenB"
initial_balance = 5


def bfs_liquidity(liquidity, start_token, initial_balance):
    # Initialize a queue for BFS
    queue = deque([(start_token, [start_token], initial_balance)])

    # Define max_length as per requirements
    max_length = 7  # Example max length
    i = 0
    while queue:
        token, path, balance = queue.popleft()
        for neighbor_token in liquidity.keys():
            if token in neighbor_token:
                a, b = liquidity[neighbor_token]
                if neighbor_token[1] == token:
                    neighbor = neighbor_token[0]
                    sell_amount = b
                    buy_amount = a
                else:
                    neighbor = neighbor_token[1]
                    sell_amount = a
                    buy_amount = b

                # Calculate the new balance after exchanging tokens
                current_balance = balance
                new_balance = gamma * current_balance / \
                    (sell_amount + gamma * current_balance) * buy_amount

                if new_balance < 0:
                    continue  # Skip if balance is negative after the exchange

                # Update liquidity pool
                sell_amount = sell_amount + current_balance
                buy_amount = buy_amount - new_balance
                if neighbor == neighbor_token[0]:
                    liquidity[neighbor_token] = (buy_amount, sell_amount)
                else:
                    liquidity[neighbor_token] = (sell_amount, buy_amount)

                new_path = path + [neighbor]
                if neighbor == start_token and new_balance > 20:
                    # final_path = new_path + [neighbor]
                    final_path = new_path
                    final_balance = new_balance
                    # print("Path found:", '->'.join(final_path),
                    #       ", balance: ", final_balance)
                    path_str = "->".join(final_path)
                    print(
                        f"path: {path_str}, {start_token} balance={final_balance:.6f}")
                    return final_path
                # if neighbor not in path and len(new_path) <= max_length:
                if len(new_path) <= max_length:
                    queue.append((neighbor, new_path, new_balance))
                    # print(new_balance)

    print("No path found within max length or balance condition.")
    return None


# Call the BFS function with the liquidity data, starting token, and initial balance
final_path = bfs_liquidity(liquidity, start_token, initial_balance)

# def DFS(tokenIn, visited, path, tokenOut):
#     visited[tokenIn] = True
#     path.append(tokenIn)

#     if len(path) >= 10:
#         return path

#     if tokenIn == tokenOut and len(path) > 1:
#         return path

#     for token_pair, (sell_amount, buy_amount) in liquidity.items():
#         # Skip the pair that doesn't include curent tokens
#         if token_pair[0] != tokenIn and token_pair[1] != tokenIn:
#             continue
#         # token0 -> token1
#         if tokenIn == token_pair[0]:
#             i = token_pair[1]
#             if not visited[i]:
#                 newPath = DFS(i, visited.copy(), path.copy(), tokenOut)
#                 if newPath:
#                     return newPath
#         # token0 <- token1
#         else:
#             i = token_pair[0]
#             if not visited[i]:
#                 newPath = DFS(i, visited.copy(), path.copy(), tokenOut)
#                 if newPath:
#                     return newPath


# tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]


# def find_arbitrage_path(tokenIn, tokenOut):
#     visited = {i: False for i in tokens}
#     path = []
#     return DFS(tokenIn, visited, path, tokenOut)


# tokenIn = "tokenB"
# tokenOut = "tokenB"
# path = find_arbitrage_path(tokenIn="tokenB", tokenOut="tokenB")
# path_str = "->".join(path + [tokenOut])
# print(f"path: {path_str}, {tokenOut} balance={final_balance:.6f}")
