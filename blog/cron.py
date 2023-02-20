from.models import Test, Blog
from datetime import datetime


def my_scheduled_job():
    Test.objects.create(name='test')

  

def document_expired_check():
    today = datetime.today().strftime('%Y-%m-%d')
    qs = Blog.objects.filter(expired = False)
    for doc in qs:
        exp = doc.expiration_date.strftime('%Y-%m-%d')
        if exp < today:
            doc.expired=True
            doc.save()
