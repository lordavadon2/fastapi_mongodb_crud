
def student_entity(db_item) -> dict:
    return {
        'id': str(db_item['_id']),
        'name': db_item['student_name'],
        'email': db_item['student_email'],
        'phone': db_item['student_phone']
    }


def list_of_student_entity(db_item_list) -> list:
    return [student_entity(item) for item in db_item_list]
