import re

class ValidationChecks:
    @staticmethod
    def validate_response_format(result, keywords):
        """
        Validates if the response starts with any of the expected keywords.
        """
        return any(result.startswith(k) for k in keywords)

    @staticmethod
    def parse_validated_fields(result, dynamic_fields):
        """
        Parses the validated fields from the response dynamically.
        """
        parsed_fields = {}
        for field in dynamic_fields:
            regex = rf"{field.capitalize()}s: \[(.*?)\]"
            matches = re.findall(regex, result)
            parsed_fields[f"valid_{field}s"] = [m.strip() for m in matches[0].split(",")] if matches and matches[0] else []
        return parsed_fields

    @staticmethod
    def check_missing_fields(state, required_fields):
        """
        Checks for missing fields in the state.
        """
        missing_fields = [field for field in required_fields if not state.get(f"valid_{field}s")]
        return missing_fields

    @staticmethod
    def handle_specific_response(result):
        """
        Handles missing, invalid, or ambiguous fields dynamically.
        """
        try:
            status, field = result.split(maxsplit=1)
            prompts = {
                "Missing": f"Please provide the {field}.",
                "Invalid": f"The {field} is not valid. Please correct it.",
                "Ambiguous": f"The {field} is unclear. Can you specify more?",
            }
            return prompts.get(status, "Please clarify.")
        except ValueError:
            return "Unrecognized response format. Please clarify."

    @staticmethod
    def handle_unrecognized_response():
        """
        Handles unrecognized response formats.
        """
        return "Unrecognized response format. Please clarify."

    @staticmethod
    def handle_exception(exception):
        """
        Handles exceptions that occur during LLM invocation.
        """
        return f"⚠️ Gemini failed: {exception}"