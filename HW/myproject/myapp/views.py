from django.http import HttpResponse
import logging

# Получаем экземпляр объекта логгера для записи логов
logger = logging.getLogger(__name__)

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы найдете много интересного о моем проекте и обо мне :)</p>
    """
    
    # Логируем посещение страницы
    logger.info('Пользователь посетил главную страницу')
    
    return HttpResponse(html)

def about(request):
    html = """
    <h1>Привет</h1>
    <h2>Меня зовут Сергей и я начинающий Python-разработчик</h2>
    """
    
    # Логируем посещение страницы
    logger.info('Пользователь посетил страницу "О себе"')
    
    return HttpResponse(html)