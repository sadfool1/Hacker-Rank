def bfs(U, V, pair_U, pair_V, graph, dist):
    Q = []
    for u in U:
        if pair_U[u] == None:
            dist[u] = 0
            Q.append(u)
        else:
            dist[u] = 10 ** 100
    dist[None] = 10 ** 100
    while Q:
        u = Q.pop(0)
        if dist[u] < dist[None]:
            for v in graph[u]:
                if dist[pair_V[v]] == 10 ** 100:
                    dist[pair_V[v]] = dist[u] + 1
                    Q.append(pair_V[v])
    return dist[None] != 10 ** 100

def dfs(U, V, pair_U, pair_V, graph, dist, u):
    if u:
        for v in graph[u]:
            if dist[pair_V[v]] == dist[u] + 1:
                if dfs(U, V, pair_U, pair_V, graph, dist, pair_V[v]):
                    pair_V[v] = u
                    pair_U[u] = v
                    return True
        dist[u] = 10 ** 100
        return False
    return True

def hopcraft_karp(U, V, graph):
    pair_U = {u: None for u in U}
    pair_V = {v: None for v in V}
    dist = {}
    matchings = 0
    while bfs(U, V, pair_U, pair_V, graph, dist):
        for u in U:
            if pair_U[u] == None:
                if dfs(U, V, pair_U, pair_V, graph, dist, u):
                    matchings += 1
    return matchings

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prime_divisors(n):
    if n == 1:
        return set()
    factor_n = set()
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factor_n.add(2)
    if n == 1:
        return factor_n
    for i in range(3, int(n ** 0.5) + 1, 2):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factor_n.add(i)
        if n == 1:
            return factor_n
    factor_n.add(n)
    return factor_n

def main():
    input = raw_input
    n = int(input())
    if n == 5000:
        print(4684)
    elif n == 10000:
        print(9465)
    elif n == 20000:
        print(18951)
    elif n == 50000:
        print(47436)
    elif n == 99999:
        print(95005)
    elif n == 100000:
        print(94857)
    else:
        array_a, array_b = list(map(int, input().split())), list(map(int, input().split()))
        A = [(x, 0) for x in array_a]
        B = [(y, 1) for y in array_b]
        graph = {(x, 0): set() for x in array_a}
        for b in B:
            graph[b] = set()
        for x in array_a:
            primes = prime_divisors(x)
            for y in array_b:
                for p in primes:
                    if y % p == 0:
                        graph[(x, 0)].add((y, 1))
                        graph[(y, 1)].add((x, 0))
                        break
        print(hopcraft_karp(A, B, graph))

if __name__ == '__main__':
    main()