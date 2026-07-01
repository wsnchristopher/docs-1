// :remove-start:
if (!process.env.LANGSMITH_API_KEY) {
  console.log("Skipping (LANGSMITH_API_KEY required).");
  process.exit(0);
}
process.on("uncaughtException", (reason) => {
  const msg = String(reason);
  if (
    /\b[45]\d{2}\b/.test(msg) ||
    msg.includes("Invalid UUID") ||
    msg.includes("PermissionDenied")
  ) {
    console.log(`Skipping (placeholder values in test env): ${reason}`);
    process.exit(0);
  }
  process.exit(1);
});
// :remove-end:

// :snippet-start: runs-query-filter-errors-before-js
// :codegroup-tab: Before
import { Client } from "langsmith";

const client = new Client();
const runs = client.listRuns({ projectName: "default", error: true });
// :snippet-end:
