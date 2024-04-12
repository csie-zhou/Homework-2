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
    queue = deque([(start_token, [start_token], initial_balance, liquidity)])

    # Define max_length as per requirements
    max_length = 7  # Example max length
    i = 0
    while queue:
        token, path, balance,  current_liquidity = queue.popleft()
        for neighbor_token in current_liquidity.keys():
            if token in neighbor_token:
                a, b = current_liquidity[neighbor_token]
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
                new_balance = gamma * current_balance * buy_amount / \
                    (sell_amount + gamma * current_balance)

                if new_balance < 0:
                    continue  # Skip if balance is negative after the exchange

                # Update liquidity pool
                sell_amount = sell_amount + current_balance
                buy_amount = buy_amount - new_balance
                new_liquidity = {}
                # Iterate over the existing liquidity data and assign it to the new variable
                for pair, values in liquidity.items():
                    # Extract tokens from the pair
                    token1, token2 = pair
                    # Swap token order and values for the new liquidity dictionary
                    new_pair = (token2, token1)
                    new_values = values[::-1]
                    # Assign the values to the new dictionary
                    new_liquidity[new_pair] = new_values

                if neighbor == neighbor_token[0]:
                    new_liquidity[neighbor_token] = (
                        buy_amount, sell_amount)
                else:
                    new_liquidity[neighbor_token] = (
                        sell_amount, buy_amount)

                new_path = path + [neighbor]
                if neighbor == start_token and new_balance > 20:

                    final_path = new_path
                    final_balance = new_balance
                    liquidity = new_liquidity

                    path_str = "->".join(final_path)
                    print(
                        f"path: {path_str}, {start_token} balance={final_balance:.6f}")
                    return final_path
                # if neighbor not in path and len(new_path) <= max_length:
                if len(new_path) <= max_length:
                    queue.append(
                        (neighbor, new_path, new_balance, new_liquidity))

    print("No path found within max length or balance condition.")
    return None


edges = {
    ("tokenA", "tokenB"),
    ("tokenA", "tokenC"),
    ("tokenA", "tokenD"),
    ("tokenA", "tokenE"),
    ("tokenB", "tokenC"),
    ("tokenB", "tokenD"),
    ("tokenB", "tokenE"),
    ("tokenC", "tokenD"),
    ("tokenC", "tokenE"),
    ("tokenD", "tokenE"),

    ("tokenB", "tokenA"),
    ("tokenC", "tokenA"),
    ("tokenD", "tokenA"),
    ("tokenE", "tokenA"),
    ("tokenC", "tokenB"),
    ("tokenD", "tokenB"),
    ("tokenE", "tokenB"),
    ("tokenD", "tokenC"),
    ("tokenE", "tokenC"),
    ("tokenE", "tokenD"),
}


def bonus(liquidity, start_token, initial_balance):
    max_profit = 0
    # Initialize a queue for BFS
    visited = {node: False for node in edges}
    queue = deque(
        [(start_token, [start_token], initial_balance, liquidity, visited)])

    # Define max_length as per requirements
    max_length = 13  # Example max length
    i = 0
    while queue:
        token, path, balance,  current_liquidity, current_visited = queue.popleft()
        for neighbor_token in current_liquidity.keys():
            if token in neighbor_token:
                a, b = current_liquidity[neighbor_token]
                if neighbor_token[1] == token:
                    neighbor = neighbor_token[0]
                    sell_amount = b
                    buy_amount = a
                else:
                    neighbor = neighbor_token[1]
                    sell_amount = a
                    buy_amount = b

                ############################
                # Visited check
                if current_visited[(token, neighbor)]:
                    continue
                new_visited = {}
                # Iterate over the existing liquidity data and assign it to the new variable
                for token1, token2 in edges:
                    # Swap token order and values for the new liquidity dictionary
                    pair = (token2, token1)

                    # Assign the values to the new dictionary
                    new_visited[pair] = current_visited[pair]
                new_visited[(token, neighbor)] = True
                ###########################

                # Calculate the new balance after exchanging tokens
                current_balance = balance
                new_balance = gamma * current_balance * buy_amount / \
                    (sell_amount + gamma * current_balance)

                if new_balance < 0:
                    continue  # Skip if balance is negative after the exchange

                # Update liquidity pool
                sell_amount = sell_amount + current_balance
                buy_amount = buy_amount - new_balance
                new_liquidity = {}
                # Iterate over the existing liquidity data and assign it to the new variable
                for pair, values in liquidity.items():
                    # Extract tokens from the pair
                    token1, token2 = pair
                    # Swap token order and values for the new liquidity dictionary
                    new_pair = (token2, token1)
                    new_values = values[::-1]
                    # Assign the values to the new dictionary
                    new_liquidity[new_pair] = new_values

                if neighbor == neighbor_token[0]:
                    new_liquidity[neighbor_token] = (
                        buy_amount, sell_amount)
                else:
                    new_liquidity[neighbor_token] = (
                        sell_amount, buy_amount)

                new_path = path + [neighbor]
                if neighbor == start_token and new_balance > max_profit:
                    max_profit = new_balance
                    final_path = new_path
                    final_balance = new_balance
                    final_liquidity = new_liquidity
                    final_visited = new_visited

                    # path_str = "->".join(final_path)
                    # print(
                    #     f"Bonus: path: {path_str}, {start_token} balance={final_balance:.6f}")
                    # return final_path
                # if neighbor not in path and len(new_path) <= max_length:
                if len(new_path) <= max_length:
                    queue.append(
                        (neighbor, new_path, new_balance, new_liquidity, new_visited))

    path_str = "->".join(final_path)
    print(
        f"Bonus: path: {path_str}, {start_token} balance={final_balance:.6f}")
    print("No path found within max length or balance condition.")
    return None


# Call the BFS function with the liquidity data, starting token, and initial balance
# bfs_liquidity(liquidity, start_token, initial_balance)

bonus(liquidity, start_token, initial_balance)
