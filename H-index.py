def solution(citations):
    print(citations)
    print(type(citations))
    citations.sort(reverse=True)
    print(citations)
    #H지수는 게재된 논문의 수보다 인용지수가 작아진 갑을 의미함
    # 3, 0,6,1,5= > 5편 논무이라면 인용수는 5이상 나와야 함
    #5이상이 되지 않는 인용수는 3,1,0이며, 그 중 가장 큰수는 3임
    for idx, citation in enumerate(citations):
        print("idx : ", idx)
        print("citation : ", citation)
        if idx >=citation :
            return idx
    return len(citations)
