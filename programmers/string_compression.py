'''
2020 KAKAO BLIND RECRUITMENT > 문자열 압축
'''

def solution(s):
    answer = 0
    unit = 1
    string_answer = s

    while unit < len(s):
        n = 0
        count = 1
        temp_answer = ''
        while n < len(s):
            temp = s[n:n+unit]
            if s[n+unit:n+unit+unit] == temp:
                count += 1
            else:
                if count != 1:
                    temp_answer += str(count) + temp
                else:
                    temp_answer += temp
                count = 1
            n += unit
            
        if len(temp_answer) < len(string_answer):
            string_answer = temp_answer
            
        unit += 1

    answer = len(string_answer)
    return answer