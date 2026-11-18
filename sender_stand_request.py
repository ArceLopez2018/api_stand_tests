import configuration
import requests

#def get_docs():  #1
#    return requests.get()   #1

#def get_logs():    #2
#    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)   #2

#def get_users_table(): #3
#    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,params = {"count": 20}) #3

# las lineas de codigo de abajo se usarón para realizar los ejercicios La librería Requests: solicitudes GET
# se dejaran comentados.
#response = get_logs()  # 2
#response = get_users_table()   #2
#print(response.status_code)    #1 y 2
#print(response.headers)    #1 y 2

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

#response = get_logs("https://cnt-96ad008b-3333-468e-a8fc-55957cb3e67e.containerhub.tripleten-services.com\docs")
# print(response.status_code)
# print(response.headers)

 # "https://cnt-e47761f0-4629-4884-ac7d-aea73fe19b6c.containerhub.tripleten-services.com/docs/"
 # url de arriba para ver la documentación de la api => Urban.Grocers

### La librería de solicitudes de Python: solicitudes POST
#########################################################################################################

import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)

#########################################################################################################
# ejercicio 2 de esta seccion


def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json()) # Muestra del resultado en la consola
