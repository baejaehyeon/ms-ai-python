def my_add(a,b) : 
    return a + b
def my_adds(*args) : 
    return sum(args)
def fourCalc(a, b) : 
    return a+b, a-b, a*b, a//b

# 현재 모듈에서 실행시키면 __name__은 '__main__' 값을 가진다
# 하지만 mymodule을 다른 모듈에서 실행시키면 아래 print에서 __name__은 mymodule로 출력됨.
# 즉, 현재 이 모듈 자체를 메인으로 실행 시키면 __main
# 그게 아니고 다른데에서 불러와져 실행되면 모듈 파일 이름
print(f'mymodule 내부에서의 __name__ : {__name__}')
