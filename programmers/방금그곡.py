# C# 등을 소문자로 변환
def change(string):
    if '#' in string:
        idx = string.index('#')
        return string.replace(string[idx-1:idx+1], string[idx-1].lower())
    return string

def find_music(m, musicinfos):
    answer = '(None)'
    answers = []

    for musicinfo in musicinfos:
        # 시간동안 재생 된 악보 정보
        play_music = ''

        start, end, title, info = musicinfo.split(',')
        
        # '#'개수만큼 바꿔주기!!!!!
        for _ in range(info.count('#')):
            info = change(info)
        
        # 재생 시간
        s_hours, s_minutes = map(int, start.split(':'))
        e_hours, e_minutes = map(int, end.split(':'))
        start = s_hours * 60 + s_minutes
        end = e_hours * 60 + e_minutes
        gap = end-start

        # 악보 길이
        play_length = len(info)

        # 시간동안 재생 된 악보 정보
        if gap > play_length:
            # repeat = gap // play_length
            # part =  gap % play_length
            # play_music = info * repeat
            # play_music += info[:part]
            play_music = info * (gap // play_length) + info[:gap % play_length]
        else:
            play_music = info[:gap]

        # 악보에서 네오가 들었던 패턴 찾기
        for _ in range(play_music.count(m[0])):
            start_point = play_music.index(m[0])

            # m의 첫 문자와 매칭되는 곳부터 m길이 만큼 잘라서, 비교
            if play_music[start_point:start_point + len(m)] == m:
                answers.append((gap, title))
            # m의 첫 문자 다음부터, 다시 시작
            play_music = play_music[start_point + 1:]

    if answers:
        ## 오름차순으로 하면 재생시간이 같을 경우 나중에 추가 된 title이 반환 됨
        # answers.sort(key=lambda x:x[0])
        # print(answers)
        # answer = answers[-1][1]

        ## 내림차순, [0][1]로하여, 재생시간이 같을 경우에도 먼저 추가 된 title을 반환
        answers.sort(key=lambda x:-x[0])
        # print(answers)
        answer = answers[0][1]
    return answer


def solution(m, musicinfos):
    # '#'개수만큼 바꿔주기!!!!!
    for _ in range(m.count('#')):
        m = change(m)
    return find_music(m, musicinfos)

print(solution("ABCDEFG", ["12:00,12:15,three,CDEFGAB", "12:00,12:14,one,CDEFGAB", "12:00,12:14,two,CDEFGAB"]))
print(solution("ABCDEFG", ["12:00,12:14,one,CDEFGAB", "12:00,12:14,two,CDEFGAB"]))
