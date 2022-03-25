def solution(record):
    answer = []
    users = {}
    message_count = 0
    for text in record:
        message = text.split(' ')[0]
        if 'Enter' in message:
            id, name = text.split(' ')[1:3]
            if id in users:
                prev_name = users[id][0]
                index = users[id][1]
                users[id][0] = name
                for i in index:
                    answer[i] = answer[i].replace(prev_name, name)
                users[id][1].append(message_count)

            else:
                users[id] = [name, [message_count]]

            message_count += 1
            answer.append(users[id][0] + '님이 들어왔습니다.')

        elif 'Leave' in message:
            id = text.split(' ')[1]
            answer.append(users[id][0] + '님이 나갔습니다.')
            users[id][1].append(message_count)
            message_count += 1
        elif 'Change' in message:
            id, name = text.split(' ')[1:3]
            prev_name = users[id][0]
            index = users[id][1]
            users[id][0] = name
            for i in index:
                answer[i] = answer[i].replace(prev_name, name)

    return answer
