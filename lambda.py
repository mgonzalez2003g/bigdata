import requests
import boto3
from datetime import datetime, timedelta

def descargar_pagina(url):
    # Realizar la solicitud HTTP para descargar la página
    response = requests.get(url)
    # Retornar el contenido de la página
    return response.content

def cargar_archivo_en_s3(bucket_name, file_key, file_content):
    # Crear un cliente de S3
    s3_client = boto3.client('s3')
    # Cargar el contenido del archivo en el bucket de S3
    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)

def descargarCasas_handler(event, context):
    # Lista de enlaces de las categorías del sitio web
    links_categorias = [
        "https://casas.mitula.com.co/casas/arriendo-locales-medellin",
        "https://casas.mitula.com.co/casas/apartamentos-ceja",
        "https://casas.mitula.com.co/casas/casas-armenia",
        "https://casas.mitula.com.co/casas/casas-mosquera",
        "https://casas.mitula.com.co/casas/arriendo-casas-floridablanca"
        
    ]
    
    # Nombre del bucket de S3
    bucket_name = "bucket-parcial"
    
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    # Iterar sobre los enlaces de las categorías
    for i, link_categoria in enumerate(links_categorias, start=1):
        # Descargar la página
        contenido_pagina = descargar_pagina(link_categoria)
        # Construir la clave del archivo en S3
        file_key = f"casas/contenido-categoria-{i}-{fecha_actual.strftime('%Y-%m-%d')}.html"
        # Cargar el contenido en S3
        cargar_archivo_en_s3(bucket_name, file_key, contenido_pagina)
    
    return {
        'statusCode': 200,
        'body': 'Archivos descargados y almacenados en S3 correctamente.'
    }
