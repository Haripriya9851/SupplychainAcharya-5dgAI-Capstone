# Supply chain Acharya - 5dgAI - Capstone Project
Your Gen AI guide for intelligent inventory & replenishment diagnostics

# Problem Statement
Retail supply chains constantly face two critical questions: ```Why is there no inventory? Why is there too much inventory?```
        
These problems frustrate store managers, disrupt store operations, cusromers and result in massive financial loss—often caused by misconfigured or forgotten replenishment parameters buried in complex systems. Supply Chain Acharya is a Gen AI-powered assistant designed to uncover these root causes using a Digital Twin of a retail supply chain network.

# Solution
"Supply Chain Acharya - An AgentBot" can help answer all your supplychain related queries. The Agentic The supply chain management system that integrates with a database to analyze forecast, inventory, logistics, sales tables, generate SQL queries, and provide root cause analysis based on agent-driven workflows.

Acharya answers questions conversationally, explains root causes, and suggests actions.

# 🚀 Features

**Chat-Based Interface:**  Natural language interface for planners to ask questions like “Why am I out of stock?” or “Why was too much inventory sent?”

**Intent Recognition:**  Detects user intent—whether it’s a strategic, tactical, or operational query (e.g., inventory, lead time issue, price discrepancy).

**Entity Extraction:**  Extracts supply chain-specific entities such as item, store, DC, vendor, lead time, and calendar from queries.

**Dynamic SQL Generation:**  Generates real-time, schema-aware SQL queries to fetch precise data from the Digital Twin simulation.

**Interactive Workflow Looping:**  Auto-verifies parameters, re-prompts for missing info, and loops back with refined answers—just like a human expert.


# Tech-Stack 

1. LangGraph - 
2. Function Calling -
3. CoT Prompt Engineering- 
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

# Folder Structure

    /SupplychainAcharya-5dgAI-Capstone
      ├── /db_tools
      │    ├── db_connection.py
      │    ├── query_executor.py
      ├── /agents
      │    ├── manager_agent.py
      │    ├── sql_generator_agent.py
      │    ├── sql_executor_agent.py
      │    ├── root_cause_agent.py
      │    ├── intent_recognition_agent.py  # New agent for intent recognition
      │    ├── entity_extraction_agent.py  # New agent for entity extraction
      ├── /graph
      │    ├── state.py
      │    ├── node.py
      │    ├── graph_builder.py
      ├── /data
      │    ├── sample_data.csv  # New folder for storing sample data
      │    ├── schema.sql       # Database schema file
      ├── /utils
      │    ├── logger.py        # Utility for logging
      │    ├── config.py        # Configuration file
      ├── main.py


## Setup and Run
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/supply_chain_graph.git
   cd supply_chain_acharya
   ```

2. Create a Conda environment:

   ```bash
   conda create -n supply_chain_env python=3.10 -y
   conda activate supply_chain_env
   ```

3. Install Requirements:

   ```bash
   pip install -r requirements.txt

   # Install additional dependencies
   pip install langchain-google-genai==2.1.2
   pip install -U langgraph
   pip install -U langchain langchain-core langchain-community pydantic
   ```

4. Run the system:

   Execute the `main.py` script to start the application:

   ```bash
   python main.py
   ```

This will initiate the process, running the sequence of agents (manager, SQL generator, SQL executor, and root cause analyzer), and print the results.

👥 Contributors

## 👥 Co-Authors

| Name                    | Kaggle Profile                                                  | LinkedIn Profile                                                   |
|-------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
| Dr. Sonney George       | [@sonneygeorge](https://www.kaggle.com/sonneygeorge)           | [Dr. Sonney George](https://www.linkedin.com/in/dr-sonney-george)  |
| Hari Priya Ramamoorthy  | [@haripriyaram51](https://www.kaggle.com/haripriyaram51)       | [Hari Priya Ramamoorthy](https://www.linkedin.com/in/haripriyaram51) |
| Dr. Yuan Shang          | [@raymondyuanshang](https://www.kaggle.com/raymondyuanshang)   | [Dr. Yuan Shang](https://www.linkedin.com/in/yuanshang2020/)       |
| Toshal Warke            | [@toshall](https://www.kaggle.com/toshall)                     | [Toshal Warke](https://www.linkedin.com/in/toshal-warke)           |



