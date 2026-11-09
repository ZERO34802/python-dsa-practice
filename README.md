# Python DSA Practice

Re-learning DSA in Python, coming from C++ (STL, AlgoZenith up to DP).
Goal: write Python about as fast as C++, without looking up syntax.

Syntax notes: [CHEATSHEET.md](CHEATSHEET.md)

## Progress

| # | Topic | Status |
|---|---|---|
| 1 | Python's "STL" (list, tuple, str, dict, defaultdict, Counter, set, deque, heapq, bisect, itertools, math) | Done |
| 2 | Arrays and hashing | |
| 3 | Two pointers and sliding window | |
| 4 | Prefix sums and binary search (incl. on the answer) | In progress |
| 5 | Stacks and queues (monotonic stack/queue) | |
| 6 | Linked lists | |
| 7 | Recursion and backtracking | |
| 8 | Trees | |
| 9 | Heaps and greedy | |
| 10 | Graphs (BFS/DFS, Dijkstra, topo sort, union-find) | |
| 11 | Dynamic programming | |

## Solved

| Topic | Problem | File | Key idea |
|---|---|---|---|
| 1 | All permutations of 1..n | [all_permutations.py](01-python-stl/all_permutations.py) | `itertools.permutations`, `print(end=" ")` |
| 1 | Queue using two stacks | [queue_two_stacks.py](01-python-stl/queue_two_stacks.py) | Pour only when out-stack empty, amortized O(1) |
| 1 | Map add / erase / print | [map_operations.py](01-python-stl/map_operations.py) | dict, `in`, `del`, `elif` |
| 1 | Every x appears exactly x times | [exactly_x_times.py](01-python-stl/exactly_x_times.py) | `defaultdict(int)` frequency count |
| 1 | Registration (AZ101) | [registration.py](01-python-stl/registration.py) | Count per name, print before incrementing |
| 1 | Common Absolute Difference | [common_absolute_difference.py](01-python-stl/common_absolute_difference.py) | Count earlier A[j] ± K with defaultdict |
| 1 | Priority Queue | [priority_queue.py](01-python-stl/priority_queue.py) | heapq + negation for max-heap |
| 1 | The Magical Candy Bag (AZ101) | [magical_candy_bag.py](01-python-stl/magical_candy_bag.py) | Greedy max-heap, halve before negating |
| 1 | Reduce the Array (AZ101) | [reduce_the_array.py](01-python-stl/reduce_the_array.py) | Min-heap optimal merge (Huffman) |
| 1 | Multimap (AZ101) | [multimap.py](01-python-stl/multimap.py) | `defaultdict(deque)`, guard empty entries |
| 1 | Set (AZ101) | [set_operations.py](01-python-stl/set_operations.py) | Built-in set, `sorted()` at print time |
| 1 | Students and Grades | [students_and_grades.py](01-python-stl/students_and_grades.py) | Hash set; check then add each arrival |
| 1 | Multiset (AZ101) | [multiset.py](01-python-stl/multiset.py) | Count map as multiset, sort at print |
| 1 | Towers (AZ101) | [towers.py](01-python-stl/towers.py) | Sorted list + `bisect_right`, replace in place |
| 4 | LR Sum Query | [lr_sum_query.py](04-prefix-sums-binary-search/lr_sum_query.py) | Prefix sums mod M, fast input |
| 4 | Buy Maximum Objects II | [buy_maximum_objects_ii.py](04-prefix-sums-binary-search/buy_maximum_objects_ii.py) | Sort + prefix sums + `bisect_right` |
| 4 | Good Numbers | [good_numbers.py](04-prefix-sums-binary-search/good_numbers.py) | Difference array + two prefix sums, fast I/O |

## Language decisions

- **OAs:** C++ for now, especially for ordered set/map/multiset with lower_bound or heavy loops.
- **Live interviews and projects:** Python.
