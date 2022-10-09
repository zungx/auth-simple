from app import dyn, config


class UserRefreshToken(object):

    def __init__(self):
        self.table = dyn.resource.Table(config.DYNAMODB_TABLE_REFRESH_TOKEN)
