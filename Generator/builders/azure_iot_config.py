import json


class Builder():
    def __init__(self, data, manifest_updates):

        self.bindings = list(elem for elem in data.get('bindings').get(
            'azure_iot') if elem.get('enabled', True) == True)

        self.manifest_updates = manifest_updates

    def build(self, manifest):

        new_manifest = {**manifest, **{}}

        for item in self.bindings:
            manifest_updates = item.get('manifest')

            for key, value in manifest_updates.items():
                if type(value) is list:
                    manifest_list = manifest.get(key, [])
                    if type(manifest_list) is dict:
                        for item in value:
                            for k, v in item.items():

                                manifest_list.update({k: v})

                                # The commented out code updated an element if it existed
                                # manifest_list_value = manifest_list.get(k)
                                # if manifest_list_value is None:
                                #     manifest_list.update({k:v})
                                # else:
                                #     if type(manifest_list_value) is list:
                                #         new_list = manifest_list_value + v
                                #         new_list = list(dict.fromkeys(new_list))
                                #         manifest_list.update({k:new_list})
                                #     elif type(manifest_list_value) is str:
                                #         manifest_list.update({k:v})
                        new_manifest.update({key: manifest_list})
                    elif type(manifest_list) is list:
                        # The commented out code updated an element if it existed
                        # new_list = value + manifest_list
                        # new_list = list(dict.fromkeys(new_list))
                        # new_manifest.update({key:new_list})
                        new_manifest.update({key: value})

        return new_manifest
