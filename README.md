# FlowCLI

**Build AI workflows in your terminal. Local-first, code-driven, and self-hostable.**

## Why FlowCLI?
- **Local-First**: No cloud dependencies. Run workflows on your machine.
- **CLI-Driven**: Define workflows in YAML/JSON and execute via CLI.
- **Self-Hostable**: Export workflows as Docker containers or Python scripts.
- **Minimalist**: No bloat. Just the essentials for AI workflows.

## Installation
```bash
pip install -e .
```

## Quick Start
1. **Initialize a workflow**:
   ```bash
   flowcli init
   ```
   This creates `workflow.yaml` with a default LLM prompt step.

2. **Run the workflow**:
   ```bash
   flowcli run workflow.yaml
   ```

## Example Workflow
```yaml
name: my_workflow
steps:
  - name: prompt
    type: llm
    model: llama3
    prompt: "Summarize this document: {{input}}"
```

## Roadmap
- Ollama integration for local LLM execution.
- Dockerfile generation for self-hosting.
- Advanced workflow features (RAG, agents).

## License
MIT