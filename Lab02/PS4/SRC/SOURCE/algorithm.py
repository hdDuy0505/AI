from copy import deepcopy

class Algorithm:
    def __init__(self):
        self.clauseList = [] # Dach sách mệnh đề tạo ra
        self.newClauseList = [] # Danh sách mệnh đề mới tạo ra sau mỗi lần lặp white
        self.n = 0 # Số lượng mệnh đề sau mỗi lần lặp white
        self.fileOut = None

    def readData(self, input_filename: str):
        f = open(input_filename, 'r')
        alpha = []
        KB = []
        countLine = -1 # Dùng để tính dòng đọc file hiện tại
        for line in f:
            countLine += 1
            if(countLine == 1): # Không cần lưu số lượng mệnh đề
                continue
            else:
                clause = line.split(' OR ')
                for i in range(len(clause)):
                    clause[i] = clause[i].strip() # Loại bỏ các khoảng trắng dư thừa ở đầu và cuối của mỗi phần tử
                clause.sort(key=self.sortByLiteralName) # Sắp xếp theo tăng dần chữ cái
                if(countLine == 0):
                    for x in self.createNegativeSentence(clause): # Nghich đảo alpha
                        alpha.append(x)
                else:
                    KB.append(clause) # Thêm mệnh đề KB 
        self.clauseList = deepcopy(KB)
        for sentence in alpha:
            self.clauseList.append(sentence)
        f.close()

    def pl_Resolution(self):
        while(True):
            count = 0 # Đếm số lượng mệnh đề mới tạo ra
            n = len(self.clauseList)
            for i in range(n):
                for j in range(i+1, n):
                    (number, newClause) = self.createNewClause(self.clauseList[i], self.clauseList[j]) # n: lấy số lần tạo cố ngẫu 2 mệnh đề, newClause: Mệnh đề mới
                    if number == 1: # Hợp giải được và sinh ra mệnh đề mới
                        count += 1
                        if len(newClause) == 0: # Hợp giải mà có mệnh đề {}
                            self.n = count # Lưu số lượng mệnh đề mới tạo ra
                            self.writeData('YES')
                            return True
                        self.newClauseList.append(newClause) # Thêm mệnh đề mới vào newClauseList
            self.n = count # Lưu số lượng mệnh đề mới tạo ra
            if count == 0: # Không tạo ra được mệnh đề mới
                self.writeData('NO')
                return False
            self.writeData(None) # Thêm các mệnh đề mới vào fileOut
            for i in self.newClauseList: # Thêm các mệnh đề mới vào clauseList
                self.clauseList.append(i)
            self.newClauseList = [] # reset danh sách mệnh đề mới

    def saveNameFileOut(self, nameFileOut): # Lấy tên output do người dùng nhập
        self.fileOut = nameFileOut
        
    def writeData(self, state):
        f = open(self.fileOut, 'a') # Mỗi lần mở file để write sẽ viết vào cuối file
        f.write(str(self.n) + '\n') # Ghi số lượng mệnh đề tạo ra output
        for clause in self.newClauseList: # Thêm các mệnh đề mới vào ouutput
            f.write(self.convertArrayToString(clause) + '\n') # Chuyển về dang ban đầu rùi mới viết vào file
        if state == 'YES':
            f.write('{}' + '\nYES')
        if state == 'NO':
            f.write('NO')
        f.close()

    def negative(self, e): # Đổi dấu phần tử(Ví dụ: negative(A) => -A)
        if len(e) == 2:
            e = e.strip('-')
        else:
            e = '-' + e
        return e

    def sortByLiteralName(self, e): # Điều kiện để sort(phần tử sẽ chuyển đổi thành không âm để sort mà không thay đổi giá trị của phần tử đó)
        if len(e) == 2:
            return self.negative(e)
        return e

    def createNegativeSentence(self, alpha): # Tạo mệnh đề đảo ngược
        for i in range (len(alpha)):
            alpha[i] = self.negative(alpha[i])
        if(len(alpha) == 1):
            return [alpha]
        return [[x] for x in alpha]
    
    def checkDuality(self, a, b): # Kiểm tra tính đối ngẫu
        if (a == self.negative(b)):
            return True
        return False

    def createNewClause(self, clauseA, clauseB): # Tạo mệnh đề mới
        n = 0 # Khởi tạo số lượng đối ngẫu
        newClause = deepcopy(clauseA) #  Đầu tiên copy ClauseA
        for i in clauseB:
            if i not in newClause: # Phần tử của clauseB chưa nằm trong newClause
                check = True # Kiểm tra có đối ngẫu hay không
                for literal in newClause:
                    if(self.checkDuality(i, literal)): # Có đổi ngẫu
                        newClause.remove(literal) # Xóa phần tử ra khỏi newClause
                        n += 1
                        check = False
                        break
                if check: # Không đối ngẫu ta thêm vào newClause 
                    newClause.append(i)
        newClause.sort(key=self.sortByLiteralName) # sort newClause tăng dần theo bảng chữ cái
        if newClause in self.clauseList or newClause in self.newClauseList: # Mệnh đề mới nằm trong clauseList hoặc trong newClauseList
            n = 0 # n = 1 mới là tạo mệnh đề mới, nên gán n = 0 để làm cờ để không thêm newClause vào newClauseList
        return (n, newClause)

    def convertArrayToString(self, clause): # Chuyển đổi về dạng mệnh đề
        stringClause = ''
        if len(clause) == 1: # Nếu có 1 phần tử
            for s in clause:
                stringClause += s
        else:
            for i in range (0, len(clause) - 1):
                tempString = '' # phần tử có thể âm(ví dụ: -A) 
                for s in clause[i]:
                    tempString += s
                stringClause += tempString + ' OR '
            stringClause += clause[len(clause)-1] # Thêm phần tử cuối 
        return stringClause            