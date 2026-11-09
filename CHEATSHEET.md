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
- `map(f, lst)` applies `f` to every element (like `std::transform`). It's lazy: wrap it in `list()` to store the results.

### Fast I/O (use when input/output is ~1e5+ lines)

```python
import sys
input = sys.stdin.readline      # rebinds the name; no parentheses
out = []
...
out.append(ans)                 # collect inside the loop
print("\n".join(map(str, out))) # print once, after the loop
```

- Built-in `input()` flushes output before every read (`cin.tie` behaviour) and is built for interactive use. `readline` just reads from a buffer: it's `sync_with_stdio(0)` + `cin.tie(0)`.
- `print` writes to a buffer. A flush sends it out. A million small flushes is the slow part.
- `readline` keeps the `\n`: harmless with `.split()`, but use `.strip()` when reading a whole line as a string.
- `join` needs strings: `map(str, out)` converts each element first. The separator goes before `.join`.
- `print` has named arguments: `end` (default `"\n"`) and `sep` (default `" "`).

## Control flow

| C++ | Python |
|---|---|
| `while (t--)` | `for _ in range(t):` (or `t -= 1`; there is no `--`) |
| `x++` / `mp[s]++` | `x += 1` / `mp[s] += 1` (no `++` either) |
| `for (int x : arr)` | `for x in arr:` |
| `else if` | `elif` |
| `c ? a : b` | `a if c else b` (no `? :`; `int(cond)` gives 1/0) |
| `{ }` | indentation; check which loop a line belongs to |

- Declare per-test-case containers **inside** the test loop.
- `return` only works inside a `def`. Top-level code uses `print`.

## 2D arrays

| C++ | Python |
|---|---|
| `vector<vector<int>> g(n, vector<int>(m, 0))` | `g = [[0] * m for _ in range(n)]` |
| `g[i][j]` | `g[i][j]` |
| rows / cols | `len(g)` / `len(g[0])` |
| read n rows | `g = [list(map(int, input().split())) for _ in range(n)]` |

- **Never** `[[0] * m] * n`: `[0] * m` runs once, and `* n` copies the *pointer* to that one row n times, so editing one row edits "all" of them.
- Lists hold **references** (pointers). `a = b` gives two names for one list; it doesn't copy.
- `x[i] = v` repoints slot i (ints are immutable, so `[0] * m` is safe). The bug only appears when slots share a **mutable** object (a list) and you edit *inside* it.
- `[0]` on its own **creates** a list; `row[0]` **indexes** into one.

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
- `heapq.heapify(lst)` builds a heap in O(n), in place.
- Do arithmetic on the **positive** value, then negate: `-7 // 2 == -4` (Python floors toward -inf; C++ truncates to -3).

## dict / defaultdict / set

| C++ | Python |
|---|---|
| `unordered_map` | `dict` (`{}`) |
| `mp.count(k)` | `k in mp` |
| `mp.erase(k)` | `del mp[k]` or `mp.pop(k, None)` (safe) |
| `for (auto& [k, v] : mp)` | `for k, v in mp.items():` |
| `map` where `mp[k]++` creates k | `defaultdict(int)` |
| `unordered_set` | `set()` (`{}` is an empty **dict**) |
| `unordered_set<ll> s(v.begin(), v.end())` | `s = set(arr)` |
| `s.erase(x)` | `s.discard(x)` (safe) / `s.remove(x)` (crashes if missing) |

- Plain dict: `mp[k] += 1` on a missing key → `KeyError`. Use `mp.get(k, 0)` or `defaultdict(int)`.
- `defaultdict(int)` passes the **function** `int`, which is called for each missing key (`int()` = 0, `list()` = []).
- With defaultdict, just **reading** `mp[k]` inserts k. Use `k in mp` to check without inserting.
- Looping over a dict gives **keys**. Use `.items()` for pairs.
- `from collections import ...`, lowercase. `list`, `dict`, `set` are built in: never import them.
- `range()` takes a number. To loop over a list (or `sorted(s)`), write `for x in lst:` directly.
- `map<K, vector<T>>` → `defaultdict(list)`. Need fast front removal → `defaultdict(deque)` + `popleft()`.
- `deque` is imported from `collections` (`from collections import defaultdict, deque`), not `import deque`.
- `list.pop(0)` is O(n); `popleft()` exists only on a deque.
- A key can exist with an **empty** list/deque after removals. `k in mp` isn't enough before `[0]` / `popleft()`: check `if mp[k]:`.
- `del mp[k]` on a missing key → `KeyError`. Guard with `if k in mp:` or use `mp.pop(k, None)`.

## Sorted containers (the big gap)

- `dict` / `set` are **not sorted**. A dict keeps insertion order.
- `sorted(mp)` gives sorted keys. `sorted(mp.items())` gives pairs sorted by key. `sorted(mp.items(), key=lambda kv: kv[1])` sorts by value.
- No `std::set` / `map` / `multiset`. `sortedcontainers` is third-party and **not available on my OA platform**.
- Standard-library workaround: a sorted list + `bisect_left` (lower_bound) / `bisect.insort`. O(n) insert, fast up to ~1e5.
- Only need min/max with deletions → `heapq` + lazy deletion.
- `bisect_right(a, x)` = `upper_bound`: first index with `a[i] > x`, or `len(a)` (= `end()`). `bisect_left` = `lower_bound` (first `>= x`).
- Replacing `a[bisect_right(a, x)]` with `x` keeps `a` sorted. That's a multiset replacement with no shifting (Towers, LIS).
- A heap is **not** sorted: only `pq[0]` (the min) is meaningful. Sets can't be indexed at all.
- Don't name variables `id`, `list`, `max`, `sum`, `input`, `str`: it hides the built-in.
- Multiset → count map `defaultdict(int)`; erase one copy with `cnt[x] -= 1` and `del` at 0. Sorted output: `sorted(cnt)` once, print each x `cnt[x]` times.
- Clearing: clear **every** container you keep in sync (`st.clear()` *and* `mp.clear()`).
- Heavy ordered-set work on an OA → C++.

## itertools

- No `next_permutation`. `itertools.permutations(a)` yields **tuples**, follows input **positions** (sort first), and repeats duplicates.
- `permutations(a, r)` gives nPr, `combinations(a, r)` gives nCr, and `product(a, repeat=k)` replaces nested loops.

## Performance

- Python is ~10-100x slower per operation in your own loops. Built-ins (`sort`, `sum`, `Counter`, `max`) run in C.
- About 1e8 simple operations: C++ is fine, Python risks TLE.
- `%` with a positive mod is never negative in Python: `(a - b) % M` is safe (no `+ M` needed like C++).
- Out-of-range index raises `IndexError` (C++ silently writes past the array). Size difference arrays `MAX + 2`.
