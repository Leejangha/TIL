# 실습 2-1

'''
다음은 이형기 시인의 "낙화"의 한 구절이다.
- 1연
	가야할 때 언제인가를
	분명히 알고 가는 이의
	뒷모습은 얼마나 아름다운가.

나는 이 시를 보며 '나는 내가 가야할 때가 언제일까?' 를 생각해 보았다.
'''

print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n- 1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')


# 실습 2-2

# 책 한 권당 print문을 한 번씩만 사용한다.
author_1 = '권필'
author_2 = '허균'
book_1 = '주생전'
book_2 = '홍길동전'

print(f'{book_1}의 작가는 {author_1}이고,\n{author_2}은 {book_2}를 집필하였다.')


# 실습 2-3

books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

print("{} : {}".format(authors[1], books[3]))
print("{} : {}".format(authors[3], books[1]))
print("{} : {}".format(authors[0], books[2]))
print("{} : {}".format(authors[2], books[0]))
print("{} : {}".format(authors[4], books[4]))


# 실습 2-4

information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

'''
- 작가와 작품 목록 참고
- 허균 : 홍길동전, 장생전, 도문대작
- 임제 : 수성지, 백호집, 원생몽유록
- 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
'''

information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

for key, value in information.items():
    print(f'{key} : {value}')


# 실습 2-5

import copy

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성']
]

backup_catalog = copy.deepcopy(catalog)

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']


print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(backup_catalog == catalog)


print('backup_catalog : ')
print(backup_catalog)


print('catalog : ')
print(catalog)


# 과제 2-2

book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(int(book) * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(total - int(rental))


# 과제 2-4

authors = ['작자 미상', '이항복', '임제', '임제', 
           '조성기', '조성기', '조성기', '임제', 
           '허균', '허균', '허균', '임제', '임제', 
           '임제', '임제', '임제', '임제', '임제', 
           '임제', '임제', '임제', '박지원', '이항복', 
           '남영로', '남영로', '남영로', '이항복', '임제', '임제']


print(list(set(authors)))
