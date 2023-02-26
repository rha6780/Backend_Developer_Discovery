import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework_jwt.views import BaseJSONWebTokenAuthentication
from rest_framework.views import APIView

from django.shortcuts import redirect
from django.contrib.auth import login


class JSONWebTokenAuthenticationQS(BaseJSONWebTokenAuthentication):
    def get_jwt_value(self, request):
        return request.QUERY_PARAMS.get("jwt")
