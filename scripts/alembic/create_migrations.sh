read -p "Enter name of migration: " message
export BOT_CONTAINER_NAME=restaurant_bot
docker exec ${BOT_CONTAINER_NAME} alembic revision --autogenerate -m "$message"