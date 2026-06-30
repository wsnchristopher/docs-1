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

# :snippet-start: runs-query-scoped-filters-before-py
# :codegroup-tab: Before
from langsmith import Client

client = Client()
runs = client.list_runs(
    project_name="default",
    filter='eq(name, "RetrieveDocs")',
    trace_filter='and(eq(feedback_key, "user_score"), eq(feedback_score, 1))',
    tree_filter='eq(name, "ExpandQuery")',
)
# :snippet-end:

# :snippet-start: runs-query-scoped-filters-after-py
# :codegroup-tab: After
import asyncio

from langsmith import Client


async def main():
    client = Client()
    async for project in client.projects.list(name="default", limit=1):
        break
    async for run in client.runs.query(
        project_ids=[str(project.id)],
        filter='eq(name, "RetrieveDocs")',
        trace_filter='and(eq(feedback_key, "user_score"), eq(feedback_score, 1))',
        tree_filter='eq(name, "ExpandQuery")',
    ):
        print(run.id, run.name, run.status)


asyncio.run(main())
# :snippet-end:
