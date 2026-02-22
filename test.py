import pandas as pd

# 모든 행/열 다 보이게 설정
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 엑셀 파일 읽기
file_path = "sample.xlsx"   # 네 엑셀 파일 이름으로 수정

df = pd.read_excel(file_path)

# 데이터 출력
print("=== 엑셀 내용 ===")
print(df)

# 첫 행만 확인
print("\n=== 첫 행 ===")
print(df.head(1))