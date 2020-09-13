from converter import Converter


def get_label_id_from_name(label_name):
    converter = Converter.getInstance()

    for labelmap in converter.labelmap:
        if labelmap.type == label_name:
            return labelmap.id

    return 0
