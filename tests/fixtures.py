from typing import Any, Dict


def json_response() -> Dict[str, Any]:
    return {
        "response": {
            "status": "OK",
            "head": {
                "query": "pymojeek",
                "nword": 1,
                "words": [
                    {
                        "full": "pymojeek",
                        "stem": "pymojeek",
                        "plus": 1,
                        "hits:": 17,
                    },
                ],
                "timer": 0.12,
                "start": 1,
                "return": 10,
                "exact": True,
                "results": 17,
                "rankm": 169,
                "dups": 0,
                "more|excluded": 16,
            },
            "cats_ref": {
                "cat1": 4,
                "cat3": 1,
            },
            "cats_other": {
                "cat2": 2,
            },
            "facet_dates": {
                "2023-09-15T00:00:00Z": 8,
                "2023-09-16T00:00:00Z": 5,
                "2023-09-17T00:00:00Z": 3,
                "2023-09-18T00:00:00Z": 1,
            },
            "results": [
                {
                    "url": "https://github.com/openculinary/pymojeek.git/",
                    "title": "pymojeek - Python library for the Mojeek API",
                    "desc": "pymojeek - Python library for the Mojeek API",
                    "size": "2kb",
                    "timestamp": 1695037500,
                    "date": "Mon Sep 18 11:45:00 2023",
                    "pdate": 1695037500,
                    "cdatetimestamp": 1695037500,
                    "cdate": "Mon Sep 18 11:45:00 2023",
                    "mres": 1,
                    "cats": "cat1|cat3",
                    "image": {
                        "url": "https://example.org",
                        "width": 64,
                        "height": 64,
                    },
                }
            ],
        }
    }
