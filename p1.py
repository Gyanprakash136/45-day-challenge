def magical_day_counter(n:int,scoreboard:list):
    day = 0
    prev = 0
    current = 1
    next = 2

    while(next < n):
        if((scoreboard[current] > scoreboard[next])and (scoreboard[current] > scoreboard[next])):
            day += 1
        prev = current
        current = next
        next +=1

    return  day


days = int(input("Enter number of days in your streak: "))
scorecard = list(map(int,input("Enter your score seperated by space:").split()))

a = magical_day_counter(days,scorecard)
print(a)


