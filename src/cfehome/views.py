import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir=pathlib.Path(__file__).resolve().parent
print(f"this_dir: {this_dir}")


def home_view(request,*args,**kwargs):
  return about_view(request,*args,**kwargs) # string of HTML code

def about_view(request,*args,**kwargs):
  qs=PageVisit.objects.all()
  page_qs=qs.filter(path=request.path)
  try:
    percent=(page_qs.count()*100.0)/qs.count()
  except:
    percent=0
  my_title="My Page"
  html_template="home.html"
  my_context={
    "page_title":my_title,
    "page_visit_count":qs.count(),
    "percent":percent,
    "total_visit_count":page_qs.count(),
    
    }
  
  PageVisit.objects.create(path=request.path)
  return render(request,html_template,my_context) # string of HTML code
  
  

def my_old_home_page_view(request,*args,**kwargs):
  my_title="My Page"
  my_context={"page_title":my_title}
  html_="""
  <!DOCTYPE html>
  <html>
  <body>
    <h1>{page_title} is anything</h1>
  </body>
  </html>
  """.format(**my_context)
  return HttpResponse(html_) # string of HTML code