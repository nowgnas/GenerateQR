from PIL import Image
import qrcode
import pandas as pd

UserData = pd.read_excel('../data/tave_member.xlsx')

for _iter in UserData.iterrows():
    print(_iter[1]['phone'])
    generation = _iter[1]['gen']
    UserName = _iter[1]['name']
    UserPhone = _iter[1]['phone']
    UserDataString = f'gen: {generation} name: {UserName} phone: {UserPhone}'

    QRGeneration = qrcode.make(UserDataString)
    QRGeneration.save(f'../data/qrImg/usr_qrCode/{UserName}.png')
