import pytesseract
from PIL import Image
import pandas as pd
import streamlit as st
import re

#b_p = st.sidebar.selectbox('Batter or Pichter', ['Batter'])
b_p = st.sidebar.selectbox('Batter or Pichter', ['Batter', 'Pichter'])
photo = st.file_uploader('Upload a photo')
photo_2 = st.file_uploader('Upload another photo')

if photo and b_p == 'Batter':
    img = Image.open(photo)
    img = img.resize((3600, 1200))
    strings_list = pytesseract.image_to_string(img, config='--psm 6').split("'")
    df = pd.DataFrame(columns = ['NAME', 'AB', 'AVG', 'H', "HR", 'RBI', 'R', 'SB', 'OBP'])
    row = 0
    for i, stat in enumerate(strings_list):
        if i > 0:
            stats = stat.replace('\n', ' ').split(' ')
            if float(stats[2]) > 1:
                stats[2] = str(float(stats[2]) / 1000)
            else:
                stats[2] = str(float(stats[2]))
            if float(stats[8]) > 1:
                stats[8] = str(float(stats[8]) / 1000)
            else:
                stats[8] = str(float(stats[8]))
            df.loc[row] = [
                (re.findall(r'[A-Z]\.[A-Z][a-z-. ]*[A-Za-z]*', strings_list[i-1])[-1] + "'" + stats[0]).replace(' ',''),
                stats[1],
                stats[2],
                stats[3],
                stats[4],
                stats[5],
                stats[6],
                stats[7],
                stats[8]
            ]
            row += 1
    if photo_2:
        img_2 = Image.open(photo_2)
        img_2 = img_2.resize((3600, 1200))
        strings_list_2 = pytesseract.image_to_string(img_2, config='--psm 6').split("'")
        for i, stat in enumerate(strings_list_2):
            if i > 0:
                stats = stat.replace('\n', ' ').split(' ')
                if float(stats[2]) > 1:
                    stats[2] = str(float(stats[2]) / 1000)
                else:
                    stats[2] = str(float(stats[2]))
                if float(stats[8]) > 1:
                    stats[8] = str(float(stats[8]) / 1000)
                else:
                    stats[8] = str(float(stats[8]))
                df.loc[row] = [
                    (re.findall(r'[A-Z]\.[A-Z][a-z-. ]*[A-Za-z]*', strings_list_2[i-1])[-1] + "'" + stats[0]).replace(' ',''),
                    stats[1],
                    stats[2],
                    stats[3],
                    stats[4],
                    stats[5],
                    stats[6],
                    stats[7],
                    stats[8]
                ]
                row += 1
    df = df.drop_duplicates(subset=['NAME'])
    st.write(df)
    cols = ' '.join(df.columns)
    df[cols] = df.apply(' '.join, axis=1)
    df[len(df)] = ['NAME', 'AB', 'AVG', 'H', "HR", 'RBI', 'R', 'SB', 'OBP', cols]
    st.write(df.cols)
elif photo and b_p == 'Pichter':
    img = Image.open(photo)
    img = img.resize((2000, 900))
    strings_list = pytesseract.image_to_string(img, config='--psm 6').split("'")
    df = pd.DataFrame(columns = ['NAME', 'IP', 'ERA', 'W', "L", 'SV', 'SO', 'BB', 'WHIP'])
    row = 0
    for i, stat in enumerate(strings_list):
        if i > 0:
            #name = strings_list[i-1].replace('\n', ' ').split(' ')
            stats = stat.replace('\n', ' ').split(' ')
            if float(stats[2]) > 50:
                stats[2] = str(float(stats[2]) / 100)
            else:
                stats[2] = str(float(stats[2]))
            if float(stats[8]) > 1:
                stats[8] = str(float(stats[8]) / 100)
            else:
                stats[8] = str(float(stats[8]))
            df.loc[row] = [
                re.findall(r'[A-Z]\.[A-Z][a-z-. ]*[A-Za-z]*', strings_list[i-1])[-1] + "'" + stats[0],
                stats[1],
                stats[2],
                stats[3],
                stats[4],
                stats[5],
                stats[6],
                stats[7],
                stats[8]
            ]
            row += 1
    if photo_2:
        img_2 = Image.open(photo_2)
        img_2 = img_2.resize((2000, 900))
        strings_list_2 = pytesseract.image_to_string(img_2, config='--psm 6').split("'")
        for i, stat in enumerate(strings_list_2):
            if i > 0:
                stats = stat.replace('\n', ' ').split(' ')
                if float(stats[2]) > 1:
                    stats[2] = str(float(stats[2]) / 1000)
                else:
                    stats[2] = str(float(stats[2]))
                if float(stats[8]) > 1:
                    stats[8] = str(float(stats[8]) / 1000)
                else:
                    stats[8] = str(float(stats[8]))
                df.loc[row] = [
                    re.findall(r'[A-Z]\.[A-Z][a-z-. ]*[A-Za-z]*', strings_list_2[i-1])[-1] + "'" + stats[0],
                    stats[1],
                    stats[2],
                    stats[3],
                    stats[4],
                    stats[5],
                    stats[6],
                    stats[7],
                    stats[8]
                ]
                row += 1
    st.write(df.drop_duplicates(subset=['NAME']))






