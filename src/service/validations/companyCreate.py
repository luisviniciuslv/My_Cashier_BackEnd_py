from exceptions.invalidPayloadException  import InvalidPayloadException

REQUIRED_FIELDS = ['name', 'email', 'password', 'password_confirmation']

def validatePayload(payload: dict):
  for field in REQUIRED_FIELDS:
    if field not in payload:
      raise InvalidPayloadException(f'Missing field {field}')

  if payload['password'] != payload['password_confirmation']:
    raise InvalidPayloadException('Password and password confirmation do not match')

  return True