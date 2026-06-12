# Agentic Folder Rebuild — FastAPI Backend

Two agents: **content_agent**, **web_search_agent**

---

## Step-by-step order

### 1. Enums
`src/agentic/enums/`
- `agents_enum.py` — `AgentsEnum` (CONTENT, WEB_SEARCH)
- `tools_enum.py` — tool name constants
- `agent_message_source.py` — message source enum
- `web_search_type.py` — web search type enum

### 2. Models
`src/agentic/models/`
- `api_response_dto.py` — standard API response wrapper (`BaseModel`)
- `agent_response_model.py` — agent output shape
- `structured_response_models/supervisor_structured_response.py` — supervisor routing model

### 3. Schema
`src/agentic/schema/`
- `state/base_state_schema.py` — shared base `TypedDict` fields
- `state/content_agent_state_schema.py` — content agent state
- `state/web_search_agent_state_schema.py` — web search agent state
- `state/graph_unified_state_schema.py` — merged graph state
- `dao/agentic_master_session.py` — session DB model
- `dao/agentic_session_conversations.py` — conversation DB model

### 4. Exception
`src/agentic/exception/`
- `function_polling_exception.py`

### 5. Base
`src/agentic/base/`
- `base_agent_tool.py` — abstract tool with `name`, `description`, `run()`
- `base_agent_tool_registry.py` — tool list builder
- `base_agent.py` — abstract agent: `build_graph()`, `invoke()`
- `base_supervisor.py` — routing logic base

### 6. Utils
`src/agentic/utils/`
- `async_mongo_db_saver.py` — async MongoDB checkpointer for LangGraph
- `function_polling.py` — long-running tool polling
- `reducers/add_messages_trim_reducer.py`
- `reducers/conversation_summary_utils.py`

### 7. Prompts
`src/agentic/prompts/`
- `supervisor_prompt.py`
- `content_agent_prompt.py`
- `web_search_agent_prompt.py`

### 8. Agents
Build each agent in this sub-structure:
```
agents/
  content_agent/
    tools/
      helpers/generate_email_helper.py
      content_tool.py
    content_agent.py
  web_search_agent/
    tools/
      web_search_agent_tools.py
    web_search_agent.py
```
Order: helpers -> tools -> agent class

### 9. Service
`src/agentic/service/`
- `graph_invocation_service.py` — wires agents into the graph, handles invoke/stream
- `agent_session_dashboard_service.py` — session CRUD

### 10. Controller
`src/agentic/controller/`
- `agent_session_dashboard_controller.py` — `APIRouter` with `/invoke` and session endpoints

### 11. Entry point
- `agentic_workflow.py` — builds and compiles the LangGraph graph
- Include router in `src/main.py` via `app.include_router(...)`

---

## Key dependency rules
- Agents import from `base`, `schema`, `prompts`, `enums`, `utils` only
- Service imports agents + DAOs; never the reverse
- Controller imports service only; no direct agent imports

---

## Checklist
- [ ] Enums
- [ ] Models
- [ ] Schema (states + DAOs)
- [ ] Exception
- [ ] Base classes
- [ ] Utils
- [ ] Prompts
- [ ] content_agent (tools -> agent)
- [ ] web_search_agent (tools -> agent)
- [ ] Service
- [ ] Controller
- [ ] agentic_workflow.py
