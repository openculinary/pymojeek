from datetime import datetime
from unittest import TestCase

from tests.fixtures import json_response

from pymojeek import Search


class ParseTests(TestCase):
    def test_parse_json(self) -> None:
        response_data = json_response()["response"]
        search_results = Search.Results.parse(response_data)

        self.assertEqual(1, len(search_results))
        self.assertEqual(17, search_results.total)

        expected_result = Search.Result(
            url="https://github.com/openculinary/pymojeek.git/",
            title="pymojeek - Python library for the Mojeek API",
            description="pymojeek - Python library for the Mojeek API",
            clustered=True,
            categories=["cat1", "cat3"],
            crawled_at=datetime(2023, 9, 18, 12, 45),
            modified_at=datetime(2023, 9, 18, 12, 45),
            published_at=datetime(2023, 9, 18, 12, 45),
            image_url="https://example.org",
            image_width=64,
            image_height=64,
        )
        self.assertEqual(expected_result, search_results[0])
