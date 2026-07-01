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

// :snippet-start: runs-query-filter-metadata-after-js
// :codegroup-tab: After
import { Client } from "langsmith";

const client = new Client();
const filterStr = "and(eq(metadata_key, 'user_id'), eq(metadata_value, 'u_123'))";
const project = await client.projects
  .list({ name: "default", limit: 1 })
  .then((page) => page.getPaginatedItems()[0]);
for await (const run of client.runs.query({
  project_ids: [project.id],
  filter: filterStr,
})) {
  console.log(run.id);
}
// :snippet-end:
