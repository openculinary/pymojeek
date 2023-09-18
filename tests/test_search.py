import json
from unittest import TestCase
from unittest.mock import Mock, patch

from pymojeek import Search

from tests.fixtures import json_response


class SearchTest(TestCase):
    class MockResponse:
        def read(self) -> bytes:
            return json.dumps(json_response()).encode("utf-8")

    @patch("pymojeek.urlopen")
    def test_basic_query(self, mock_urlopen: Mock) -> None:
        mock_urlopen.return_value = SearchTest.MockResponse()

        client = Search(api_key="000000000000000000000000")
        client.search("testing")

        self.assertTrue(mock_urlopen.called)
