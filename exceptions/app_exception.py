class AppException(Exception):
    status_code = 500

    def __init__(self, message=None, status_code=None, payload=None):
        super(AppException, self).__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = {
            "status_code": self.status_code,
            "message": self.message
        }
        if self.payload is not None:
            rv['errors'] = self.payload

        # TODO: Format sub error
        return rv
