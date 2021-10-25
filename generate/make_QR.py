import pandas as pd
import qrcode

UserData = pd.read_excel('../data/tave_member.xlsx')

for _iter in UserData.iterrows():
    generation = _iter[1]['gen']
    UserName = _iter[1]['name']
    UserPhone = _iter[1].iloc[2]
    UserDataString = f'gen: {generation} name: {UserName} phone: 0{UserPhone}'
    QRGeneration = qrcode.make(UserDataString)
    QRGeneration.save(f'../data/qrImg/usr_qrCode/{UserName}.png')
# 소켓 통신 한번 시도해보기
