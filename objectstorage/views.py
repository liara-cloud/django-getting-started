import boto3
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Initialize S3 Client
def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

# List all files in the bucket
def list_files(request):
    s3_client = get_s3_client()
    try:
        response = s3_client.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        return JsonResponse({'files': files})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Upload a file
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        s3_client = get_s3_client()
        file = request.FILES['file']
        try:
            s3_client.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
            return JsonResponse({'message': f'{file.name} uploaded successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Delete a file
@csrf_exempt
def delete_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        if not file_name:
            return JsonResponse({'error': 'File name is required'}, status=400)
        s3_client = get_s3_client()
        try:
            s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_name)
            return JsonResponse({'message': f'{file_name} deleted successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Generate a pre-signed URL
def generate_presigned_url(request):
    file_name = request.GET.get('file_name')
    if not file_name:
        return JsonResponse({'error': 'File name is required'}, status=400)
    s3_client = get_s3_client()
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': file_name},
            ExpiresIn=3600  # URL valid for 1 hour
        )
        return JsonResponse({'url': url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def manage_files(request):
    context = {
        'AWS_STORAGE_BUCKET_NAME': settings.AWS_STORAGE_BUCKET_NAME,
        'AWS_S3_ENDPOINT_URL': settings.AWS_S3_ENDPOINT_URL,
    }
    return render(request, 'manage_files.html', context)