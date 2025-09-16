import pandas as pd

# Excel 파일 읽기 (첫 번째 행을 헤더로 사용)
df = pd.read_excel(r"C:\202525014 송영주\data.xlsx", header=1)

# 첫 번째 컬럼(Unnamed: 0) 제거
df = df.drop(df.columns[0], axis=1)

print("컬럼명:", list(df.columns))
print("\n데이터:")
print(df)

# 평균 계산
df['평균'] = (df['영어'] + df['국어'] + df['수학']) / 3

print("\n평균 계산 결과:")
print(df)