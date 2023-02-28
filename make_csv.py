import pandas as pd

# 욕 들어간거: neg,  욕 없는거: pos
# 자기 담당에 맞게 주석처리 후 실행

# df=pd.read_csv('pos_linklist.csv')
df =pd.read_csv('neg_linklist.csv')
df = df.iloc[:,1:]
print(df)

array = []
while True:
    url = input("URL: (종료:! 입력)")
    if url=="!": break
    start = input("Start: ")
    end = input("End: ")
    text = input("Text: ")
    row = [url,start,end,text]
    print(row)
    if input('(맞으면 ㅇ(한글)입력): ')!='ㅇ': continue
    array.append([url,start,end,text])
new_df = pd.DataFrame(array,columns=['url','start','end','text'])
new_df = pd.concat([df,new_df])

new_df.to_csv('pos_linklist.csv')
# new_df.to_csv('neg_linklist.csv')