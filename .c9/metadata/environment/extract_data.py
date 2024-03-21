{"filter":false,"title":"extract_data.py","tooltip":"/extract_data.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":110,"column":19},"action":"insert","lines":["import boto3","from datetime import datetime","from bs4 import BeautifulSoup","import pandas as pd","","","def extract_data(html_content):","    \"\"\"","    Función para extraer el precio, metraje,","    número de habitaciones y características","    adicionales de las páginas HTML.","    \"\"\"","    soup = BeautifulSoup(html_content, 'html.parser')","    # print(\"HTML:     \",soup)","    properties = soup.find_all('div', class_='listing-card__information')","    # print(\"PROPERTIES: \",properties)","    data = []","","    for prop in properties:","","        price = prop.find('div', class_='price').text.strip()","        area_div = prop.find('div', class_='card-icon card-icon__area')","        area_span = None","        if area_div:","            area_span = area_div.find_next('span')","        area = area_span.text.strip() if area_span else \"No disponible\"","        bedrooms_element = prop.find('span', attrs={'data-test': 'bedrooms'})","","        if bedrooms_element:","            bedrooms = bedrooms_element.text.strip()","        else:","            bedrooms = 'No disponible'","        adicional = prop.find('span', class_='facility-item__text')","","        if adicional:","            adicional_text = adicional.text.strip()","        else:","            adicional_text = 'No disponible'","","        data.append([price, area, bedrooms, adicional_text])","        # print(data)","","    return data","","","def handler(event, context):","    \"\"\"","    Función para procesar los datos descargados","    y guardarlos en un archivo CSV en AWS S3.","    \"\"\"","    s3 = boto3.client('s3')","    bucket_name = 'parcial18032024'","","    # Obtener la fecha actual","    current_date = datetime.now().strftime('%Y-%m-%d')","","    # Obtener la lista de objetos en el bucket","    response = s3.list_objects(Bucket=bucket_name)","    all_data = []","","    # for obj in response.get('Contents', []):","    if 'Contents' in response:","        for obj in response['Contents']:","            # Obtener el contenido de cada objeto","            response_obj = s3.get_object(Bucket=bucket_name, Key=obj['Key'])","            html_content = response_obj['Body'].read()","","            # Extraer los datos de la página HTML y agregarlos a la lista","            data = extract_data(html_content)","            all_data.extend(data)","","    # Crear un DataFrame pandas con todos los datos recolectados","    df = pd.DataFrame(","        all_data,","        columns=[","            'Price',","            'Area',","            'Bedrooms',","            'Adicional'])","","    df['Price'] = pd.to_numeric(","        df['Price'].str.replace(","            '[$,.]',","            '',","            regex=True),","        errors='coerce')","    df['Price'] = df['Price'].astype('Int64')  # Convertir a tipo Int64","","    df['Bedrooms'] = pd.to_numeric(","        df['Bedrooms'].str.split(' ').str[0],","        errors='coerce')","","    df['Area'] = df['Area'].str.extract(r'(\\d+)').astype(float)","    # df['Area'] = df['Area'].apply(lambda x: '{:.0f} m²'.format(x))  #","    # Agregar el sufijo 'm²'","","    # Guardar el DataFrame como archivo CSV en S3","    csv_key = (f'casas/year={current_date[:4]}/'","               f'month={current_date[5:7]}/'","               f'day={current_date[8:]}/'","               f'{current_date}.csv')","    csv_buffer = df.to_csv(index=False)","    s3.put_object(Body=csv_buffer, Bucket='parcialfinal18032024', Key=csv_key)","","    return {","        'statusCode': 200,","        'body': 'Datos procesados y guardados en S3 correctamente.'","    }","","","handler(None, None)"],"id":1}],[{"start":{"row":102,"column":43},"end":{"row":102,"column":63},"action":"remove","lines":["parcialfinal18032024"],"id":3},{"start":{"row":102,"column":43},"end":{"row":102,"column":44},"action":"insert","lines":["b"]},{"start":{"row":102,"column":44},"end":{"row":102,"column":45},"action":"insert","lines":["u"]},{"start":{"row":102,"column":45},"end":{"row":102,"column":46},"action":"insert","lines":["c"]},{"start":{"row":102,"column":46},"end":{"row":102,"column":47},"action":"insert","lines":["k"]},{"start":{"row":102,"column":47},"end":{"row":102,"column":48},"action":"insert","lines":["e"]},{"start":{"row":102,"column":48},"end":{"row":102,"column":49},"action":"insert","lines":["t"]},{"start":{"row":102,"column":49},"end":{"row":102,"column":50},"action":"insert","lines":["p"]},{"start":{"row":102,"column":50},"end":{"row":102,"column":51},"action":"insert","lines":["a"]},{"start":{"row":102,"column":51},"end":{"row":102,"column":52},"action":"insert","lines":["r"]},{"start":{"row":102,"column":52},"end":{"row":102,"column":53},"action":"insert","lines":["c"]},{"start":{"row":102,"column":53},"end":{"row":102,"column":54},"action":"insert","lines":["i"]},{"start":{"row":102,"column":54},"end":{"row":102,"column":55},"action":"insert","lines":["a"]},{"start":{"row":102,"column":55},"end":{"row":102,"column":56},"action":"insert","lines":["l"]}],[{"start":{"row":51,"column":19},"end":{"row":51,"column":34},"action":"remove","lines":["parcial18032024"],"id":4},{"start":{"row":51,"column":19},"end":{"row":51,"column":20},"action":"insert","lines":["b"]},{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"insert","lines":["u"]},{"start":{"row":51,"column":21},"end":{"row":51,"column":22},"action":"insert","lines":["c"]},{"start":{"row":51,"column":22},"end":{"row":51,"column":23},"action":"insert","lines":["k"]},{"start":{"row":51,"column":23},"end":{"row":51,"column":24},"action":"insert","lines":["e"]},{"start":{"row":51,"column":24},"end":{"row":51,"column":25},"action":"insert","lines":["t"]},{"start":{"row":51,"column":25},"end":{"row":51,"column":26},"action":"insert","lines":["."]},{"start":{"row":51,"column":26},"end":{"row":51,"column":27},"action":"insert","lines":["p"]},{"start":{"row":51,"column":27},"end":{"row":51,"column":28},"action":"insert","lines":["a"]},{"start":{"row":51,"column":28},"end":{"row":51,"column":29},"action":"insert","lines":["r"]}],[{"start":{"row":51,"column":28},"end":{"row":51,"column":29},"action":"remove","lines":["r"],"id":5},{"start":{"row":51,"column":27},"end":{"row":51,"column":28},"action":"remove","lines":["a"]},{"start":{"row":51,"column":26},"end":{"row":51,"column":27},"action":"remove","lines":["p"]},{"start":{"row":51,"column":25},"end":{"row":51,"column":26},"action":"remove","lines":["."]}],[{"start":{"row":51,"column":25},"end":{"row":51,"column":26},"action":"insert","lines":["."],"id":6},{"start":{"row":51,"column":26},"end":{"row":51,"column":27},"action":"insert","lines":["p"]}],[{"start":{"row":51,"column":26},"end":{"row":51,"column":27},"action":"remove","lines":["p"],"id":7},{"start":{"row":51,"column":25},"end":{"row":51,"column":26},"action":"remove","lines":["."]}],[{"start":{"row":51,"column":25},"end":{"row":51,"column":26},"action":"insert","lines":["-"],"id":8},{"start":{"row":51,"column":26},"end":{"row":51,"column":27},"action":"insert","lines":["p"]},{"start":{"row":51,"column":27},"end":{"row":51,"column":28},"action":"insert","lines":["a"]},{"start":{"row":51,"column":28},"end":{"row":51,"column":29},"action":"insert","lines":["r"]},{"start":{"row":51,"column":29},"end":{"row":51,"column":30},"action":"insert","lines":["c"]},{"start":{"row":51,"column":30},"end":{"row":51,"column":31},"action":"insert","lines":["i"]},{"start":{"row":51,"column":31},"end":{"row":51,"column":32},"action":"insert","lines":["a"]},{"start":{"row":51,"column":32},"end":{"row":51,"column":33},"action":"insert","lines":["l"]}],[{"start":{"row":7,"column":0},"end":{"row":11,"column":7},"action":"remove","lines":["    \"\"\"","    Función para extraer el precio, metraje,","    número de habitaciones y características","    adicionales de las páginas HTML.","    \"\"\""],"id":9}],[{"start":{"row":6,"column":31},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":10}],[{"start":{"row":6,"column":31},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":3},"end":{"row":45,"column":7},"action":"remove","lines":[" \"\"\"","    Función para procesar los datos descargados","    y guardarlos en un archivo CSV en AWS S3.","    \"\"\""],"id":12}],[{"start":{"row":6,"column":31},"end":{"row":7,"column":4},"action":"remove","lines":["","    "],"id":13}],[{"start":{"row":6,"column":31},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"insert","lines":["    "],"id":15}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "],"id":16}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":17}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":18}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":19}],[{"start":{"row":6,"column":31},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":20}],[{"start":{"row":6,"column":31},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"insert","lines":["    "],"id":22}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":23}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "],"id":24},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":26}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":[" "],"id":27},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":[" "]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":[" "]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":12},"action":"insert","lines":["    "],"id":37}],[{"start":{"row":22,"column":6},"end":{"row":22,"column":8},"action":"insert","lines":["  "],"id":38}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"insert","lines":["    "],"id":39}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"remove","lines":["    "],"id":40}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"remove","lines":[" "],"id":41},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"insert","lines":["    "],"id":42}],[{"start":{"row":28,"column":8},"end":{"row":28,"column":12},"action":"insert","lines":["    "],"id":43}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":12},"action":"insert","lines":["    "],"id":44}]]},"ace":{"folds":[],"scrolltop":1143,"scrollleft":0,"selection":{"start":{"row":98,"column":26},"end":{"row":98,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":80,"state":"start","mode":"ace/mode/python"}},"timestamp":1711040545660,"hash":"13a31bd4d542d50598888c722b35f9e0d1bf3726"}