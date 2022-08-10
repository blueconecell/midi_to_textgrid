import mido
import textgrid

midi_fname = input('midi 파일명을 입력해주세요 : ')
tg_fname = input('TextGrid 파일명을 입력해주세요 : ')
write_name = input('결과물 파일명을 입력해주세요 : ')
midi_fname = midi_fname +'.mid'
tg_fname = tg_fname +'.TextGrid'
write_name = write_name +'.TextGrid'

note_scale = {}
for i in range(40, 100):
    if i%12==0:
        note_scale[i]=f'C{i//12 - 2}'
    elif i%12==1:
        note_scale[i]=f'Db{i//12 - 2}'
    elif i%12==2:
        note_scale[i]=f'D{i//12 - 2}'
    elif i%12==3:
        note_scale[i]=f'Eb{i//12 - 2}'
    elif i%12==4:
        note_scale[i]=f'E{i//12 - 2}'
    elif i%12==5:
        note_scale[i]=f'F{i//12 - 2}'
    elif i%12==6:
        note_scale[i]=f'Gb{i//12 - 2}'
    elif i%12==7:
        note_scale[i]=f'G{i//12 - 2}'
    elif i%12==8:
        note_scale[i]=f'Ab{i//12 - 2}'
    elif i%12==9:
        note_scale[i]=f'A{i//12 - 2}'
    elif i%12==10:
        note_scale[i]=f'Bb{i//12 - 2}'
    elif i%12==11:
        note_scale[i]=f'B{i//12 - 2}'
        
tg = textgrid.TextGrid.fromFile(tg_fname)
mid = mido.MidiFile(midi_fname)
msg = []
for i in mid:
    if i.type=='note_on'or i.type=='note_off':
        msg.append(i.dict())
time=[]
note=[]
for i in msg[1::2]:
    time.append(i['time'])
for i in msg:
    if i['type'] == 'note_on':
        eng_note = note_scale[i['note']]
        note.append(eng_note)
        
time_accumulate = []
stacking = msg[0]['time']
for i in time: 
    if i > 0.01:
        time_accumulate.append(stacking)
    stacking +=i    
    
def tg_creater(time_accumulate, note):
    time=[0.0]
    time = time + time_accumulate
    
    tg[2].__init__('int', 0.0, tg.maxTime)
    
    time_len = len(time)
    
    for i in range(time_len-2):
        tg[2].add(float(time[i+1]), float(time[i+2]), f"{note[i]}") 
        
        
#main
tg_creater(time_accumulate,note)
tg.write(write_name)
