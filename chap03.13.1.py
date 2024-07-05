#시계열 데이터 다루기
#시계열 데이터란(time series data) 시간을 기준으로 측정된 자료를 말하며,
#주가나 제무제표 등 투자에 쓰이는 대부분의 데이터가 시계열 데이터라고 볼 수 있기 때문이다.


import seaborn as sns
import pandas as pd
import numpy as np


df = sns.load_dataset('taxis')
print(df.head())
print()
print()

#'pickup' 과 'dropoff' 열을 살펴보면 시계열 형태처럼 보인다.

print(df.info())
print()
print()

#pandas 에서는 to_datetime() 메서드를 통해
#문자열을 datetime 객체로 변환할 수 있다.

df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])

print(df.info())
#두 열의 타입이 'datetime64[ns]', 즉 datetime64 객체로 변하였다.
print()
print()

#원소의 끝에 year를 붙여주면 연도에 해당하는 값이 추출된다.

print(df['pickup'][0].year)
print()
print()

#dt 접근자를 사용하면 datetime  타입의 열에 한 번에 접근할 수 있다.

df['year'] = df['pickup'].dt.year
df['month'] = df['pickup'].dt.month
df['day'] = df['pickup'].dt.day

print(df[['pickup', 'year', 'month', 'day']].head())
#먼저, 열을 의미하는 df['pickup'] 뒤에 dt 접근자를 붙여준 후,
#추출하고자 하는 정보(year, month, day)를 입력한다.
#그 결과, 연, 월, 일에 해당하는 정보만이 추출되었다.

print()
print()

#현재는 데이터가 시간 순서대로 정렬되어 있지 않으므로
#'pickup' 열을 기준으로 정렬을 해주도록 한다.

df.sort_values('pickup', inplace=True)
#sort_values() 메서드를 통해 'pickup' 열을 기준으로 데이터를 오름차순으로 정렬한다.

df.reset_index(drop=True, inplace=True)
#reset_index() 메서드를 통해 행 인덱스를 초기화한다.

print(df.head())
print()
print()

#이번에는 'pickup' 열과 'dropoff' 열의 차이, 즉 운행 시간을 계산해 보자

print(df['dropoff'] - df['pickup'])
print()
print()


#이번에는 'pickup' 열을 행 인덱스로 변경해보자

df.set_index('pickup', inplace=True)

print(df.head())
print()
print()

#인덱스가 'DatetimeIndex' 형태라는 것을 알 수 있다.

print(df.index)
print()
print()

#2019년 2월에 해당하는 정보만 선택해 보자

print(df.loc['2019-02'])
print()
print()


#이번에는 2019년 3월 1일부터 3월 2일까지의 데이터를 선택해보자

print(df.loc['2019-03-01':'2019-03-02'])
print()
print()


#시계열 데이터 만들기
#pandas의 date_range() 함수를 통해 여러 개의 날짜가 들어있는
#배열 형태의 시계열 데이터를 만들 수 있다.

print(pd.date_range(start='2021-01-01', end='2021-12-31', freq='ME'))
print()
print()


#3D 는 3일을 뜻한다. 즉 2021년 1월 1일 부터 3일 주기의 시계열 데이터가 만들어진다.

print(pd.date_range(start='2021-01-01', end='2021-01-31', freq='3D'))
print()
print()


#W는 주를 뜻하고 MON는 월요일을 뜻한다. 즉 매주 월요일에 해당하는 날짜가
#시계열 데이터로 만들어진다.

print(pd.date_range(start='2021-01-01', end='2021-01-31', freq='W-MON'))
print()
print()


#WOM 는 week of month를 , 2THU 는 둘째 주 목요일을 뜻한다.
#WOM-2FRI 는 매일 둘째 주 목요일에 해당하는 날짜가 시계열 데이터로 만들어진다.

print(pd.date_range(start='2021-01-01', end='2021-12-31', freq='WOM-2THU'))
print()
print()






