def pizzaStore(M,N):
    Ps={}
    for i in range(N):
        Ps[i]=int(input())
    Ps=sorted(Ps.items(),key=lambda pz:(pz[1],pz[0]),reverse=True)
    #print(Ps[2])
    i=0
    cap=M
    sumSlices=0
    pizzas=[]
    while(sumSlices<M and cap>0 and i<N):
        if(sumSlices+Ps[i][1]<=M):
            sumSlices=sumSlices+Ps[i][1]
            pizzas.append(Ps[i])
            print('sumSlices ',sumSlices)
            cap=cap-Ps[i][1]
            print('cap ',cap)
        
        i=i+1

    print (sumSlices)
    for i in range(len(pizzas)):
        print(pizzas[i][0],' ')
    
pizzaStore(17,4)