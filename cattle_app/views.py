from django.shortcuts import render
from .models import Cattle
import uuid
from PIL import Image
import imagehash

def home(request):
    cow_id = None
    message = None
    confidence = None
    uploaded_image = None

    if request.method == 'POST':
        image = request.FILES.get('image')
        uploaded_image = image

        img = Image.open(image)
        img_hash = imagehash.average_hash(img)

        found = False

        for cow in Cattle.objects.all():
            try:
                existing_hash = imagehash.hex_to_hash(cow.image_hash)

                diff = img_hash - existing_hash

                if diff < 5:
                    cow_id = cow.cow_id
                    message = "⚠️ Cow already registered"
                    confidence = round((1 - diff/10) * 100, 2)  # % score
                    found = True
                    break

            except Exception as e:
                print("Skipping invalid hash:", e)
                continue

        if not found:
            cow_id = str(uuid.uuid4())[:8]

            Cattle.objects.create(
                cow_id=cow_id,
                image=image,
                image_hash=str(img_hash)
            )

            message = "✅ New Cow Registered"
            confidence = 100

    return render(request, 'home.html', {
        'cow_id': cow_id,
        'message': message,
        'confidence': confidence,
        'uploaded_image': uploaded_image
    })