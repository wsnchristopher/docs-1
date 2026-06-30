///usr/bin/env jbang "$0" "$@" ; exit $?
//JAVA 21
//KOTLIN 2.0.21
//DEPS com.langchain.smith:langsmith-java:0.1.0-beta.8

// :snippet-start: runs-query-basic-before-kt
// :codegroup-tab: Before
import com.langchain.smith.client.LangsmithClient
import com.langchain.smith.client.okhttp.LangsmithOkHttpClient
import com.langchain.smith.models.runs.RunQueryV1Params
import com.langchain.smith.models.runs.RunTypeEnum

// :remove-start:
fun main() {
    if (System.getenv("LANGSMITH_API_KEY").isNullOrBlank()) {
        println("[smithdb-runs-query-basic-before] Skipping (LANGSMITH_API_KEY is not set).")
        return
    }

// :remove-end:
val client: LangsmithClient = LangsmithOkHttpClient.fromEnv()

val params = RunQueryV1Params.builder()
    .addSession("<project-id>")
    .runType(RunTypeEnum.LLM)
    .filter("""and(eq(status, "success"), gt(total_tokens, 100))""")
    .addSelect(RunQueryV1Params.Select.ID)
    .addSelect(RunQueryV1Params.Select.NAME)
    .addSelect(RunQueryV1Params.Select.STATUS)
    .limit(100L)
    .build()

client.runs().queryV1(params).runs().forEach { run ->
    println("${run.id()} ${run.name()} ${run.status()}")
}
// :remove-start:
}
// :remove-end:
// :snippet-end:
