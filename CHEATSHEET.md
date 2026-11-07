# C++ → Python cheat sheet

Built from mistakes I actually made. Newest additions at the bottom of each section.

## Input / output

| C++ | Python |
|---|---|
| `cin >> n` | `n = int(input())` |
| `cin >> a >> b` (one line) | `a, b = map(int, input().split())` |
| read array on one line | `arr = list(map(int, input().split()))` |
| `"push 5"` on one line | `parts = input().split()` → `parts[0]`, `int(parts[1])` |
| `cout << x << " "` | `print(x, end=" ")` |
| `cout << endl` | `print()` |
| print a sequence space-separated | `print(*p)` |

- `input()` reads a **whole line**. `split()` gives **strings**, so convert with `int()`.
- `print` has named arguments: `end` (default `"\n"`) and `sep` (default `" "`).

## Control flow

| C++ | Python |
|---|---|
| `while (t--)` | `for _ in range(t):` (or `t -= 1`; there is no `--`) |
| `x++` / `mp[s]++` | `x += 1` / `mp[s] += 1` (no `++` either) |
| `for (int x : arr)` | `for x in arr:` |
| `else if` | `elif` |
| `c ? a : b` | `a if c else b` |
| `{ }` | indentation; check which loop a line belongs to |

- Declare per-test-case containers **inside** the test loop.
- `return` only works inside a `def`. Top-level code uses `print`.

## Stack / queue

| C++ | Python |
|---|---|
| `stack` / `vector` as stack | `list` |
| `push` / `push_back` | `append(x)` |
| `top()` / `back()` | `lst[-1]` |
| `pop()` / `pop_back()` | `lst.pop()`, which also **returns** the element |
| `empty()` | `not lst` |
| `queue` / `deque` | `collections.deque`, never `list.pop(0)` (O(n)) |

- `s2.append(s1.pop())` moves the top of s1 onto s2.
- `lst[-1]` / `lst.pop()` on an empty list → `IndexError`.

## Priority queue (heapq)

| C++ `priority_queue<int> pq` (max) | Python `pq = []` + `import heapq` |
|---|---|
| `pq.push(x)` | `heapq.heappush(pq, -x)` |
| `pq.top()` | `-pq[0]` |
| `pq.pop()` | `heapq.heappop(pq)`, which also **returns** the (negated) value |
| `pq.empty()` / `size()` | `not pq` / `len(pq)` |

- `heapq` is **min-heap only**. For a max-heap, negate on push and negate again on read.
- No heap object: the functions take the list, `heappop(pq)`, not `heappop()`.
- Pairs: `heappush(pq, (-score, name))` negates only the sort key.
- `pq[0]` / `heappop` on an empty heap crash. Guard with `if pq:`.
- Skip `queue.PriorityQueue` (thread-safe, slower).

## dict / defaultdict / set

| C++ | Python |
|---|---|
| `unordered_map` | `dict` (`{}`) |
| `mp.count(k)` | `k in mp` |
| `mp.erase(k)` | `del mp[k]` or `mp.pop(k, None)` (safe) |
| `for (auto& [k, v] : mp)` | `for k, v in mp.items():` |
| `map` where `mp[k]++` creates k | `defaultdict(int)` |
| `unordered_set` | `set()` (`{}` is an empty **dict**) |
| `s.erase(x)` | `s.discard(x)` (safe) / `s.remove(x)` (crashes if missing) |

- Plain dict: `mp[k] += 1` on a missing key → `KeyError`. Use `mp.get(k, 0)` or `defaultdict(int)`.
- `defaultdict(int)` passes the **function** `int`, which is called for each missing key (`int()` = 0, `list()` = []).
- With defaultdict, just **reading** `mp[k]` inserts k. Use `k in mp` to check without inserting.
- Looping over a dict gives **keys**. Use `.items()` for pairs.
- `from collections import ...`, lowercase.

## Sorted containers (the big gap)

- `dict` / `set` are **not sorted**. A dict keeps insertion order.
- `sorted(mp)` gives sorted keys. `sorted(mp.items())` gives pairs sorted by key. `sorted(mp.items(), key=lambda kv: kv[1])` sorts by value.
- No `std::set` / `map` / `multiset`. `sortedcontainers` is third-party and **not available on my OA platform**.
- Standard-library workaround: a sorted list + `bisect_left` (lower_bound) / `bisect.insort`. O(n) insert, fast up to ~1e5.
- Only need min/max with deletions → `heapq` + lazy deletion.
- Heavy ordered-set work on an OA → C++.

## itertools

- No `next_permutation`. `itertools.permutations(a)` yields **tuples**, follows input **positions** (sort first), and repeats duplicates.
- `permutations(a, r)` gives nPr, `combinations(a, r)` gives nCr, and `product(a, repeat=k)` replaces nested loops.

## Performance

- Python is ~10-100x slower per operation in your own loops. Built-ins (`sort`, `sum`, `Counter`, `max`) run in C.
- About 1e8 simple operations: C++ is fine, Python risks TLE.
