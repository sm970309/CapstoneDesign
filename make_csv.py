import pandas as pd

# df =pd.DataFrame({'url':'youtube.com','start':10,'end':20,'text':'예시입니다'},index=[0])
# df.to_csv('linklist.csv')
df =pd.read_csv('linklist.csv')
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

new_df.to_csv('linklist.csv')
