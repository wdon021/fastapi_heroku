from pydantic import BaseModel, Field
# 2. Class which describes irirs BaseModel
# Pydantic baseModel has the function to do
# Data COnversion
# Data validation
# Data parsing
class Iris(BaseModel):
    # Declare validation and metadata inside of Iris Model using Field
    sepal_length: float = Field(..., example = 6.0) # ... means this field is not optional
    sepal_width: float = Field(..., example = 2.2) # example is a placeholder
    petal_length: float = Field(..., example = 5.0)
    petal_width: float= Field(..., example = 1.5)
