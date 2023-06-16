from flask import Flask, render_template,url_for, request, jsonify
from controllers.ligar_controller import ligar_bp
from controllers.login_controller import login_bp
from controllers.usuario_controller import usuario_bp
from controllers.produto_controller import produtos_bp
from controllers.listar_clientes_controller import listar_clientes_bp
from controllers.carrinho_controller import carrinho_bp
from controllers.pagamento_controller import pagamento_bp
from controllers.atualizar_cliente_controller import atualizar_cliente_bp
from controllers.atualizar_sensor_controller import atualizar_sensor_bp
from controllers.atualizar_microcontrolador_controller import atualizar_microcontrolador_bp
from controllers.atualizar_atuador_controller import atualizar_atuador_bp
from controllers.iot_controller import iot
from controllers.cadastrar_iot_controller import cadastro_iot
from controllers.listar_dispositivos_controller import listar_dispositivos_bp
from models.db import db, instance
from models.mqtt import mqtt_client, topic_subscribe
from datetime import datetime
from flask_mqtt import Mqtt
from models.iot.leitura import Leitura
from controllers.listar_menssagem_controller import listar_menssagem_bp



def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                static_folder="./static/", 
                root_path="./")


    app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True
    app.config["SQLALCHEMY_DATABASE_URI"] = instance

    mqtt_client.init_app(app)
    db.init_app(app)

    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'


    app.register_blueprint(ligar_bp, url_prefix='/ligar')
    app.register_blueprint(login_bp, url_prefix='/login')
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(produtos_bp, url_prefix='/produtos')
    app.register_blueprint(listar_clientes_bp,url_prefix='/listar_clientes')
    app.register_blueprint(carrinho_bp, url_prefix='/carrinho')
    app.register_blueprint(pagamento_bp, url_prefix='/pagamento')
    app.register_blueprint(atualizar_cliente_bp, url_prefix='/atualizar_cliente')
    app.register_blueprint(atualizar_sensor_bp, url_prefix='/atualizar_sensor')
    app.register_blueprint(atualizar_microcontrolador_bp,url_prefix='/atualizar_microcontrolador')
    app.register_blueprint(atualizar_atuador_bp, url_prefix='/atualizar_atuador')
    app.register_blueprint(cadastro_iot, url_prefix= '/cadastro_sensor')
    app.register_blueprint(listar_dispositivos_bp, url_prefix='/listar_dispositivos')
    app.register_blueprint(iot, url_prefix="/iot")
    app.register_blueprint(listar_menssagem_bp, url_prefix='/listar_mensagem')
    
    

    @app.route('/')
    def index():
        return render_template('login.html')

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            for topic in topic_subscribe:   
                mqtt_client.subscribe(topic)
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
        )
        with app.app_context():
            leitura = Leitura(date_time=datetime.now(), message=message.payload.decode())
            db.session.add(leitura)
            db.session.commit()

        print('Received message on topic: {topic} with payload: {payload}'.format(**data))
        

    
    return app
    