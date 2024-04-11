
def transaction(queue, i):
    current_token, current_balance = queue.pop(0)
    next_token, (sell_amount, buy_amount) = list(liquidity.items())[i]
    fee = 0.003
    gamma = 1 - fee
    if current_token == next_token[0]:
        alpha = current_balance/sell_amount  # check amount
        reward = gamma*current_balance / \
            (sell_amount+gamma*current_balance)*buy_amount

        # Modify new value pairs to the pool
        sell_amount += current_balance
        buy_amount -= reward
        new_value_pair = (sell_amount, buy_amount)
        liquidity[next_token] = new_value_pair

        start_token = next_token[1]
        queue.append((start_token, reward))
    else:
        alpha = current_balance/buy_amount  # check amount
        reward = gamma*current_balance / \
            (buy_amount+gamma*current_balance)*sell_amount

        # Modify new value pairs to the pool
        buy_amount += current_balance
        sell_amount -= reward
        new_value_pair = (buy_amount, sell_amount)
        liquidity[next_token] = new_value_pair

        start_token = next_token[0]
        queue.append((start_token, reward))
    return start_token


def find_arbitrage_path(pairs, tokenIn, tokenOut, maxHops, currentPairs, path):
    # For loop: BFS node
    for i in range(len(pairs)):
        newPath = path.copy()
        pair = pairs[i]
        # Skip the pair that doesn't include curent tokens
        if not pair['token0']['address'] == tokenIn['address'] and not pair['token1']['address'] == tokenIn['address']:
            continue
        # Skip the pair that the token isn't enough to give
        if pair['reserve0']/pow(10, pair['token0']['decimal']) < 1 or pair['reserve1']/pow(10, pair['token1']['decimal']) < 1:
            continue

        # Set the next token
        if tokenIn['address'] == pair['token0']['address']:
            tempOut = pair['token1']
        else:
            tempOut = pair['token0']
        # Add the next token to the path
        newPath.append(tempOut)

        # If the next token meets the end token
        # Check if balance exceeds 20? return path, balance; kill this path
        if tempOut['address'] == tokenOut['address']:
            if (bal)
            c = {'route': currentPairs, 'path': newPath}
            circles.append(c)
        # Else if still got hops, recursive
        elif maxHops > 1 and len(pairs) > 1:
            pairsExcludingThisPair = pairs[:i] + pairs[i+1:]
            path = find_arbitrage_path(
                pairsExcludingThisPair, tempOut, tokenOut, maxHops-1, currentPairs + [pair], newPath)
    return path


def find_arbitrage_path(liquidity, maxHops, path, tokenIn, tokenOut, balance):
    queue = [(tokenIn, balance)]
    current_token, current_balance = queue.pop(0)

    # If balance >= 20, return path
    if current_token == tokenOut and current_balance >= 20:
        # best_balance = current_balance
        # best_path = [start_token]  # add the start to the end, and quit
        path.append(current_token)
        return path, current_balance
    elif current_token == tokenOut and maxHops == 0:
        print("Hops not enough")
        return

    # visited.add(current_token)

    # For loop: BFS node
    for token_pair, (sell_amount, buy_amount) in liquidity.items():
        # Skip the pair that doesn't include curent tokens
        if token_pair[0] != current_token and token_pair[1] != current_token:
            continue
        # Skip the pair that the token isn't enough to give #

        # token0 -> token1
        if tokenIn == token_pair[0]:
            path.append(token_pair[1])
            alpha = current_balance/sell_amount  # check amount
            reward = gamma*current_balance / \
                (sell_amount+gamma*current_balance)*buy_amount

            # Modify new value pairs to the pool
            sell_amount += current_balance
            buy_amount -= reward
            new_value_pair = (sell_amount, buy_amount)
            liquidity[token_pair] = new_value_pair

            find_arbitrage_path(liquidity, maxHops-1, path,
                                token_pair[1], tokenOut, current_balance)
            # tokenIn = token_pair[1]
            # queue.append((tokenIn, reward))

        # token0 <- token1
        else:
            path.append(token_pair[0])
            alpha = current_balance/buy_amount  # check amount
            reward = gamma*current_balance / \
                (buy_amount+gamma*current_balance)*sell_amount

            # Modify new value pairs to the pool
            buy_amount += current_balance
            sell_amount -= reward
            new_value_pair = (buy_amount, sell_amount)
            liquidity[token_pair] = new_value_pair

            tokenIn = token_pair[0]
            queue.append((tokenIn, reward))

        ###
        if token_pair[0] == current_token or token_pair[1] == current_token:
            pass


if final_balance >= 20:
    path_str = "->".join(new_path + [start_token])
    print(f"path: {path_str}, {start_token} balance={final_balance:.6f}")
    all_paths.append(new_path)
