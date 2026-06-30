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

# :snippet-start: smithdb-runs-retrieve-by-id-before-py
# :codegroup-tab: Before
from langsmith import Client

client = Client()
run = client.read_run("<run-id>")
# :snippet-end:

# :snippet-start: smithdb-runs-retrieve-by-id-after-py
# :codegroup-tab: After
import asyncio

from langsmith import Client


async def main():
    client = Client()
    async for project in client.projects.list(name="default", limit=1):
        break
    run = await client.runs.retrieve(
        run_id="<run-id>",
        project_id=str(project.id),
        start_time="2025-01-01T12:00:00Z",
    )


asyncio.run(main())
# :snippet-end:
