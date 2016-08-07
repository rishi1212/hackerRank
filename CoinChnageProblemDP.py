CACHE = {}
def num_coins(target, coins):
    global CACHE

    if (target, tuple(coins)) in CACHE:
        return CACHE[(target, tuple(coins))]
    if target < 0:
        return 0
    elif target == 0:
        return 1
    else:
        result = 0
        for i in range(len(coins)):
            result += num_coins(target-coins[i], coins[i:])
        CACHE[(target, tuple(coins))] = result
        return result


N, C = (int(x) for x in input().split())
coins = [int(x) for x in input().split()]
print(num_coins(N, coins))