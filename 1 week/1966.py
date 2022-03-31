casecountnumber=int(input())
   
for _ in range(casecountnumber):
    datacount_, target = map(int, input().split(" "))
    impo = list(map(int,input().split(" ")))
    data=list()
    
    for a in impo:
        data.append(a)
        
    impo.sort(reverse=True)
    datex=list()
    count=1
    for datanum in range(datacount_):
        datex.append(datanum)#index넘버
        
    while True:#프린터가 되는 문서나올때바다반복됨
        usun=impo.pop(0)#우선순위 제일 높은것 꺼냄
        while True: #usun과 같은거 나올때까지 팝
            index=datex.pop(0)
            imdata=data.pop(0)
            if imdata==usun:
                break
            datex.append(index)
            data.append(imdata)
        if target==index:
            break
        count+=1
    print(count)
