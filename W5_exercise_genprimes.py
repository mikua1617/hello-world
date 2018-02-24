def genPrimes():
    primes=[2]
    prime=2
    flag=0
    while True:
        prime+=1
        flag=0
        for i in primes:
            if prime%i==0:
                flag=1
                break

        if flag==0:
            primes.append(prime)
            next=primes

        yield next    
