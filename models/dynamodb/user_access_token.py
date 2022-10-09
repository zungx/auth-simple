from app import dyn, config


class UserAccessToken(object):

    def __init__(self):
        self.table = dyn.resource.Table(config.DYNAMODB_TABLE_ACCESS_TOKEN)
