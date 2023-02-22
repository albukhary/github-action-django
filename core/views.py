from django.http import HttpResponse

def home(request):
   text = """<h1>LAZIZBEK's mind blowing home page</h1>"""
   return HttpResponse(text)