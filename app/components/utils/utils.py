from fastapi import status, HTTPException


class ResponseException(Exception):
    def __init__(self,  detail: str):
        self.detail = detail

    def getResponse(self, done: bool, errorMessage: str):
        if not done:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=errorMessage)
        return None


    def riseHttpExceptionIfNotFound(result, message: str):
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)