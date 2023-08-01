############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calculate_sum_number(word):
    total = 0
    for w in word:
        if w.isdigit():
            total += int(w)
    return total
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행을 위한 코드입니다. 
if __name__ == '__main__':
    print(calculate_sum_number('ab123cd45ef6')) # => 21
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.