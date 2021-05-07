from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successful"""
        email = 'test@abc.com'
        password = 'password124'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the new email for user is normalized"""
        email = 'test@ABC.cOm'
        user = get_user_model().objects.create_user(email, 'password124')

        self.assertEqual(user.email, email.lower()) 

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'passswer124')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        email = 'test@abc.com'
        password = 'pasafnak123'
        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_advisor_created(self):
        """Test creating a new advisor"""
        name = 'Advisor1'
        advisor = models.Advisor.objects.create(
            name = name
        )
    
        self.assertEqual(advisor.name, name)

    @patch('uuid.uuid4')
    def test_advisor_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid 
        file_path = models.recipe_image_file_path(None, 'image.jpg')

        exp_path = f'uploads/advisor/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)