import logging

# Configurar el logger
logger = logging.getLogger(__name__)

# Middleware personalizado para registrar cada solicitud
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'Solicitud entrante: {request.method} {request.path}')
        response = self.get_response(request)
        return response