def maxMeetings(start, end, n):
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])
    count = 1  
    last_end = meetings[0][1]
    for i in range(1, n):
        if meetings[i][0] > last_end:
            count += 1
            last_end = meetings[i][1]
    return count
start = [1, 3, 0, 5, 8, 5]
end =   [2, 4, 6, 7, 9, 9]
n = len(start)
print(maxMeetings(start, end, n))