import textgrid

fin_tg_fname = input('이미 작업이 완료된 파일명을 입력해주세요 : ')
blank_tg_fname = input('작업을 시작해야하는 다른 키의 파일명을 입력해주세요 : ')
key_change_amount = int(input('변화된 키의 양을 입력해주세요 : '))
write_name = input('결과물 파일명을 입력해주세요 : ')

fin_tg_fname = fin_tg_fname+'.TextGrid'
blank_tg_fname = blank_tg_fname+'.TextGrid'
write_name = write_name + '.TextGrid'

fin_tg = textgrid.TextGrid.fromFile(fin_tg_fname)
blank_tg = textgrid.TextGrid.fromFile(blank_tg_fname)

note_scale = {}
for i in range(40, 100):
    if i%12==0:
        note_scale[i]=f'C{i//12 - 1}'
    elif i%12==1:
        note_scale[i]=f'Db{i//12 - 1}'
    elif i%12==2:
        note_scale[i]=f'D{i//12 - 1}'
    elif i%12==3:
        note_scale[i]=f'Eb{i//12 - 1}'
    elif i%12==4:
        note_scale[i]=f'E{i//12 - 1}'
    elif i%12==5:
        note_scale[i]=f'F{i//12 - 1}'
    elif i%12==6:
        note_scale[i]=f'Gb{i//12 - 1}'
    elif i%12==7:
        note_scale[i]=f'G{i//12 - 1}'
    elif i%12==8:
        note_scale[i]=f'Ab{i//12 - 1}'
    elif i%12==9:
        note_scale[i]=f'A{i//12 - 1}'
    elif i%12==10:
        note_scale[i]=f'Bb{i//12 - 1}'
    elif i%12==11:
        note_scale[i]=f'B{i//12 - 1}'
        
note_scale_sharp = {}
for i in range(40, 100):
    if i%12==0:
        note_scale_sharp[i]=f'C{i//12 - 1}'
    elif i%12==1:
        note_scale_sharp[i]=f'C#{i//12 - 1}'
    elif i%12==2:
        note_scale_sharp[i]=f'D{i//12 - 1}'
    elif i%12==3:
        note_scale_sharp[i]=f'D#{i//12 - 1}'
    elif i%12==4:
        note_scale_sharp[i]=f'E{i//12 - 1}'
    elif i%12==5:
        note_scale_sharp[i]=f'F{i//12 - 1}'
    elif i%12==6:
        note_scale_sharp[i]=f'F#{i//12 - 1}'
    elif i%12==7:
        note_scale_sharp[i]=f'G{i//12 - 1}'
    elif i%12==8:
        note_scale_sharp[i]=f'G#{i//12 - 1}'
    elif i%12==9:
        note_scale_sharp[i]=f'A{i//12 - 1}'
    elif i%12==10:
        note_scale_sharp[i]=f'A#{i//12 - 1}'
    elif i%12==11:
        note_scale_sharp[i]=f'B{i//12 - 1}'
        
note_scale_reverse = {v:k for k,v in note_scale.items()}
note_scale_sharp_reverse = {v:k for k,v in note_scale_sharp.items()}
note_scale_reverse.update(note_scale_sharp_reverse)
blank_tg[2].__init__('int', 0.0, fin_tg.maxTime)

for i in fin_tg[2]:
    if (i.mark.strip() in note_scale_reverse):
        note = note_scale_reverse[i.mark.strip()] + key_change_amount
        blank_tg[2].add(i.minTime, i.maxTime, note_scale_sharp[note])
    else:
        blank_tg[2].add(i.minTime, i.maxTime, '')
        
blank_tg.maxTime = blank_tg[2][-1].maxTime
blank_tg[0].maxTime = blank_tg[2][-1].maxTime
blank_tg[1].maxTime = blank_tg[2][-1].maxTime
blank_tg[2].maxTime = blank_tg[2][-1].maxTime
blank_tg[0][-1].maxTime = blank_tg[2][-1].maxTime
blank_tg[1][-1].maxTime = blank_tg[2][-1].maxTime

blank_tg.write(write_name)
