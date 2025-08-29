def validate_non_empty_string(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value

def validate_id(value, entity_name):
    try:
        id_value = int(value)
        if id_value <= 0:
            raise ValueError(f"{entity_name} ID must be a positive integer.")
        return id_value
    except ValueError:
        raise ValueError(f"Invalid {entity_name} ID")