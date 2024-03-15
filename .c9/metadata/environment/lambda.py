{"changed":true,"filter":false,"title":"lambda.py","tooltip":"/lambda.py","value":"import requests\nimport boto3\nfrom datetime import datetime, timedelta\n\ndef descargar_pagina(url):\n    # Realizar la solicitud HTTP para descargar la página\n    response = requests.get(url)\n    # Retornar el contenido de la página\n    return response.content\n\ndef cargar_archivo_en_s3(bucket_name, file_key, file_content):\n    # Crear un cliente de S3\n    s3_client = boto3.client('s3')\n    # Cargar el contenido del archivo en el bucket de S3\n    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)\n\ndef descargarCasas_handler(event, context):\n    # URL base del sitio web\n    base_url = \"https://casas.mitula.com.co/\"\n    # Nombre del bucket de S3\n    bucket_name = \"bucket-parcial\"\n    \n    # Obtener la fecha actual\n    fecha_actual = datetime.now()\n    \n    # Iterar sobre las 5 primeras páginas del sitio web\n    for i in range(1, 6):\n        # Construir la URL de la página actual\n        url_pagina = f\"{base_url}?page={i}\"\n        # Descargar la página\n        contenido_pagina = descargar_pagina(url_pagina)\n        # Construir la clave del archivo en S3\n        file_key = f\"casas/contenido-pag-{i}-{fecha_actual.strftime('%Y-%m-%d')}.html\"\n        # Cargar el contenido en S3\n        cargar_archivo_en_s3(bucket_name, file_key, contenido_pagina)\n    \n    return {\n        'statusCode': 200,\n        'body': 'Archivos descargados y almacenados en S3 correctamente.'\n    }\n","undoManager":{"mark":2,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["a",""],"id":4},{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["import requests","import boto3","","def descargar_pagina(url):","    # Realizar la solicitud HTTP para descargar la página","    response = requests.get(url)","    # Retornar el contenido de la página","    return response.content","","def cargar_archivo_en_s3(bucket_name, file_key, file_content):","    # Crear un cliente de S3","    s3_client = boto3.client('s3')","    # Cargar el contenido del archivo en el bucket de S3","    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)","","# URL de la página a descargar","url = 'https://casas.mitula.com.co/'","# Nombre del bucket de S3","bucket_name = 'bucket-raw'","# Nombre del archivo en S3","file_key = 'casas/contenido-pag-x-yyyy-mm-dd.html'","","# Descargar la página","contenido_pagina = descargar_pagina(url)","# Cargar el contenido en S3","cargar_archivo_en_s3(bucket_name, file_key, contenido_pagina)",""]}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["import requests","import boto3","","def descargar_pagina(url):","    # Realizar la solicitud HTTP para descargar la página","    response = requests.get(url)","    # Retornar el contenido de la página","    return response.content","","def cargar_archivo_en_s3(bucket_name, file_key, file_content):","    # Crear un cliente de S3","    s3_client = boto3.client('s3')","    # Cargar el contenido del archivo en el bucket de S3","    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)","","# URL de la página a descargar","url = 'https://casas.mitula.com.co/'","# Nombre del bucket de S3","bucket_name = 'bucket-raw'","# Nombre del archivo en S3","file_key = 'casas/contenido-pag-x-yyyy-mm-dd.html'","","# Descargar la página","contenido_pagina = descargar_pagina(url)","# Cargar el contenido en S3","cargar_archivo_en_s3(bucket_name, file_key, contenido_pagina)",""],"id":5},{"start":{"row":0,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["import requests","import boto3","from datetime import datetime, timedelta","","def descargar_pagina(url):","    # Realizar la solicitud HTTP para descargar la página","    response = requests.get(url)","    # Retornar el contenido de la página","    return response.content","","def cargar_archivo_en_s3(bucket_name, file_key, file_content):","    # Crear un cliente de S3","    s3_client = boto3.client('s3')","    # Cargar el contenido del archivo en el bucket de S3","    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=file_content)","","def lambda_handler(event, context):","    # URL base del sitio web","    base_url = \"https://casas.mitula.com.co/\"","    # Nombre del bucket de S3","    bucket_name = \"bucket-parcial\"","    ","    # Obtener la fecha actual","    fecha_actual = datetime.now()","    ","    # Iterar sobre las 5 primeras páginas del sitio web","    for i in range(1, 6):","        # Construir la URL de la página actual","        url_pagina = f\"{base_url}?page={i}\"","        # Descargar la página","        contenido_pagina = descargar_pagina(url_pagina)","        # Construir la clave del archivo en S3","        file_key = f\"casas/contenido-pag-{i}-{fecha_actual.strftime('%Y-%m-%d')}.html\"","        # Cargar el contenido en S3","        cargar_archivo_en_s3(bucket_name, file_key, contenido_pagina)","    ","    return {","        'statusCode': 200,","        'body': 'Archivos descargados y almacenados en S3 correctamente.'","    }",""]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":18},"action":"remove","lines":["lambda_handler"],"id":6},{"start":{"row":16,"column":4},"end":{"row":16,"column":26},"action":"insert","lines":["descargarCasas_handler"]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"insert","lines":["g"],"id":8},{"start":{"row":40,"column":1},"end":{"row":40,"column":2},"action":"insert","lines":["i"]},{"start":{"row":40,"column":2},"end":{"row":40,"column":3},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":2},"end":{"row":40,"column":3},"action":"remove","lines":["t"],"id":9},{"start":{"row":40,"column":1},"end":{"row":40,"column":2},"action":"remove","lines":["i"]},{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"remove","lines":["g"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":40,"column":0},"end":{"row":40,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1710484547217}