from django.test import TestCase
from jenkinsapp.forms import StudentRegistrationForm

# Create your tests here.

class StudentRegistrationTestCase(TestCase):
    def test_student_registration_form_valid(self):
        form_data = {
            'name': 'John Doe',
            'roll_number': '12345',
            'email': 'joh@nexample.com'
        }
        form = StudentRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_student_registration_form_invalid(self):
        form_data = {
            'name': 'John Doe',
            'roll_number': '',
            'email': 'john@example.com'
        }
        form = StudentRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
