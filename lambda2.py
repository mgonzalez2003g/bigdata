import boto3
import csv
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def lambda_handler(event, context):
    # Obtener la URL del archivo desde el evento
    file_url = event['file_url']
    
    # Descargar el archivo
    response = requests.get(file_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Procesar los datos con Beautifulsoup
    # Supongamos que aquí se extraen los datos necesarios
    
    # Datos de ejemplo
    price = "$100,000"
    area = "200 sqft"
    rooms = "3"
    additional_features = "Garden, Pool"
    
    # Crear un archivo CSV con los datos procesados
    csv_data = [
        ['price', 'area', 'rooms', 'additional_features'],
        [price, area, rooms, additional_features]
    ]
    
    # Crear el nombre del archivo
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    file_name = f"{year}-{month:02d}-{day:02d}.csv"
    
    # Guardar el archivo CSV en S3
    s3 = boto3.client('s3')
    bucket_name = 'bucket-final'
    key = f"casas/year={year}/month={month}/day={day}/{file_name}"
    s3.put_object(Body=csv_data, Bucket=bucket_name, Key=key)
    
    return {
        'statusCode': 200,
        'body': 'Procesamiento completado'
    }
