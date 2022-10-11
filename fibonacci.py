# Viết function nhập một số bất kỳ
# và in ra giá trị trong dãy số Fibonacci tại
# vị trí được nhập

def Fibo (n):
        if n < 0:
            raise Exception("Không nhập được số âm đâu nha!")
        elif n == 0 or n == 1:
            return 1
        return Fibo(n-1) + Fibo(n-2)
   
if __name__ == "__main__":
    print(Fibo(3))
    print(Fibo(4))
    print(Fibo(-1))
    
    
