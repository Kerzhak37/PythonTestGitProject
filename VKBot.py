import vk
import time
import datetime

session = vk.Session('7741ef578fc49ec7f17501bff17ed58e2c343bc308d19735f92cb2298adf2012850be05502eac7980160c')

api = vk.API(session)

while(True):

    messages = api.messages.get()

    commands = ['стих','Privet','Poka','','help', 'weather']

    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if comand == 'help':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBot v0.1\n>Разработал: Elagin')
        if comand == 'стих':
            api.messages.send(user_id=user_id,
                              message='\nНочь, улица, фонарь, аптека,\nБессмысленный и тусклый свет.\nЖиви еще хоть четверть века —\nВсе будет так. Исхода нет.\nУмрешь — начнешь опять сначала\nИ повторится все, как встарь:\nНочь, ледяная рябь канала,\nАптека, улица, фонарь.\n')
        if comand == 'Privet':
            api.messages.send(user_id=user_id,
                              message='\n>Привет \nРазработал: Elagin')
        if comand == 'Poka':
            api.messages.send(user_id=user_id,
                              message='\n>Пока \nРазработал: Elagin')
        if comand == 'weather':
            api.messages.send(user_id=user_id,
                              message='\nПогода отличная!')

    ids = ', '.join([str(m[1]) for m in messages])

    if ids:
        api.messages.markAsRead(message_ids=ids)

    time.sleep(3)
