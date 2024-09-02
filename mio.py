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
    
def limpiar_idea(entrada):
    entrada = entrada.replace("_", " ").replace(".", "").replace(",", "").lower()
    return entrada
    
def clean_data():
    def limpieza_sexo(df):
        df = df.copy()
        df.sexo = df.sexo.str.lower()
        return df

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.replace("-", " ", regex=True).replace("_", " ", regex=True)
    df = limpieza_sexo(df)
    #df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x: x.lower())
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: limpiar_idea(x))
    df["monto_del_credito"] = df["monto_del_credito"].apply(limpiar_monto)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(limpiar_fecha)
    return df

print(clean_data().sexo.value_counts().to_list() )