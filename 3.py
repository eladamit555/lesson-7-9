all_votes = {}
while True:
    id = input('enter id: ')
    if id == '-999':
        break
    vote = input('enter vote: ')
    if vote != 'A' and vote != 'B' and vote != 'C' and vote != 'D':
        print('party doesnt exist')
        continue
    if id not in all_votes:
        all_votes[id] = vote
    else:
        all_votes[id] = 'F'
print(all_votes)
count = {}
for v in all_votes.values():
    if v == 'F':
        continue
    count[v] = count.get(v, 0) + 1
print(sorted(count.items(), reverse=True))
print(max(count, key=count.get), max(count.values()))

