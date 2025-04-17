from Graph.graph_builder import SupplyChainGraph

def run():
    graph = SupplyChainGraph().build()
    state = {
    'user_query': '',
    'valid_stores': [],
    'valid_items': [],
    'generated_sql': '',
    'executed_results': '',
    'root_cause_summary': '',
    'needs_user_input': False,  # Let ManagerAgent process the query
    'clarification_attempts': 0
}

    result = graph.invoke(state)
    print(result.get('root_cause_summary') or result.get('manager_response'))

if __name__ == '__main__':
    run()
