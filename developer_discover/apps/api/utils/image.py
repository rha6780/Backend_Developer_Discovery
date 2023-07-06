import os
import uuid

from django.conf import settings


class ImageSave:
    def save(self, request):
        if request.FILES.get("image", None) is not None:
            image = request.FILES["image"]
            image_extension = os.path.splitext(image.name)[1]
            image_name = str(uuid.uuid4()) + image_extension

            save_path = settings.MEDIA_ROOT
            if not os.path.exists(save_path):
                os.makedirs(os.path.dirname(save_path), exist_ok=True)

            img_save_path = "%s/%s" % (save_path, image_name)
            with open(img_save_path, "wb+") as f:
                for chunk in image.chunks():
                    f.write(chunk)

            return image_name
