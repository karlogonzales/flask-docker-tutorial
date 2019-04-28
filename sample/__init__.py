from flask import Flask, jsonify, make_response
from flask_cors import CORS
__version__ = '0.0.1'


def create_app(conf=None):
    app = Flask(__name__)
    CORS(app)
    if conf:
        app.config.from_object(conf)
    else:
        app.config.from_object(f'sample.config.DefaultConfig')

    @app.route('/version')
    def version():
        return jsonify({"sample": __name__, "version": __version__})

    @app.errorhandler(404)
    def page_not_found(e):
        return make_response(jsonify({"error": True, "code": 404, "msg": str(e)}), 404)

    @app.errorhandler(405)
    def page_not_found(e):
        return make_response(jsonify({"error": True, "code": 405, "msg": str(e)}), 405)

    @app.errorhandler(400)
    def bad_request(e):
        return make_response(jsonify({"error": True, "code": 400, "msg": str(e)}), 400)

    @app.errorhandler(500)
    def internal_error(e):
        return make_response(jsonify({"error": True, "code": 500, "msg": str(e)}), 500)

    from sample.api import bp
    app.register_blueprint(bp)

    return app
