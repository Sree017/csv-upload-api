from django.shortcuts import render

import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.db import IntegrityError

class UploadCSV(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file.name.endswith('.csv'):
            return Response({"error":"Only csv files allowed"}, status=400)
        
        decode_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decode_file)
        success = 0
        failed = 0
        errors = []
        for row in reader:
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                try:
                    serializer.save()
                    success += 1
                except IntegrityError:
                    continue
            else:
                failed += 1
                errors.append(serializer.errors)

        return Response({"success_count": success, "failed_count": failed, "errors":errors})
