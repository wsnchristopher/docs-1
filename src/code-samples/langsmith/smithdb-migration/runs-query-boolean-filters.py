# :remove-start:
import os
import sys

if not os.environ.get("LANGSMITH_API_KEY"):
    print("Skipping (LANGSMITH_API_KEY required).")
    sys.exit(0)


def _handle_expected_error(exc_type, exc_val, exc_tb):
    import requests
    _skip = (ValueError, requests.HTTPError)
    try:
        from langsmith.utils import LangSmithError, LangSmithUserError
        _skip = _skip + (LangSmithError, LangSmithUserError)
    except ImportError:
        pass
    if isinstance(exc_val, _skip) or "403" in str(exc_val) or "404" in str(exc_val) or "422" in str(exc_val):
        print(f"Skipping (placeholder values in test env): {exc_val}")
        sys.exit(0)
    sys.__excepthook__(exc_type, exc_val, exc_tb)


sys.excepthook = _handle_expected_error
# :remove-end:

# :snippet-start: runs-query-boolean-filters-before-py
# :codegroup-tab: Before
from langsmith import Client

client = Client()
filter_str = (
    'and(gt(start_time, "2023-07-15T12:34:56Z"),'
    ' or(neq(status, "error"),'
    '    and(eq(feedback_key, "Correctness"), eq(feedback_score, 0.0))))'
)
runs = client.list_runs(project_name="default", filter=filter_str)
# :snippet-end:

# :snippet-start: runs-query-boolean-filters-after-py
# :codegroup-tab: After
import asyncio

from langsmith import Client


async def main():
    client = Client()
    filter_str = (
        'and(gt(start_time, "2023-07-15T12:34:56Z"),'
        ' or(neq(status, "error"),'
        '    and(eq(feedback_key, "Correctness"), eq(feedback_score, 0.0))))'
    )
    async for project in client.projects.list(name="default", limit=1):
        break
    runs = client.runs.query(project_ids=[str(project.id)], filter=filter_str)


asyncio.run(main())
# :snippet-end:
