///usr/bin/env jbang "$0" "$@" ; exit $?
//JAVA 21
//KOTLIN 2.0.21
//DEPS com.langchain.smith:langsmith-java:0.1.0-beta.8

// :snippet-start: smithdb-runs-query-basic-after-kt
// :codegroup-tab: After
import com.langchain.smith.client.LangsmithClient
import com.langchain.smith.client.okhttp.LangsmithOkHttpClient
import com.langchain.smith.models.runs.RunQueryV2Params

// :remove-start:
fun main() {
    if (System.getenv("LANGSMITH_API_KEY").isNullOrBlank()) {
        println("[smithdb-runs-query-basic-after] Skipping (LANGSMITH_API_KEY is not set).")
        return
    }

// :remove-end:
val client: LangsmithClient = LangsmithOkHttpClient.fromEnv()

val params = RunQueryV2Params.builder()
    .addProjectId("<project-id>")
    .runType(RunQueryV2Params.RunType.LLM)
    .filter("""and(eq(status, "success"), gt(total_tokens, 100))""")
    .addSelect(RunQueryV2Params.Select.ID)
    .addSelect(RunQueryV2Params.Select.NAME)
    .addSelect(RunQueryV2Params.Select.STATUS)
    .build()

client.runs().queryV2(params).autoPager().forEach { run ->
    println("${run.id()} ${run.name()} ${run.status()}")
}
// :remove-start:
}
// :remove-end:
// :snippet-end:
