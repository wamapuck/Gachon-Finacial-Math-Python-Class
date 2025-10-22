# -*- coding: utf-8 -*-
"""
Yoda 변환 스크립트 및 분석 템플릿

이 파일은 모든 코드 분석에 적용되는 기본 템플릿을 포함합니다.
아래 구조를 준수하여, 코드 아래에 분석을 주석으로 작성합니다:

1. 전체 로직 분석
1-1. 코드의 목적과 의도 분석
1-1-1. 세부 코드 로직 및 기능 분석
2. 사용된 함수와 메서드 설명
3. 변수 분석 및 의미 설명
"""

# ----------------------
# 1. 원본 예제: Yoda 스타일 문장 재배치
# ----------------------
original = "one two three"
e = original.split()  # ['one','two','three']

# 슬라이싱 예시 (결과를 변수에 저장하지 않고 출력용으로만 평가됨)
e[2:3] + e[1:2] + e  

# ----------------------
# 2. 마스터 문장 변환
# ----------------------
master = "you must have patience my young padawan"
e = master.split()  # ['you','must','have','patience','my','young','padawan']

first = e[3:4]     # ['patience']
second = e[:3]     # ['you','must','have']
third = e[4:]      # ['my','young','padawan']

yoda = first + second + third

yoda = " ".join(yoda)  # 'patience you must have my young padawan'

# 타입 확인 (주석 처리됨)
# print(type(yoda))  # <class 'str'>

# 최종 출력: 처음 22자를 대문자로 변환
print(yoda[:22].upper() + yoda[22:])  # PATIENCE YOU MUST HAVE my young padawan

# =====================================================================
# 1. 전체 로직 분석
# - 문자열 분리(split)과 리스트 슬라이싱을 실험
# - 주어진 문장을 Yoda 말투처럼 재배치 후 대문자 강조 출력
#
# 1-1. 코드의 목적과 의도 분석
# - split()과 슬라이싱 동작을 이해하기 위한 실험적 예제
# - Yoda 스타일 문장 생성 및 문자열 조작 기능 시연
#
# 1-1-1. 세부 코드 로직 및 기능 분석
#  1) original 변수 분할 테스트
#  2) master 변수에서 단어별 분할 및 부분 리스트(first, second, third) 추출
#  3) 추출된 리스트를 순서대로 결합하여 새로운 리스트(yoda) 생성
#  4) join()으로 문자열 결합 후 일부 문자를 대문자로 변환하여 출력
#
# 2. 사용된 함수와 메서드 설명
# - str.split(): 문자열을 공백 기준으로 분리하여 리스트 반환
# - list[start:stop]: 리스트 슬라이싱으로 부분 리스트 반환
# - " ".join(list): 리스트 요소를 공백으로 연결하여 문자열 반환
# - str.upper(): 문자열을 대문자로 변환
# - print(): 화면 출력 함수
#
# 3. 변수 분석 및 의미 설명
# - original (str): 테스트용 원본 문자열
# - e (list): split() 결과 리스트
# - master (str): Yoda 변환 대상 문장
# - first, second, third (list): 슬라이싱으로 추출된 부분 리스트
# - yoda (list/str): 결합 전 리스트, 결합 후 문자열
# =====================================================================
