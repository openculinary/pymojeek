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
        client.search("testing testing one two three")

        self.assertTrue(mock_urlopen.called)
        outbound_request = mock_urlopen.call_args_list[0].args[0]
        requested_url = outbound_request.get_full_url()
        self.assertIn("&q=testing+testing+one+two+three", requested_url)

    @patch("pymojeek.urlopen")
    def test_word_exclusion_query(self, mock_urlopen: Mock) -> None:
        mock_urlopen.return_value = SearchTest.MockResponse()

        client = Search(api_key="000000000000000000000000")
        client.search(
            "testing testing one two three",
            exclude_words=["ignore", "these"],
        )

        self.assertTrue(mock_urlopen.called)
        outbound_request = mock_urlopen.call_args_list[0].args[0]
        requested_url = outbound_request.get_full_url()
        self.assertIn("&qm=ignore+these", requested_url)
