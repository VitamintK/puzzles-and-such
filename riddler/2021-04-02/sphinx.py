from collections import defaultdict
from functools import lru_cache

tracker = defaultdict(int)
def dfs(n, q, h, ls):
    if h == 0:
        to_return = 1
    elif ls == q-1:
        to_return = 2 * dfs(n,q,h-1,1)
    else:
        m1 = dfs(n,q,h-1,1)
        m2 = dfs(n,q,h-1,ls+1)
        to_return =  (2 * m1 * m2)/(m1 + m2)
    # print(h, ls, rs, ':', to_return)
    tracker[(h, ls)] += 1
    return to_return
@lru_cache(maxsize=None)
def F(n,q):
    if n < q:
        return 1
    else:
        ans = 2 * F(n-q+1, q)
        for i in reversed(range(1,q-1)):
            ans = 2 * F(n-i, q) * ans / (F(n-i,q) + ans)
        return ans

@lru_cache(maxsize=None)
def n_nacci(n,i):
    if i < n-1:
        return 0
    elif i == n-1:
        return 1
    else:
        ans = 0
        for j in range(n):
            ans += n_nacci(n,i-1-j)
        return ans

def get_ans(n,q):
    return pow(2,n-1)/n_nacci(q-1,n+q-2)

if __name__ == '__main__':
    N,Q = map(int, input("enter n and q: ").split())
    ans = dfs(N,Q, N, 0)
    for k,v in sorted(tracker.items()):
        print(f'{k}: {v}')
    print(ans)
    c = 2
    print(F(N,Q))
    print(get_ans(N,Q))