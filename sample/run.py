import argparse
import sys
import signal

from sample import create_app

try:
    from chaussette.server import make_server
except ImportError:
    def make_server(*args, **kwargs):
        print('Chaussette unavailable on your OS. Killing process.')
        exit(0)

_CONFIG_ENVIRONMENTS = {
    'devel': 'sample.config.DevConfig',
    'prod': 'sample.config.ProdConfig',
    'default': 'sample.config.DefaultConfig'
}


def _quit(sig, frame):
    print("Bye!")
    sys.exit(0)


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Flask Docker Template')

    parser.add_argument('--fd',
                        type=int,
                        default=None)
    parser.add_argument('--config-env', "-c", help='Configuration Environment',
                        type=str,
                        dest='config',
                        choices=_CONFIG_ENVIRONMENTS.keys(),
                        default='default')
    args = parser.parse_args(args)
    config_env = args.config

    app = create_app(_CONFIG_ENVIRONMENTS[config_env])
    port = app.config.get('PORT', 5000)
    host = app.config.get('HOST', '127.0.0.1')


    signal.signal(signal.SIGINT, _quit)
    signal.signal(signal.SIGTERM, _quit)

    if args.fd is not None:
        httpd = make_server(app, host=f'fd://{args.fd}')
        httpd.serve_forever()
    else:
        app.run(host=host, port=port)


if __name__ == "__main__":
    main()
