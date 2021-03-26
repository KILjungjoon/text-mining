# 라이브러리 임포트하기

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import DataFrame

# 사이킷런의 CountVectorizer 를 통해 벡터화하기
    
def creat_document_term_matrix(message_list, vectorizer):
    doc_term_matrix=vectorizer.fit_transform(message_list)
    return DataFrame(doc_term_matrix.toarray(),
                     columns=vectorizer.get_feature_names())
    
count_vect = CountVectorizer()

# 엑셀 파일 불러오기
df=pd.read_excel('filename.xlsx', header=0, names=None)
df.head()

# 형태소 dtm 행렬 만들기
df_dtm=pd.DataFrame(creat_document_term_matrix(df['형태소'], count_vect))
df_dtm.head(10)

# 저장
df_dtm.to_excel('filename_morph.xlsx',encoding='utf-8')