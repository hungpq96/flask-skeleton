from app import create_app, configs


app = create_app(configs.DevConfig)

if __name__ == '__main__':
    app.run()
