MONGO_PORT = 27017
MONGO_DBNAME = 'system_db'

RESOURCE_METHODS = ['GET', 'POST']

DOMAIN = {
  'computer_info': {
    'schema': {
      'username': {
        'type': 'string'
      },
      'system_info': {
        'type' : 'dict',
        'schema' : {
         'system': {
          'type': 'string'
         },
         'node': {
          'type': 'string'
         },
         'release': {
          'type': 'string'
         },
         'processor': {
          'type': 'string'
         },
         'bit_architecture': {
          'type': 'string'
         },
         'current_cpu_freq': {
          'type': 'string'
         }
        }
      },
      'memory': {
        'type' : 'dict',
        'schema' : {
         'total': {
          'type': 'number'
         },
         'available': {
          'type': 'number'
         },
         'used': {
          'type': 'number'
         },
         'free': {
          'type': 'number'
         }
       }
      },
      'disk': {
        'type' : 'dict',
        'schema' : {
         'total': {
          'type': 'number'
         },
         'used': {
          'type': 'number'
         },
         'free': {
          'type': 'number'
         },
         'partition': {
           'type' : 'dict',
           'schema' : {
           'device': {
            'type': 'string'
           },
           'mount point': {
            'type': 'string'
           },
           'file system type': {
            'type': 'string'
           },
           'opts': {
            'type': 'string'
           }
          }
         }
       }
      }
    }
  }
}
