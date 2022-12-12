#설정
save_file = "meta.ini" #파일명 설정
target = "New" #목표 설정

#작업경로 설정
import sys, os
app_path = os.path.join(os.path.dirname(sys.argv[0])) #현재 위치 확인
os.chdir(app_path)

#초기화
while 1:
    if os.path.isfile(save_file): os.remove(save_file)
    else:
        print("기존 파일 삭제 완료")
        break

#딕셔너리 생성
json_memory = {}

#
from glob import glob
file_list =  glob(app_path + "/" +  target + "/**", recursive=True)

n = 0
for i in file_list:
    if os.path.isfile(i): #폴더는제외 파일만
        n += 1
        rel_path = os.path.dirname(os.path.relpath(i)) #상대경로
        file = os.path.basename(i) #파일명 <--- 중복될 수 있으므로 딕셔너리의 Key 위치에 있으면 안됨!
        path = rel_path[len(target):] #현재경로는 삭제하고
        date = str(int(os.path.getmtime(i))) #파일 수정 날짜
        json_memory.update({n:[file,path,date]})

#파일로 저장
import json
with open(save_file, 'w', encoding='UTF8') as f:
    json.dump(json_memory, f, indent=2, ensure_ascii=False)

print("완료")
print(n)