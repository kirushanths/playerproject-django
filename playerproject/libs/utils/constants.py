# URL LOCATIONS

DAZZLE_URL = 'http://10.30.0.2/'

STATIC_LIB_URL = DAZZLE_URL + 'static/engine/libs/'
STATIC_JS_URL = DAZZLE_URL + 'static/engine/js/'
STATIC_CSS_URL = DAZZLE_URL + 'static/engine/css/'

#BOOTSTRAP_JS_URL = STATIC_LIB_URL + 'bootstrap/js/bootstrap.min.js'
#BOOTSTRAP_CSS_URL = STATIC_LIB_URL + 'bootstrap/css/bootstrap.min.css'

COLLISION_JS_URL = STATIC_LIB_URL + 'jquery/jquery-collision.min.js'
DROPZONE_JS_URL = STATIC_LIB_URL + 'dropzone/dropzone.js'  
HALLO_JS_URLS = [STATIC_LIB_URL + 'hallo/rangy-core.js', STATIC_LIB_URL + 'jquery/jquery-ui.js', STATIC_LIB_URL + 'hallo/hallo.js']
NOTY_JS_URLS = [STATIC_LIB_URL + 'noty/jquery.noty.js', STATIC_LIB_URL + 'noty/layouts/top.js', STATIC_LIB_URL + 'noty/themes/default.js']
JQUERY_URL = STATIC_LIB_URL + 'jquery/jquery-1.9.1.min.js'
ENGINE_JS_URL = STATIC_JS_URL + 'engine.js'
ENGINE_JS_INCLUDES = [JQUERY_URL, DROPZONE_JS_URL, COLLISION_JS_URL] + HALLO_JS_URLS + NOTY_JS_URLS + [ENGINE_JS_URL]

ENGINE_CSS_URL = STATIC_CSS_URL + 'engine.css'
FONTAWESOME_CSS_URL = STATIC_LIB_URL + 'font-awesome/css/font-awesome.css'

S3_ACCESS_KEY = 'AKIAIT5VHRH3SYEXEX5Q'
S3_SECRET_KEY = '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'
S3_URL = 'http://s3.amazonaws.com/'
S3_BUCKET = 'dazzledev'
S3_TEMPLATE_FOLDER_NAME = 'templates'
S3_TEMPLATE_FOLDER = '/templates/'
S3_TEMPLATE_URL = S3_URL + S3_BUCKET + S3_TEMPLATE_FOLDER  

