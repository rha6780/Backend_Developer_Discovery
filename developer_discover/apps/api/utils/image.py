import os
import uuid

from django.conf import settings
from apps.api.utils.s3 import upload_file

IMAGE_BUCKET_NAME = "developer-discovery-images"


class ImageSave:
    def save(self, request):
        if request.FILES.get("image", None) is not None:
            image = request.FILES["image"]
            image_extension = os.path.splitext(image.name)[1]
            image_name = str(uuid.uuid4()) + image_extension

            save_path = f"{os.path.join(settings.BASE_DIR/settings.MEDIA_ROOT)}"
            img_save_path = "%s/%s" % (save_path, image_name)
            img_s3_path = "%s%s" % (settings.S3_MEDIA_PATH, image_name)

            if not os.path.exists(save_path):
                os.makedirs(os.path.dirname(save_path), exist_ok=True)

            img_save_path = "%s/%s" % (save_path, image_name)
            with open(img_save_path, "wb+") as f:
                for chunk in image.chunks():
                    f.write(chunk)

            if upload_file(img_save_path, IMAGE_BUCKET_NAME, object_name=img_s3_path):
                os.remove(img_save_path)
                return image_name
            else:
                os.remove(img_save_path)
                return "error/image_not_found.png"
