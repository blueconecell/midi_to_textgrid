from mido import MidiFile
import textgrid

mid = MidiFile("2022-06-29_2차_야생화_key-Ab-01(T69).mid")
tg = textgrid.TextGrid.fromFile('2022-06-29_2차_야생화_key-Ab-01_T69_.TextGrid')
def Data_creater(midi_file):
    midimsgs = []
    for i in midi_file:
        if i.type == 'note_on' or i.type == 'note_off':
            midimsgs.append(i.dict())

    mem1 = 0
    for i in midimsgs:
        time = i['time'] + mem1
        i['time'] = time
        mem1 = i['time']
    return midimsgs
tg[2].__init__('int', 0.0, tg.maxTime)


def createTG_for_intervalTier(Data):
    max_time = Data[-1]['time']
    data_len = len(Data)

    # body part
    time = ["0", ]
    text = ["", ]

    body = ""
    for i in range(data_len):
        data = Data[i]

        if data['type'] == 'note_on':
            text.append(data['note'])
            time.append(data['time'])

        elif data['type'] == 'note_off':
            text.append("")
            time.append(data['time'])

    time_len = len(time)
    intervals_no = 1

    #     for i,j in zip(time, text):
    #         print(i,j)

    # time 부분을 직접 넣어서 돌리는 방법으로 교체
    for i in range(time_len - 1):
        if abs(float(time[i]) - float(time[i + 1])) < 0.02:
            pass
        #           print('skipped :',time[i], time[i+1], text[i])
        else:
            tg[2].add(float(time[i]), float(time[i + 1]), f"{text[i]}")

# main

Data = Data_creater(mid)
createTG_for_intervalTier(Data)



tg.write("midi_to_textgrid_result.TextGrid")
