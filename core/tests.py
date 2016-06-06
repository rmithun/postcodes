import json
from django.test import TestCase
from django.test import Client

# Create your tests here.


class ValidateTests(TestCase):
    """tests to test validate method"""
    def setUp(self):
        # create data to post 
        self.data = 'EC1A 1BB'
        # creating instance of a client.
        self.client = Client()

    def test_response_is_200(self):
        """test the response is 200 ok"""
        # Issue a GET request.
        response = self.client.get('/postcode/validate/%s/'%(self.data))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_response_is_405_for_post(self):
        """test the response is 405"""
        # Issue a POST request.
        response = self.client.post('/postcode/validate/%s/'%(self.data))
        # Check that the response is 405 method not allowed.
        self.assertEqual(response.status_code, 405)

    def test_invalid_code(self):
        """testing invalid codes"""
        postcode = 'EC1A CYZ'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertFalse(json_data['valid'])

    def test_valid_code(self):
        """testing valid code"""
        postcode = 'SW1W 0NY'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_format_AA9A_9AA(self):
        """testing valid code format AA9A 9AA"""
        postcode = 'EC1A 1BB'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_format_A9A_9AA(self):
        """testing valid code format A9A 9AA"""
        postcode = 'W1A 0AX'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_format_A9_9AA(self):
        """testing valid code format A9 9AA"""
        postcode = 'M1 1AE'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_format_A99_9AA(self):
        """testing valid code format A99 9AA"""
        postcode = 'B33 8TH'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_format_AA9_9AA(self):
        """testing valid code format AA9 9AA"""
        postcode = 'CR2 6XH'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_format_AA99_9AA(self):
        """testing valid code format AA99 9AA"""
        postcode = 'DN55 1PT'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_formatted(self):
        """testing whether the post code is formatted"""
        postcode = 'CR26XH'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertEqual(json_data['postcode'], 'CR2 6XH')

    def test_validate_view_strips_spaces(self):
        """testing whether the post code is stripped for spaces"""
        postcode = ' DN55 1PT  '
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertEqual(json_data['postcode'], 'DN55 1PT')

    def test_special_postcode_GIR_0AA(self):
        """testing special case post code GIR 0AA"""
        postcode = 'GIR 0AA'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_lowercase_postcode_input(self):
        """testing lowercase valid code"""
        postcode = 'dn551pt'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])

    def test_postcode_without_spaces(self):
        """testing whether the post code is formatted"""
        postcode = 'CR2 6XH'
        response = self.client.get('/postcode/validate/%s/'%(postcode))
        json_data = json.loads(response.content)
        self.assertTrue(json_data['valid'])





    