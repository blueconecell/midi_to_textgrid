# Midi to textgrid
- midi to textgrid
  - 입력1 : midi 파일명
  - 입력2 : textgrid 파일명 (파일에 3개 이상의 Tier가 있어야하며 3번째 Tier에 저장됨)
  - 입력3 : 결과 도출 파일명

- shift
  - 입력1 : 편집할 textgrid 파일명 (파일에 3개 이상의 Tier가 있어야하며 3번째 Tier 에 저장됨)
  - 입력2 : 움직이고 싶은 interval이 3번째 Tier에 몇번째 interval인지
  - 입력3 : 어디로 움직이고 싶은지 1번째 or 2번째 Tier의 몇번째 interval인지
  - 입력4 : 결과 도출 파일명

- key_mover_to_flat_costomized
  - 입력1 : 이미 작업이 완료된 textgrid파일
  - 입력2 : 작업을 시작해야하는 다른 키의 textgrid파일
  - 입력3 : 변화된 키의 양
  - 입력4 : 결과 도출 파일명


prototype
needed -> .exe 형식으로 만들기, 일정시간부터 전체shift, 일정 시간부터 text만 shift

- wav -> midi 만들어야함
- midi to textgrid
  - msg부분 type -> note_off, note_on 모두 가져와서 2칸 간격으로 time, note_off or note_on 둘 중 하나 선택하여 note로 사용하여 데이터전처리하면 어떨까
