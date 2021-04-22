
from accounts.serializers import UserDetailSerializer

def custom_jwt_response_handler(token, user=None, request=None):
    return {
        'token' : token,
        'user' : UserDetailSerializer(user, context={'request' : request}).data
    }

def required_field_validator(required_fields,submitted_list):
    missing_fields = required_fields - submitted_list
    if missing_fields:
        return False, "{} is required".format(','.join(str(x) for x in list(missing_fields)))
    else:
        return True, 'valid'