#hackerrank
def SockMerchant(ar):
    color= []
    total = 0
    for i in ar:
        if i not in color:
            color.append(i)
    for c in color:
        pair = 0
        for socks in ar:
            if c==socks:
                pair+=1
        rem = pair%2
        pair = pair-rem
        P = pair//2
        total +=P
return(total)
SockMerchant([5,2,2,5,79,7,1,0,1,5])


    