# SET ENVIRONMENT VARIABLES
ENV_FILE="/c/PY/WORK/mistakes_accounted/.env"


echo "ENV_FILE is set to: $ENV_FILE"
# Load environment variables from the .env file
if [ -f "$ENV_FILE" ]; then
  source "$ENV_FILE"
else
  echo "Error: $ENV_FILE not found."
  exit 1
fi
export PG_CONTAINER_NAME
export POSTGRES_USER
export POSTGRES_DB
docker exec -t ${PG_CONTAINER_NAME} pg_dump -U ${POSTGRES_USER} -Fp -f /tmp/db_dump.sql --dbname=${POSTGRES_DB}
mkdir -p ./postgres
docker cp ${PG_CONTAINER_NAME}:/tmp/db_dump.sql ./postgres/db_dump.sql
