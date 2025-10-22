import heapq

input = open('input.txt', 'r')
lines = input.read().splitlines()
input.close()
N = int(lines[0])
lists = [list(map(int, lines[i+1].split())) for i in range(N)]

heap = [(lists[i][0], i, 0) for i in range(N)]
heapq.heapify(heap)

out = []
while heap:
    val, li, idx = heapq.heappop(heap)
    out.append(val)
    nxt = idx + 1
    if nxt < len(lists[li]):
        heapq.heappush(heap, (lists[li][nxt], li, nxt))

output = open('output.txt', 'w')
output.write(' '.join(map(str, out)))
output.close()
