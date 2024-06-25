import pandas as pd
import streamlit as st
import plotly.express as px
from credsGoogleSheetsApi import ConnectGoogleSheetsApi

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

conn = ConnectGoogleSheetsApi()
conn.connect()


st.set_page_config(
    layout="wide", 
    page_title="Apontamento de horas TCS"
)


def getSheetsValues(conn):
    try:
        service = build('sheets', 'v4', credentials=conn.creds)
        sheet = service.spreadsheets()
        result = (sheet.values().get(spreadsheetId="1dkKQhT6rHWm8Xvz-qN9B9zm3kspugkUYceU8qACDJHI", range="DB1!A1:F82").execute())
        return result

    except HttpError as err:
        print(err)


st.title("Apontamento de horas do TCS - BI")

response = getSheetsValues(conn)

if st.button("Atualizar"):
    response = getSheetsValues(conn)
st.divider()


df = pd.DataFrame(response['values'][1:], columns=response['values'][0])
df["Carimbo de data/hora"] = pd.to_datetime(df["Carimbo de data/hora"])
df["MES"] = df["Carimbo de data/hora"].apply(lambda x: x.month)
st.metric("Total de horas", f"{df['Total de horas'][0]}")

df['Horas trabalhas no TCS'] = df['Horas trabalhas no TCS'].astype(int)
df_filtred = df.groupby("MES")["Horas trabalhas no TCS"].sum()
df_filtred = pd.DataFrame(df_filtred)
df_filtred["MES"] = df_filtred.index
df_filtred.index.name = "Indice"
fig_total_project = px.bar(df_filtred, x="MES", y="Horas trabalhas no TCS", title="Horas trabalhadas por mês")
st.plotly_chart(fig_total_project, use_container_width=True)

col1, col2 = st.columns(2)
fig_total_project = px.pie(df, values="Horas trabalhas no TCS", names="No que trabalhou?", title="No que essas horas foram gastas?")
col1.plotly_chart(fig_total_project, use_container_width=True)
fig_total_hours = px.pie(df, values="Horas trabalhas no TCS", names="Estudante", title="Horas trabalhadas por estudante")
col2.plotly_chart(fig_total_hours, use_container_width=True)