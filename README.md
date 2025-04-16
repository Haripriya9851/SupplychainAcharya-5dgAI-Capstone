# Supply chain Acharya - 5dgAI - Capstone Project
Your Gen AI guide for intelligent inventory & replenishment diagnostics

# Problem Statement


# Solution
Acharya answers questions conversationally, explains root causes, and suggests actions.

"Supply Chain Acharya - An AgentBot" can help answer all your supplychain related queries. The Agentic The supply chain management system that integrates with a database to analyze forecast, inventory, logistics, sales tables, generate SQL queries, and provide root cause analysis based on agent-driven workflows.

# Features
**Text-Based Chat Interface:** A simple Tkinter-based interface for interacting.
**Intent Recognition:** Identifies the patient's intent (e.g., "refill medication," "check dosage").
**Entity Extraction:** Extracts relevant information from user/patient input (e.g., medication name).
**Medication Refill:** Simulates medication refills based on available inventory.
Dosage Check: Provides typical dosage information (from knowledge base).
OCR Support: Extracts text from prescription images using PaddleOCR.

# Tech-Stack 

1. LangGraph - 
2. Function Calling -
3. Few-Shot-CoT Prompt Engineering-
4. Evaluation - Simulated Realistic data

## How It Works
- **Digital Twin:** Digital Twin of a small supply network to simulate 30 days of demand and replenishment, enabling realistic testing.
- **Manager Agent:** This agent decides whether clarification is needed or if SQL generation should proceed based on the user's input.

- **SQL Generator Agent:** Generates SQL queries based on the user's input.

- **SQL Executor Agent:** Executes the generated SQL query to fetch the required data from the database.

- **Root Cause Agent:** Analyzes the fetched data to determine the root cause of the problem, if applicable.

The Graph module connects these agents in a sequential flow, ensuring that each agent performs its task in the correct order.

## Project Goals
**Modularity:** The design is flexible and modular, allowing for easy additions or modifications of agents or processes.

**Simplicity:** Focuses on the core logic to solve a specific task efficiently.

**Scalability:** While simplified for the hackathon, the architecture can be expanded to handle more complex supply chain tasks.

# Folder Structure

    /supply_chain_acharya
      ├── /db_tools
      │    ├── db_connection.py
      │    └── query_executor.py
      ├── /Agents
      │    ├── manager_agent.py
      │    ├── sql_generator_agent.py
      │    ├── sql_executor_agent.py
      │    └── root_cause_agent.py
      ├── /Graph
      │    ├── state.py
      │    ├── node.py
      │    └── graph_builder.py
      ├── main.py

## Setup and Run

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/supply_chain_graph.git
   cd supply_chain_acharya
   ```
2. Install Requirements:

   ```
   pip install -r requirements.txt  # Add dependencies if required
   ```
3. To run the system, simply execute the ```main.py``` script:

    ```
     python main.py
    ```

4. This will initiate the process, running the sequence of agents (manager, SQL generator, SQL executor, and root cause analyzer), and print the results.

👥 Contributors

[Your Name]

[Team Members or Collaborators]
