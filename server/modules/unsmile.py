from transformers import TextClassificationPipeline, BertForSequenceClassification, AutoTokenizer

model_name = 'server/modules/unsmile_model'

model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    device=-1,     # cpu: -1, gpu: gpu number
    return_all_scores=True,
    function_to_apply='sigmoid'
    )

def calcScore(textline):
    textlist = textline
    i = 0
    index = 0
    score = 0
    reasonlist = ['여성이나 가족을 비하하는 단어가 포함되어 있어요', '남성을 비하하는 단어가 포함되어 있어요',
            '성소수자를 비하하는 단어가 포함되어 있어요', '인종차별을 하는 단어가 포함되어 있어요', 
            '특정한 연령을 비하하는 단어가 포함되어 있어요', '특정 지역을 비하하는 단어가 포함되어 있어요',
            '특정 종교를 비하하는 단어가 포함되어 있어요', '혐오적인 단어가 포함되어 있어요',
            '악플이나 욕설인 단어가 포함되어 있어요', '깨끗한 문장입니다.']
    
    for p in pipe(textline)[0]:
        for key, value in p.items():
            if key == 'score':
                if score < value:
                    score = value
                    index = i
        i += 1            
    
    
    problemlist= [textlist,reasonlist[index]]
    return problemlist

def sendServer(problemlist):
    pass



