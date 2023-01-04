def towers_of_hanoi(t1, t2, t3):
    move_disks(t1, t3, t2, len(t1))
    
def move_disks(src, dest, spare, top):
    if top == 1:
        dest.append(src.pop())
        return
    move_disks(src, spare, dest, top - 1)
    move_disks(src, dest, spare, 1)
    move_disks(spare, dest, src, top - 1)

n = 3
t1 = [n - i for i in range(n)]
t2 = []
t3 = []
print(t1, t2, t3)
towers_of_hanoi(t1, t2, t3)
print(t1, t2, t3)
    

def hanoi_towers(n):
    move(n, 'A', 'C', 'B')

def move(n, src, dest, spare):
    if n == 1:
        print(src, '->', dest)
        return
    move(n - 1, src, spare, dest)
    move(1, src, dest, spare)
    move(n - 1, spare, dest, src)

hanoi_towers(3)