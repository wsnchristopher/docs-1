
// :snippet-start: runs-retrieve-by-id-before-js
// :codegroup-tab: Before
import { Client } from "langsmith";

const client = new Client();
const run = await client.readRun("<run-id>");
// :snippet-end:
