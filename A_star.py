from collections import defaultdict
from queue import PriorityQueue

#Graph
data = defaultdict(list)
data['A'] = ['B',2,'C',1,'D',3,6]
data['B'] = ['E',5,'F',4,3]
data['C'] = ['G',6,'H',3,4]
data['D'] = ['I',2,'J',4,5]
data['E'] = [3]
data['F'] = ['K',2,'L',1,'M',4,1]
data['G'] = [6]
data['H'] = ['N',2,'O',4,2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]
#Tạo ra 1 class Node lưu giá trị các nút
class Node:
    #Hàm tạo
    def __init__(self,name,par = None, g=0,h=0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h
    #In ra Node
    def display(self):
        print(self.name, self.g, self.h)
    #So sánh hàm đánh giá giữa 2 Node
    def __lt__ (self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h
    #Xem 2 Node có giống nhau không
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name
#Kiểm tra xem 2 Node có cùng tên không
def equal(O,G):
    if O.name == G.name:
        return True
    return False
#Kiểm tra xem Node có trong hàng đợi không
def checkInPriority(tmp,c):
    if tmp == None:
        return False
    return (tmp in c.queue)
#In ra đường đi
def getPath(O):
    print(O.name)
    if O.par != None:
        getPath(O.par)
    else:
        return
#Thuật toán tìm kiếm A*
def Astar(S, G):
    _open = PriorityQueue()
    _closed = PriorityQueue()
    S.h = data[S.name][-1]
    _open.put(S)

    while True:
        if _open.empty() == True:
            print('Tìm kiếm thất bại')
            return
        O = _open.get()
        _closed.put(O)
        print("Duyệt nút: ", O.name, O.g, O.h)

        if equal(O,G) == True:
            print("Tìm kiếm đã thành công!")
            print("Đường đi:") 
            getPath(O)
            print("Quãng đường: ", (O.g + O.h))
            return
        #Kiem tra con cua O
        i = 0
        while i < len(data[O.name]) -1:
            name = data[O.name][i]
            g = O.g + data[O.name][i+1]
            h = data[name][-1]
            tmp = Node(name = name, g = g, h=h)
            tmp.par = O

            check1 = checkInPriority(tmp,_open)
            check2 = checkInPriority(tmp,_closed)

            if not check1 and not check2:
                _open.put(tmp)

            i+=2
#Nhập điểm bắt đầu và kết thúc
S=input("Nhập điểm bắt đầu: ")
S=S.upper()
while S not in data:
    print("Vui lòng nhập điểm có trong đồ thị!")
    S=input("Nhập lại điểm bắt đầu: ")
    S=S.upper()

G=input("Nhập điểm kết thúc: ")
G=G.upper()
while G not in data:
    print("Vui lòng nhập điểm có trong đồ thị!")
    G=input("Nhập lại điểm kết thúc: ")
    G=G.upper()
    
#Gọi hàm
Astar(S= Node(S), G = Node(G))
