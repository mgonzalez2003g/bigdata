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
    # URL base del sitio web
    base_url = "https://casas.mitula.com.co/"
    # Nombre del bucket de S3
    bucket_name = "bucket-parcial"
    
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    # Iterar sobre las 5 primeras páginas del sitio web
    for i in range(1, 6):
        # Construir la URL de la página actual
        url_pagina = f"{base_url}?page={i}"
        # Descargar la página
        contenido_pagina = descargar_pagina(url_pagina)
        # Construir la clave del archivo en S3
        file_key = f"casas/contenido-pag-{i}-{fecha_actual.strftime('%Y-%m-%d')}.html"
        # Cargar el contenido en S3
        cargar_archivo_en_s3(bucket_name, file_key, contenido_pagina)
    
    return {
        'statusCode': 200,
        'body': 'Archivos descargados y almacenados en S3 correctamente.'
    }
