from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo
from django.conf import settings as s
import boto3
import datetime
import os


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
            
            # Get the original filename and extension
            original_filename, file_extension = os.path.splitext(photo_instance.image.name)
            
            # Get current date and time
            current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            # Construct unique filename with date and original filename
            filename = f"{current_date}_{original_filename}{file_extension}"
            
            # Set the filename
            photo_instance.image.name = filename
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
    objects = s3.list_objects(Bucket=bucket_name)

    uploaded_photos = []
    if 'Contents' in objects:
        for obj in objects['Contents']:
            uploaded_photos.append({
                'name': obj['Key'],  # Assuming key name as file name
                'permanent_link': f"{LIARA['endpoint']}/{bucket_name}/{obj['Key']}",
                'temporary_link': s3.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': bucket_name, 'Key': obj['Key']},
                    ExpiresIn=3600  # 1 hour expiry
                )
            })
    else:
        uploaded_photos.append({'name': 'no file', 'permanent_link': '', 'temporary_link': ''})

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


