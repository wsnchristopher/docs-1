
# :snippet-start: runs-retrieve-by-id-before-py
# :codegroup-tab: Before
from langsmith import Client

client = Client()
run = client.read_run("<run-id>")
# :snippet-end:

# :snippet-start: runs-retrieve-by-id-after-py
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
