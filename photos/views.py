from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo
from django.conf import settings as s

import boto3

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_photo')
    else:
        form = PhotoForm()

    # Retrieve a list of uploaded photos from the S3 bucket
    s3 = boto3.client('s3',
        endpoint_url=s.LIARA_ENDPOINT,
        aws_access_key_id=s.LIARA_ACCESS_KEY,
        aws_secret_access_key=s.LIARA_SECRET_KEY
    )
    bucket_name = s.LIARA_BUCKET_NAME
    objects = s3.list_objects(Bucket=bucket_name)['Contents']

    uploaded_photos = []
    for obj in objects:
        uploaded_photos.append({
            'name': obj['Key'],  # Assuming key name as file name
            'permanent_link': f"{s.LIARA_ENDPOINT}/{bucket_name}/{obj['Key']}",
            'temporary_link': s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': obj['Key']},
                ExpiresIn=3600  # 1 hour expiry
            )
        })

    return render(request, 'photos/upload_photo.html', {'form': form, 'uploaded_photos': uploaded_photos})

def show_uploaded_photo(request):
    latest_photo = Photo.objects.last()  # Retrieve the latest uploaded photo
    return render(request, 'photos/show_uploaded_photo.html', {'photo': latest_photo})
