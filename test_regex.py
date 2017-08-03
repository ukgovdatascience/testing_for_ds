from regex import is_valid_url

class TestIsValidUrl(object):
    def test_simple(self):
        assert is_valid_url('https://www.gov.uk')

    def test_ip(self):
        assert is_valid_url('https://192.168.0.1')

    def test_file(self):
        assert not is_valid_url('file://192.168.0.1')
