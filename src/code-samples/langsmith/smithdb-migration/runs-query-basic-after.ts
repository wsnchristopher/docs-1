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

// :snippet-start: runs-query-basic-after-js
// :codegroup-tab: After
import { Client } from "langsmith";

const client = new Client();
const project = await client.projects
  .list({ name: "default", limit: 1 })
  .then((page) => page.getPaginatedItems()[0]);
const page = client.runs.query({
  project_ids: [String(project.id)],
  run_type: "LLM",
  filter: 'and(eq(status, "success"), gt(total_tokens, 100))',
  selects: ["ID", "NAME", "STATUS"],
});
for await (const run of page) {
  console.log(run.id, run.name, run.status);
}
// :snippet-end:
