# AGENTS.md - Spec-Driven Development Guide

## Purpose
This project uses **Spec-Driven Development** where no code is written without a specification.

## Workflow
All AI agents must follow: **Specify → Plan → Tasks → Implement**

## Spec-Kit Files

### 1. Constitution (WHY)
File: `specs/constitution.md`
- Project principles
- Architecture values
- Technology constraints

### 2. Specify (WHAT)
File: `specs/specify.md`
- User journeys
- Requirements
- Acceptance criteria

### 3. Plan (HOW)
File: `specs/plan.md`
- Component breakdown
- Architecture
- Class diagrams

### 4. Tasks (BREAKDOWN)
File: `specs/tasks.md`
- Atomic work units
- Task IDs
- Implementation steps

## Rules for AI Agents

1. ✅ **Read specs before coding**
2. ✅ **Reference Task IDs in code comments**
3. ✅ **Follow the constitution principles**
4. ✅ **Update specs if requirements change**
5. ❌ **Never generate code without a task**
6. ❌ **Never modify architecture without updating plan**

## Code References
Every code file must include:
```python
# [Task]: T-XXX
# [From]: specify.md §Section, plan.md §Component
```

## Agent Behavior

### When generating code: