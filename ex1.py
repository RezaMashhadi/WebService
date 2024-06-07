import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

# https://docs.google.com/spreadsheets/d/1_HyKlK8Kxfs5ZJcDKUIHacxByjsTkBbnOIR2H33XYdU/edit#gid=0

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
cd = {
    "type": "service_account",
    "project_id": "python-6b6e1",
    "private_key_id": "f3fbb7bf49d263d1d18ca3449fab3ff26a1c541d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmLjJhNnGE6+cj\ntWNsaAC33rv1SRHxf5R3MIdJI6PmfBsFNwmpvwcdSyuGGCcYg4asWoljP2PT6aQX\n3Rqh0HLq3B2Xhdrv7olNmMLDfi/MBXkBZ2Fen802zZ5Kn4lcFMCEvaT8OluhFpq6\nhOcvvS+T7F+fae9AQbEYMQSwuUdiUlBNFqd8uDc3CTk/2O372uKZrrQUDvMUEllw\nQWTLLDPQdFZswxxyyUmue/hzhlBPeccvKKfhOFKKca/i8RhGULH+USR9pBID66/I\nVXIWj8wArIjr5YoFUFFEPKy53EXbgB2FJJGHg3o/3eZNOSTwZZhZKG4aRQA2ex/9\nzjOAQr9FAgMBAAECggEAEHuGBzLbdRPh396SnzK8mYAn0+cctr+Q9fZ0AKrei5KV\nKoIAPRwjpEHrrffwzsNi5O7w8A1eRStIGY7WYKTYdReCfuAprEEUUMQ9Ux8NthZ3\n304F8Bj5BX3E/MFQojeztabKubK/Gl3v2F6swIUq9ijMfjcHYi/x1QStoqqp3CRF\nbn6UK+je+W46xr9zn0we0EtsgpNaTPSaB/fceU++EqF3tmsCSmHz0+TO2pSvZ5j2\nRHVSBh73AF9jfo1J7TJDcZxa4gyuygG9iKgTtSMMPHn1ID/5zOMq4IJSB4auDM/H\nDMYfHyA1SZ8mcgskByWlKqcgVL+2Gqv15inBe4mAQQKBgQDcKKB5Qo236tUYsLYb\nDLMyXd2FTAIg+N4IOzSajBWN0yyW6iL5goT388TZ9FYkW+H9w//zjXG5FceMHlZj\nWstLrpylkOoFEVS9KfvZPwfGCUM5K732R3Io9SlvCUdjHCR0RqzOfmmkv7aubXn8\nPAzboaMiYnhirmCbuWIlSuI8QQKBgQDBO/aNmAYrwRWqgljkaRXc+ej1SDpQJktn\n9UNvtS4V/XS1xvxiF/cevoAmd2iRoKhIphops3ehqeUrng6LCWK8rHDEV1gU5UHe\naMPRkJonhRgjkH897mijQYeJqnMDZXuWKS8xWQQUBykx0jIObzjz12tXyzameenM\nBzv+FtsSBQKBgG/PolBzYI47kaZMePAb7xZxXYPJKnucaQc9KmYjJv80dLzghIq7\notRa1WrsEKO+lnPPCzqiZ1NcoE+lSLKE9iKlt6DOjEuulZ7Mp7+Zp1UIdz+d24gs\nmOn8OOLPj5XiQRFco37r7LNjOmAz8XQM+2rAGJ3p7MIRVbdA23udIHEBAoGAIWsD\nWr1947dCzfg481eRJmQ5+6GAJDhbNiFehkUpMThiJMXDBBvs6u47L2vbM8Q7FkVT\npP6ao+TD82UkUrtOzh5saihI3WRAnfw0UVvWrRsBb7UfrFA83G8Kx64osd+tHe0F\ncl1YrTYH08vsSD7H9LO+prJIQ0Y2PsjJgUnmnRkCgYEAq0W9ZCkeGSWH1Pvl3+GP\nd0vaTn/p9BhEpCEsWsK8D19IJii4XsWIyp3dqxeL48C9w+GltQpBYXHpI3cRdIlP\ndDaeZqJ5zSGK9nUdiqikCpCqY2H093yAHYqZgMiP58P8vKwIeAXwhTaGC/RmJKyS\nH3auTdNJg8kag0BUkOBMtF8=\n-----END PRIVATE KEY-----\n",
    "client_email": "reza-113@python-6b6e1.iam.gserviceaccount.com",
    "client_id": "106170095129431998482",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/reza-113%40python-6b6e1.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
with open('credentials.json', 'w') as outfile:
    json.dump(cd, outfile)
credentials = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(credentials)
sheet = client.open_by_key('1_HyKlK8Kxfs5ZJcDKUIHacxByjsTkBbnOIR2H33XYdU').sheet1

st.title("نظرسنجی محصول/خدمات")

name = st.text_input("نام شما:")
email = st.text_input("ایمیل شما:")
rating = st.selectbox("امتیاز محصول/خدمات:", [1, 2, 3, 4, 5])
feedback = st.text_area("بازخورد خود را بنویسید:")

if st.button("ارسال نظرسنجی"):
    new_row = [name, email, rating, feedback]
    sheet.append_row(new_row)
    st.success("با تشکر از نظرسنجی شما!")

existing_data = sheet.get_all_values()
data_df = pd.DataFrame(existing_data[1:], columns=existing_data[0])

st.subheader("Vote Result")
st.write(data_df[['Name', 'Email', 'Rating', 'Suggest']])

st.subheader("Rating Distribution")
rating_counts = data_df['Rating'].value_counts().sort_index()
st.bar_chart(rating_counts)