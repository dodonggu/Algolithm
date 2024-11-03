import re

def solution(new_id):
    # 1단계: 대문자 -> 소문자
    new_id = new_id.lower()
    
    # 2단계: 정규식을 활용해 허용된 문자를 제외하고 제거(공백으로 대체)
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    
    # 3단계: 연속된 마침표 하나로 대체
    new_id = re.sub('\.+', '.', new_id)
    
    # 4단계: 앞뒤 마침표 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열 'a'로 대체
    if new_id == '':
        new_id = 'a'
    
    # 6단계: 길이 16자 이상 15로 제한과 마침표 제거
    new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이가 2자 이하일 경우, 마지막문자 반복해서 3자로 바꾸기
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id