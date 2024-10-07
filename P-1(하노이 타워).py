import time


x = int(input("하노이 타워의 높이"))
cnt = 0

start = time.time()
def hanoi_tower(n,top_1,top_2,top_3):
    global cnt
    if (n == 1) :
        print("원판 1: %s --> %s" % (top_1, top_3))
    else :
        hanoi_tower(n - 1, top_1, top_3, top_2)
        print("원판 %d: %s --> %s" % (n, top_1, top_3))
        hanoi_tower(n - 1, top_2, top_1, top_3)
    cnt += 1

hanoi_tower(x,'A','B','C')
print("실행횟수 : ",cnt)

end = time.time()
print("실행시간 = ", end-start)

