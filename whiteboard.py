# In this coding challenge, you have to create a function that will identify the basic data type of the given input. The function should identify the input data as one of the following categories: 'string', 'integer', 'float', or 'boolean'.
# Input:

# input_data - The input data can be of any basic Python data type, including strings, integers, floats, or booleans.
# Output:

# Return a string representing the identification of the input data.
# Examples:


#basic_data_type_identifier("hello") # returns "string"
#basic_data_type_identifier(42) # returns "integer"
#basic_data_type_identifier(3.14) # returns "float"
#basic_data_type_identifier(True) # returns "boolean"




def basic_data_type (input_data):
    data_type = type(input_data)
    if data_type == str:
        return "str"
    elif data_type == int:
        return "integer"
    elif data_type == float:
        return "float"
    else:
        return "boolean"
print(basic_data_type("true"))