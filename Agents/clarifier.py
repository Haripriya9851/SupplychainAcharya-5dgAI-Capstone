class ClarificationNode:
    def run(self, state: dict) -> dict:
        print("\n[🔁 Clarification Needed]")
        print(state.get("manager_response", "I need more information."))

        # Dynamic prompt
        response = state.get("manager_response", "").lower()

        if "store" in response:
            prompt = "Please provide the store (e.g., Store 2): "
        elif "item" in response:
            prompt = "Please provide the item name (e.g., eggs): "
        else:
            prompt = "Please provide missing information: "


        user_input = input(f"{prompt}(or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("👋 Ending session. Please restart if you'd like to try again.")
            exit()

        state["user_query"] = f"{state.get('user_query', '')} {user_input}".strip()
        state["needs_user_input"] = False
        return state
