import textgrid

tg_fname = input('편집 대상 파일명을 입력해주세요 : ')
loc = int(input('움직일 대상의 번호를 적어주세요 (midi 행): '))
shift_loc = int(input('움직이고 싶은 목적지의 번호를 적어주세요 (영어 또는 한글 행): '))
write_name = input('결과물 파일명을 입력해주세요 : ')
tg_fname = tg_fname+'.TextGrid'
write_name = write_name+'.TextGrid'

tg = textgrid.TextGrid.fromFile(tg_fname)

shift_amount = tg[0][shift_loc-1].minTime - tg[2][loc-1].minTime

tg[2][loc-2].maxTime += shift_amount



for i, j in enumerate(tg[2]):
    if i >= loc-1:
        j.minTime += shift_amount
        j.maxTime += shift_amount
        
tg.maxTime = tg[2][-1].maxTime
tg[0].maxTime = tg[2][-1].maxTime
tg[1].maxTime = tg[2][-1].maxTime
tg[2].maxTime = tg[2][-1].maxTime
tg[0][-1].maxTime = tg[2][-1].maxTime
tg[1][-1].maxTime = tg[2][-1].maxTime

tg.write(write_name)
