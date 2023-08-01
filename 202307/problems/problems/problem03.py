############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_item_price(item_list):
    total = 0
    for item in item_list:
        total += item['price'] * item['count']

    return total
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행을 위한 코드입니다. 
if __name__ == '__main__':
    # 아래의 코드는 수정하지 마세요.
    SSAFANG_ITEM_LIST = [
        {
          'name': 'Galaxi Buds',
          'count': 3,
          'price': 150000,
        },
        {
          'name': 'Galaxi Pro Book 3',
          'count': 2,
          'price': 1500000,
        },
        {
          'name': 'Galaxi Mouse Pro',
          'count': 3,
          'price': 21000,
        },
    ]

    print(calc_item_price(SSAFANG_ITEM_LIST))  # => 3513000
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.