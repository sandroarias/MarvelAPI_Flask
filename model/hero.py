

class Heroi(object):
    def __init__(self, id, image, name, description):
        self._id = id
        self._image = image
        self._name = name
        self._description = description

    def get_id(self):
        return self._id

    def get_image(self):
        return self._image

    def get_nome(self):
        return self._name

    def get_description(self):
        return self._description


class HeroiConvocado(object):
    def __init__(self, id, image, name, description, dbId, dbType):
        self._id = id
        self._image = image
        self._name = name
        self._description = description
        self._dbId = dbId
        self._dbType = dbType

    def get_id(self):
        return self._id

    def get_image(self):
        return self._image

    def get_nome(self):
        return self._name

    def get_description(self):
        return self._description

    def get_dbId(self):
        return self._dbId

    def get_dbType(self):
        return self._dbType

