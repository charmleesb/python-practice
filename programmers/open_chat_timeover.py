def solution(record):
    answer = []
    users = {}
    result = ()
    for text in record:
        message = text.split(' ')[0]
        if 'Enter' in message:
            id, name = text.split(' ')[1:3]
            result += (id,)
            if id in users:
                prev_name = users[id]
                users[id] = name
                for i in range(len(answer)):
                    if result[i] == id:
                        answer[i] = answer[i].replace(prev_name, name)
            else:
                users[id] = name
            
            answer.append(users[id] + '님이 들어왔습니다.')

        elif 'Leave' in message:
            id = text.split(' ')[1]

            result += (id,)
            answer.append(users[id] + '님이 나갔습니다.')
        elif 'Change' in message:
            id, name = text.split(' ')[1:3]
            prev_name = users[id]
            users[id] = name
            for i in range(len(answer)):
                if result[i] == id:
                    answer[i] = answer[i].replace(prev_name, name)

    return answer
