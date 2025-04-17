# welcome_node.py or nodes.py

class WelcomeNode:
    def run(self, state: dict) -> dict:
        print("👋 Welcome to Supply Chain Acharya!")
        print("Ask me why a product is out of stock at a store, and I’ll investigate!")
        state["needs_user_input"] = False  # Proceed to manager
        return state
