from azure.cosmos import CosmosClient, exceptions
from dotenv import load_dotenv
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()
  
# Obtener las variables de entorno
COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CONTAINER_USUARIO = os.getenv("CONTAINER_USUARIO")
CONTAINER_PROYECTO = os.getenv("CONTAINER_PROYECTO")

# Inicializar el cliente de Cosmos DB
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)

# Crear o obtener la base de datos
try:
    database = client.create_database_if_not_exists(id=DATABASE_NAME)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(DATABASE_NAME)

# Crear o obtener el contenedor usuario
try:
    container_usuario  = database.create_container_if_not_exists(
        id=CONTAINER_USUARIO,
        partition_key={'paths': ['/id'], 'kind': 'Hash'},
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(CONTAINER_USUARIO)


# Crear o obtener el contenedor proyecto
try:
    container_proyecto = database.create_container_if_not_exists(
        id=CONTAINER_PROYECTO,
        partition_key={'paths': ['/id'], 'kind': 'Hash'},
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    container_proyecto = database.get_container_client(CONTAINER_PROYECTO)
    