# AI-Powered STLC Automation Agent using n8n, Groq LLM & QA Engineering

## Overview

This project demonstrates how Artificial Intelligence can automate key activities of the Software Testing Life Cycle (STLC) using n8n workflows, Groq Large Language Models, and modern QA engineering practices.

The solution consists of multiple AI agents that assist QA Engineers in requirement analysis, test planning, test case generation, Jira integration, and automated test script creation.

Instead of manually reviewing Product Requirement Documents (PRDs) and creating testing artifacts, the AI Agent analyzes the uploaded requirement document and automatically generates comprehensive QA deliverables.

---

## Business Problem

In traditional software testing projects, QA Engineers spend significant time performing:

* Requirement Analysis
* Test Planning
* Test Case Design
* Test Data Preparation
* Automation Script Creation
* Defect Tracking

These activities are repetitive and consume considerable effort.

This project leverages Generative AI to automate these tasks and accelerate the QA process while maintaining consistency and quality.

---

## Project Objectives

The primary goals of this project are:

* Automate requirement analysis from PRD documents
* Generate detailed Test Plans
* Create comprehensive Test Cases
* Produce Playwright Automation Scripts
* Assist QA Engineers using AI-powered recommendations
* Integrate with Jira for issue management
* Reduce manual effort during STLC activities

---

## Solution Architecture

```text
PRD PDF
   │
   ▼
Read PDF File
   │
   ▼
Extract Content
   │
   ▼
Groq LLM (Llama 3.3 70B)
   │
   ├── Generate Test Plan
   │
   ├── Generate Test Cases
   │
   └── Generate Playwright Scripts
   │
   ▼
Export QA Artifacts
```

---

## Workflows Included

### 1. AI Agent STLC

A conversational QA assistant powered by Groq LLM.

Features:

* Answers software testing questions
* Provides QA best practices
* Supports SDLC and STLC concepts
* Generates testing recommendations
* Acts as a virtual QA consultant

---

### 2. AI Agent STLC + Jira

Enhanced QA assistant integrated with Jira.

Features:

* QA-focused conversations
* Jira issue creation
* Bug logging support
* Requirement discussions
* Test strategy recommendations
* Memory-enabled interactions

Example Use Cases:

* Create a defect in Jira
* Generate bug summaries
* Draft issue descriptions
* Assist during defect triage

---

### 3. AI Agent STLC from PRD

The flagship workflow of this project.

The workflow accepts a Product Requirement Document (PDF) and automatically creates testing artifacts.

#### Inputs

* Product Requirement Document (PRD)
* Business Requirements
* Functional Requirements

#### AI Processing

The workflow performs:

* Requirement extraction
* Feature identification
* Risk analysis
* Test coverage planning
* Automation opportunity analysis

#### Outputs

##### Test Plan

Automatically generates:

* Project Overview
* Scope
* Objectives
* Features to Test
* Features Not to Test
* Test Types
* Entry Criteria
* Exit Criteria
* Risk Assessment
* Test Schedule

##### Test Cases

Creates structured test cases covering:

* Functional Testing
* Negative Testing
* Edge Cases
* Boundary Testing
* UI Validation
* Business Rule Validation

Generated in CSV format for easy import into QA tools.

##### Playwright Automation Scripts

Generates:

* End-to-End Tests
* UI Validation Scripts
* Form Validation Tests
* User Journey Automation
* Reusable Playwright Framework Code

---

## Technologies Used

| Technology     | Purpose                |
| -------------- | ---------------------- |
| n8n            | Workflow Automation    |
| Groq LLM       | AI Processing          |
| Llama 3.3 70B  | Requirement Analysis   |
| Jira           | Defect Tracking        |
| Playwright     | Test Automation        |
| JavaScript     | Workflow Logic         |
| PDF Processing | Requirement Extraction |
| CSV Generation | Test Case Export       |

---

## Key Features

* AI-Powered Requirement Analysis
* Automated Test Plan Creation
* Automated Test Case Generation
* Playwright Script Generation
* Jira Integration
* QA Assistant Chatbot
* End-to-End STLC Support
* Low-Code Implementation using n8n

---

## Sample Output Artifacts

The workflow generates:

```text
test_plan.md
test_cases.csv
playwright_test_cases.md
```

These files can be directly used by QA teams during project execution.

---

## Benefits

### For QA Engineers

* Faster test planning
* Improved requirement coverage
* Reduced manual documentation effort
* Faster automation script creation

### For Organizations

* Reduced testing costs
* Improved QA productivity
* Faster release cycles
* Better requirement traceability

---

## Future Enhancements

* Jira Story Retrieval
* Test Case Management Integration
* API Test Case Generation
* Selenium Framework Generation
* Test Data Generation
* Requirement Traceability Matrix (RTM)
* Defect Prediction using AI
* Multi-LLM Support

---

## Author

Rekha Govardhan

Senior QA Engineer | Banking Domain Specialist | AI-Powered QA Enthusiast

---

## Disclaimer

This project is intended for learning, experimentation, and demonstrating how Generative AI can accelerate Software Testing Life Cycle activities. Human review is recommended before using generated artifacts in production environments.
