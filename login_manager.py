from flask_login import ID_ATTRIBUTE, LOGIN_MESSAGE, LOGIN_MESSAGE_CATEGORY, REFRESH_MESSAGE, AnonymousUserMixin


class LoginManager:
    def __init__(self, app=None, add_context_processor=True):
        
        self.anonymous_user = AnonymousUserMixin
        
        self.login_view = None
        
        self.blueprint_login_views = {}
        
        self.login_message = LOGIN_MESSAGE
        
        self.login_message_category = LOGIN_MESSAGE_CATEGORY
        
        self.refresh_view = None
        
        self.needs_refresh_message = REFRESH_MESSAGE
        
        self.session_protection = "basic"
        
        self.localize_callback = None
        
        self.unauthorized_callback = None
        
        self.id_attribute = ID_ATTRIBUTE
        
        self._user_callback = None

        self._header_callback = None

        self._request_callback = None

        self._session_identifier_generator = _create_identifier
        
        if app is not None:
            self.init_app(app, add_context_processor)