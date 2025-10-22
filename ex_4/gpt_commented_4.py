# ==============================================================
# 1. 전체 로직 분석
#
# 이 파일은 크게 두 부분으로 구성된다:
#   1) (주석 처리된) URL에서 텍스트 파일을 다운로드하는 함수 정의 및 호출
#   2) 로컬 'input.txt' 파일에서 특정 문자열('202531340')을 찾아
#      'output.txt'에 기록하고, 해당 줄의 마지막 문자를 출력
#
# ==============================================================

# --------------------------------------------------------------
# 1‑1. 코드의 목적과 의도 분석
#
# - 목적: 인터넷 또는 로컬 파일에서 특정 키값('202531340')을 검색하여
#   결과를 별도의 출력 파일('output.txt')에 저장하고, 해당 줄의 마지막 문자를
#   화면에 출력함으로써 간단한 파일 I/O 흐름과 예외 없는 자원 관리를 실습
# - 의도: 
#   1) urllib.request를 사용한 파일 다운로드 과정을 보여주고,
#   2) open()/write() versus with 문을 이용한 파일 쓰기 방식을 비교
#
# --------------------------------------------------------------

# --------------------------------------------------------------
# 1‑1‑1. 세부 코드 로직 및 기능 분석
#
# Part A (주석 처리됨):
#   - download_file(url, filename):
#       * urllib.request.urlopen()으로 URL에서 바이트 읽기
#       * UTF-8로 디코딩 후 로컬 파일에 쓰기
#
# Part B:
#   - out = open('output.txt', 'w')
#       * 수동으로 파일 객체를 열어 write 모드 준비
#   - for line in open('input.txt'):
#       * 'input.txt'를 한 줄씩 읽으며 반복
#       * if line == '202531340': (정확히 일치할 때)
#           - print(line[-1]): 마지막 문자 출력
#           - _ = out.write(line): 출력을 파일에 기록 (반환값은 쓰여진 문자 수)
#   - with open('output.txt', 'w') as f:
#       * 컨텍스트 매니저를 사용해 파일 열기 및 자동 닫기
#     - for line in open('input.txt'): (동일 반복)
#       * 일치 시 print 및 f.write(line)
#   - out.close(): Part B 첫 번째 방식의 파일 객체 닫기
#   - input.close(): 잘못된 호출 (input() 내장 함수에 대한 잘못된 접근)
#
# --------------------------------------------------------------

# --------------------------------------------------------------
# 2. 사용된 함수와 메서드 설명
#
# - urllib.request.urlopen(url).read(): URL에서 바이트를 읽어들임
# - bytes.decode('utf-8'): 바이트를 UTF-8 문자열로 디코딩
# - open(filename, mode): 파일을 열어 파일 객체 반환
# - file.write(text): 문자열을 파일에 기록, 기록된 길이(문자 수) 반환
# - for line in open('input.txt'): 파일을 한 줄씩 순회
# - print(value): 값을 stdout으로 출력
# - with open(...) as f: 컨텍스트 매니저, 블록 종료 시 자동으로 파일 닫기
#
# --------------------------------------------------------------

# --------------------------------------------------------------
# 3. 변수 분석 및 의미 설명
#
# original URL 다운로드 부분 (주석 처리됨)
# - url      : 다운받을 원격 파일의 주소
# - filename : 로컬에 저장할 파일명
#
# Part B
# - out   : 첫 번째 방식으로 연 output.txt에 대한 파일 객체
# - line  : 'input.txt'에서 순회 중인 현재 줄 문자열
# - f     : with 문을 통해 연 output.txt에 대한 파일 객체
# - _     : write() 호출 시 반환값(문자 수)을 무시하기 위한 임시 변수
#
# ==============================================================

# -------------------- 코드 시작 --------------------

# # import urllib.request
# #
# # def download_file(url, filename):
# #     txt = urllib.request.urlopen(url).read().decode('utf-8')
# #     open(filename, 'w').write(txt)
# #
# # download_file('http://jonghyup.com/tmp/input.txt', 'input.txt')


# 첫 번째: 수동으로 파일 열고 쓰기
out = open('output.txt', 'w')

for line in open('input.txt'):
    # 정확히 '202531340' 문자열과 일치하는 줄만 처리
    if line == '202531340':
        # 마지막 문자 출력
        print(line[-1])
        # 전체 줄을 output.txt에 기록, 반환값(문자 수)은 무시
        _ = out.write(line)

# 두 번째: with 문을 사용해 자동으로 파일 닫기
with open('output.txt', 'w') as f:
    for line in open('input.txt'):
        if line == '202531340':
            print(line[-1])
            _ = f.write(line)

# 자원 정리
out.close()
# 잘못된 호출: input은 내장 함수이므로 파일 객체가 아님
# - 실제 파일 객체를 close하려면 열었던 변수명을 사용해야 함
# input.close()
