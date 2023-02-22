from django.http import HttpResponse

def home(request):
   text = """<h1>Lazizbek's mind blowing home page</h1>"""
   return HttpResponse(text)