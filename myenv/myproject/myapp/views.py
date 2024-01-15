from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# creating the function with def

def hello(request):
    return HttpResponse("Hello, Vishnu!😁😁")
def home(request):
    return HttpResponse("""<body style='background-color:Red'>
                        <h1 style='color:Yellow'>Welcome To the Home Page</h1>
                        </body>""")
#triple quotes is used for multi line strings