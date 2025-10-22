# ======================
# 3. 예제: 단어 변환 함수들
# ======================

def add_dot(s):
    # 문자열 앞뒤에 '...'를 추가하여 반환
    dotAdded = '...' + s + '...'
    print(dotAdded)
    return dotAdded


def upper2(s):
    # 문자열의 처음 2글자를 대문자로 변경하여 반환
    upperAdded = s[:2].upper() + s[2:]
    print(upperAdded)
    return upperAdded


def change_word(word):
    # 단어의 첫 글자가 'a'이면 add_dot, 아니면 upper2 호출
    if word[0] == 'a':
        word = add_dot(word)
    else:
        word = upper2(word)
    return word

# ---------------------------------------------------------------------
# 분석
# 1. 전체 로직 분석
# - 세 가지 함수(add_dot, upper2, change_word) 정의 및 동작 흐름 구현
#
# 1-1. 목적과 의도
# - 문자열 편집 함수를 통해 조건에 따른 다양한 변형 방법 시연
# - add_dot: 단어 양쪽에 점 추가, upper2: 앞부분 대문자 변환
# - change_word: 조건 분기를 통한 함수 호출 예시
#
# 1-1-1. 세부 로직
#  1) add_dot(s): '...' + s + '...' 생성 및 출력
#  2) upper2(s): s[:2].upper() + s[2:] 생성 및 출력
#  3) change_word(word): 첫 글자 검사 후 해당 함수 호출
#
# 2. 사용된 함수/메서드
# - def: 함수 정의 키워드
# - str concatenation: 문자열 결합 '+'
# - str.upper(): 대문자 변환
# - print(): 출력
# - return: 함수 반환값 지정
#
# 3. 변수 의미
# - s (str): add_dot, upper2의 입력 문자열
# - dotAdded (str): add_dot에서 생성된 결과 문자열
# - upperAdded (str): upper2에서 생성된 결과 문자열
# - word (str): change_word의 입력 단어 및 반환값
