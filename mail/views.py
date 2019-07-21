from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import EmailMessage
from django.conf import settings

import os
import wget
import zipfile
import json

# Create your views here.

class SendZipEmail(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email_to_send = body.get('email', '')
        zip_urls = body.get('urls', '')
        c = 0
        zip_file = zipfile.ZipFile('send.zip', 'w')
        for url in zip_urls:
            c += 1
            name = os.system('wget -O index'+ str(c) +'.html ' + url)
            zip_file.write('index'+str(c) +'.html', compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()
        email = EmailMessage('Html in a Zip file', 'Hope you doing well, enjoy the zip file', 'settings.EMAIL_HOST_USER', [email_to_send])
        email.attach_file('send.zip', 'application/zip')
        email.send()
        return Response({'Result': 'Email sent to '+email_to_send})
