from aiogram.dispatcher.middlewares import BaseMiddleware
import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseMiddleware):
    async def on_process_message(self, message, data):
        logger.info(f"Received a message: {message}")
        return True  # Продолжить обработку сообщения