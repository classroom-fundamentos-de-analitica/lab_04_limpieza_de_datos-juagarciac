"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def limpiar_monto(monto):
    monto = monto.replace("$", "").replace(".", "").replace(",", "")
    return monto

def limpiar_fecha(entrada):
    fecha = entrada.split("/")
    if(len(fecha[0]) > 2):
        return fecha[2] + "/" + fecha[1] + "/" + fecha[0]
    else:
        return entrada
    
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.drop_duplicates().drop(df.columns[0], axis=1)
    df = df.dropna()
    df["monto_del_credito"] = df["monto_del_credito"].apply(limpiar_monto)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(limpiar_fecha)
    return df

print(clean_data())