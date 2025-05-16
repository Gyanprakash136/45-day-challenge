def shot_analyser(n:int):

    point_scored = []
    good_shots = 0
    missed_shots = 0
    for  i in range(n):
        a = int(input("Enter the points scored"))
        if(a>=0 and a<=10):
            if(a>=7):
                point_scored.append(a)
                good_shots = good_shots+1
            else:
                point_scored.append(a)
                missed_shots=missed_shots+1
    print(good_shots,missed_shots)



n = int(input("Enter the number of shots:"))
shot_analyser(n)