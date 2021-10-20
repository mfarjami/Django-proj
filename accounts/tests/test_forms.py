from django.test import SimpleTestCase
from accounts.froms import UserRegisterForm, UserImageForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


class TestResgisterForm(SimpleTestCase):
    def test_valid_data(self):
        form = UserRegisterForm(data={'username':'mohammad', 'email':'mohammad@email.com', 'password':'pass'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class TestProfileImageForm(SimpleTestCase):
    def test_valid_Data(self):
        upload_file = open(f'{settings.AWS_LOCAL_STORAGE}/1.jpg', 'br')
        file_dic = {'file':SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = UserImageForm(file_dic)
        self.assertTrue(form.is_valid())
