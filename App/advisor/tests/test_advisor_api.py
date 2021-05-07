import tempfile
import os 

from PIL import Image
from django.test import TestCase 
from django.urls import reverse 

from rest_framework import status 
from rest_framework.test import APIClient 

from core.models import Advisor

from advisor.serializers import AdvisorSerializer

ADVISOR_URL = reverse('advisor:advisor-list')

def image_upload_url(advisor_id):
    """Return URL for the recipe image upload"""
    return reverse('advisor:advisor-upload-image', args=[advisor_id])


class AdvisorImageUploadTests(TestCase):

    def test_upload_image(self):
        url = image_upload_url(self.advisor.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'image':ntf}, format='multipart')

        self.advisor.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(self.advisor.image.path))    


    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url(self.advisor.id)
        res = self.client.post(url, {'image':'notimage'}, format='multipart')
        print('anfnal')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    