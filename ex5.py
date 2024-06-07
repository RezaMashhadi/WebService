import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

# https://docs.google.com/spreadsheets/d/1nlsvVyRUH_qZWXWZtXZFtJsyqyE6YqhgwStFicyw6Xo/edit#gid=0

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
credentials = Credentials.from_service_account_file('credentials.json', scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credentials)

sheet = client.open_by_key('1nlsvVyRUH_qZWXWZtXZFtJsyqyE6YqhgwStFicyw6Xo').sheet1

event_data = {
    "Name": [],
    "Email": [],
    "Phone Number": [],
    "Organization": [],
    "Registration Date": []
}

def save_registration(name, email, phone_number, organization, registration_date):
    new_row = [name, email, phone_number, organization, registration_date]
    sheet.append_row(new_row)

def get_all_registrations():
    all_data = sheet.get_all_values()
    if not all_data:
        return pd.DataFrame(columns=["Name", "Email", "Phone Number", "Organization", "Registration Date"])
    df = pd.DataFrame(all_data[1:], columns=["Name", "Email", "Phone Number", "Organization", "Registration Date"])
    return df
def get_registrations_by_event(event_name):
    all_registrations = get_all_registrations()
    filtered_registrations = all_registrations[all_registrations["Event Name"] == event_name]
    return filtered_registrations
def analyze_registrations(df):
    org_counts = df['Organization'].value_counts()
    st.bar_chart(org_counts)
    reg_date_counts = df['Registration Date'].value_counts()
    st.line_chart(reg_date_counts)

st.title("ثبت نام رویداد")

st.header("ثبت نام در رویداد")
event_name = st.text_input("نام رویداد:")
name = st.text_input("نام:")
email = st.text_input("ایمیل:")
phone_number = st.text_input("شماره تلفن:")
organization = st.text_input("سازمان:")
registration_date = st.date_input("تاریخ ثبت نام:")
register_button = st.button("ثبت نام")

if register_button:
    if event_name and name and email and phone_number and organization and registration_date:
        event_data["Name"].append(name)
        event_data["Email"].append(email)
        event_data["Phone Number"].append(phone_number)
        event_data["Organization"].append(organization)
        event_data["Registration Date"].append(registration_date.strftime("%Y-%m-%d"))
        save_registration(name, email, phone_number, organization, registration_date.strftime("%Y-%m-%d"))
        st.success("با موفقیت ثبت نام شد!")
    else:
        st.error("لطفا تمام فیلدهای مورد نیاز را پر کنید.")

st.header("لیست ثبت نام شدگان")
all_registrations_df = get_all_registrations()
st.write(all_registrations_df)

st.header("تحلیل داده های ثبت نام")
analyze_registrations(all_registrations_df)