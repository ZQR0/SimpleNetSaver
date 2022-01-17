from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

fvar = 'String'

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def stringer(request):
    return HttpResponse('String')

def catalog(request):
    return HttpResponse(
        """<html>
    <head>
        <title>The Website</title>
        <meta charset="utf-8">
        <link rel='shortcut icon' href="https://cdn0.iconfinder.com/data/icons/flat-round-system/512/tor-512.png"/>

        <style>
            body{
                background: #A0A0CA ; /* Цвет фона и путь к файлу */
                color: #fff; /* Цвет текста */
            }
            
        </style>
        
    </head>
    <body>

        <center>
            <p><b>
            Добро пожаловать!!!
            </p></b>
        </center>

        <div class="text">
            <center>
                <p>
                    
                </p>
            </center>
        </div>

        <div class="new page link">
            <center>
                <br>
                <a href="http://127.0.0.1:8000/new_page/" target="_blank">New Page</a>
                </br>
            </center>
        </div>
            
    </body>
</html>"""
    )

def new_page_link(requests):
    return HttpResponse(
        """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Пример веб-страницы</title>
 </head>
 <body>
  <h1>Заголовок</h1>
  <!-- Комментарий -->
  <p>Первый абзац.</p>
  <p>Второй абзац.</p>
 </body>
</html>"""
    )
