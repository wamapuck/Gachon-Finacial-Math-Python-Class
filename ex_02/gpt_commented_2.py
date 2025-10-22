# ======================
# 2. 예제: 이름 목록 반복 및 조건 검사
# ======================
names = ["alex","bob","chris","david","alice"]

# 1) 리스트 순회하여 이름 출력
for i in names:
    print(i)

# 2) 이름이 "chris"일 때 "XXX" 출력, 그 외에는 이름 그대로 출력
for i in names:
    if i == "chris":
        print("XXX")
    else:
        print(i)

# 3) 첫 글자가 'a'인 이름은 "XXX" 출력, 그 외에는 이름 그대로 출력
for i in names:
    if i[0] == "a":
        print("XXX")
    else:
        print(i)

# ---------------------------------------------------------------------
# 분석
# 1. 전체 로직 분석
# - 총 세 개의 for 루프:
#   1) 모든 이름 출력
#   2) 특정 이름(chris) 조건부 대체 출력
#   3) 이름 첫 글자 조건부 대체 출력
#
# 1-1. 목적과 의도
# - for 루프를 통한 리스트 순회 방법 연습
# - if-else를 이용한 조건 검사 예제
# - 문자열 인덱싱(i[0]) 연습
#
# 1-1-1. 세부 로직
#  1) 첫 번째 루프: print(i)
#  2) 두 번째 루프: if i == "chris": print("XXX") else: print(i)
#  3) 세 번째 루프: if i[0] == 'a': print("XXX") else: print(i)
#
# 2. 사용된 함수/메서드
# - print(): 출력
# - list iteration: for i in names
# - if-else: 조건 분기
# - str.__getitem__: 문자열 인덱싱
#
# 3. 변수 의미
# - names (list): 분석 대상 이름 목록
# - i (str): 루프에서 추출되는 각 이름
# ======================================================================