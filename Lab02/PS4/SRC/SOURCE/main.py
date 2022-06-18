from algorithm import *

def main():
    for i in range(5):
        algo = Algorithm()

        fileIn = '../INPUT/input' + str(i+1) + '.txt'
        algo.readData(fileIn)

        fileOut = '../OUTPUT/output' + str(i+1) + '.txt'
        algo.saveNameFileOut(fileOut)

        algo.pl_Resolution()
    # Chạy code thầy xóa trước các output đi ạ vì do em dùng f = open(self.fileOut, 'a') nên nó ghi vào cuối(ghi thêm vào) chứ không phải ghi đè file ạ
if __name__ == '__main__':
    main()
