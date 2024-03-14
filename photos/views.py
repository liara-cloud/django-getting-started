from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo
from django.conf import settings as s
import boto3
import uuid

LIARA = {
    'endpoint': s.LIARA_ENDPOINT,
    'accesskey': s.LIARA_ACCESS_KEY,
    'secretkey': s.LIARA_SECRET_KEY,
    'bucket': s.LIARA_BUCKET_NAME
}

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo_instance = form.save(commit=False)
            photo_instance.image.name = str(uuid.uuid4())  # Set the filename to a UUID
            photo_instance.save()
            return redirect('upload_photo')
    else:
        form = PhotoForm()

    # Retrieve a list of uploaded photos from the S3 bucket
    s3 = boto3.client('s3',
        endpoint_url=LIARA['endpoint'],
        aws_access_key_id=LIARA['accesskey'],
        aws_secret_access_key=LIARA['secretkey']
    )
    bucket_name = LIARA['bucket']
    objects = s3.list_objects(Bucket=bucket_name)['Contents']

    uploaded_photos = []
    for obj in objects:
        uploaded_photos.append({
            'name': obj['Key'],  # Assuming key name as file name
            'permanent_link': f"{LIARA['endpoint']}/{bucket_name}/{obj['Key']}",
            'temporary_link': s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': obj['Key']},
                ExpiresIn=3600  # 1 hour expiry
            )
        })

    return render(request, 'photos/upload_photo.html', {'form': form, 'uploaded_photos': uploaded_photos})

def download_photo(request, photo_name):
    s3 = boto3.client('s3',
        endpoint_url=LIARA['endpoint'],
        aws_access_key_id=LIARA['accesskey'],
        aws_secret_access_key=LIARA['secretkey']
    )
    bucket_name = LIARA['bucket']
    file_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': photo_name},
        ExpiresIn=3600  # 1 hour expiry
    )
    return redirect(file_url)

def delete_photo(request, photo_name):
    s3 = boto3.client('s3',
        endpoint_url=LIARA['endpoint'],
        aws_access_key_id=LIARA['accesskey'],
        aws_secret_access_key=LIARA['secretkey']
    )
    bucket_name = LIARA['bucket']
    s3.delete_object(Bucket=bucket_name, Key=photo_name)
    return redirect('upload_photo')


