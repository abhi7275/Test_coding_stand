# Violates Indentation and Maximum Line Length guidelines
def function_with_long_name_and_wrong_indentation(parameter1, parameter2,
                                                  parameter3, parameter4):
    # Violates Whitespace guidelines
    variable_with_whitespace  = "example"

    # Violates Naming Conventions guidelines
    class myclass:
        def __init__(self):
            self.variableName = "example"

        def FunctionName(self):
            return "example"

    # Violates Comments guidelines
    # This is a comment that is too long and violates the maximum line length

    # Violates Function Annotations guidelines
    def function_with_no_annotations(x):
        return x * 2

    # Violates Avoiding Hardcoding guidelines
    magic_number = 42
    result = 10 + magic_number

    # Violates Docstrings guidelines
    def my_function():
        """This is a function without a proper docstring."""
        pass
