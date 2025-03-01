# Conversion.py holds various conversions from one standared to another. Ex: Feet to meters

def to_feet(meters):
    """Takes meters as Number, returns feet as rounded float.""" 
    return round(meters / 0.3048, 2)

def to_meters(feet):
    """Takes feet as Number, returns meters as rounded float."""
    return round(feet * 0.3048, 2)