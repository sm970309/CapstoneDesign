import shutil
import os
import tarfile
from tqdm import tqdm

origin_path = 'E:\KsponSpeech\한국인 대화 음성\Training'

# 현재 작업 디렉토리에서 .gz 파일을 모두 가져옴
gz_files = [f for f in os.listdir(origin_path) if f.endswith(".gz")]
print(gz_files)

for gz_file in tqdm(gz_files):
    dir_name = gz_file.replace('.gz','')
    try:
        gz_file = os.path.join(origin_path,gz_file)
        with tarfile.open(gz_file, "r:gz") as tar:
            tar.extractall(path=os.path.join(origin_path,dir_name))
        os.remove(gz_file)
    except tarfile.ReadError as e:
        print(f"Error extracting {gz_file}: {str(e)}")

print('압축 해제 종료')

for path in os.listdir(origin_path):
    path = os.path.join(origin_path,path)
    print(path)
    while True:
        subdir_count = sum(os.path.isdir(os.path.join(path, d)) for d in os.listdir(path))
        print("하위 디렉토리 개수:", subdir_count)
        if subdir_count>1:
            break
        path = os.path.join(path,os.listdir(path)[0])
    print(path)
    print(os.listdir(path))
    shutil.move(path,origin_path)
