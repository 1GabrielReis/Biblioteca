from fastapi import HTTPException

class ControllerException(HTTPException):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"Error {self.status_code}: {self.message}"
