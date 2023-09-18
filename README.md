# pymojeek

An unofficial client for the [Mojeek API](https://www.mojeek.co.uk/support/api/).

## Usage

```python
from pymojeek import Search

client = Search(api_key=...)
results = client.search("pymojeek")

print(f"Found {len(results)} for query 'pymojeek'")
```
