#사용자 정의 함수
def sumcalc(n):
    """1~n까지의 합계를 구하여 리턴한다."""
    sum = 0
    for num in range(1, n+1):
        sum += num
    return sum
help(sumcalc)

"""docstring : 함수이름과 본체 사이에 작성하는 문자열 함수의 활용성을
높이려고자세한함수 사용법이나 인수의 의미, 주의사항 등을 문서로 남기는것."""