
# :snippet-start: runs-retrieve-basic-before-py
# :codegroup-tab: Before
from langsmith import Client

client = Client()
run = client.read_run(run_id="<run-id>")
print(run.name, run.status, run.total_tokens)
# :snippet-end:

# :snippet-start: runs-retrieve-basic-after-py
# :codegroup-tab: After
import asyncio

from langsmith import Client


async def main():
    client = Client()
    run = await client.runs.retrieve(
        run_id="<run-id>",
        select=["NAME", "STATUS", "TOTAL_TOKENS"],
    )
    print(run.name, run.status, run.total_tokens)


asyncio.run(main())
# :snippet-end:
