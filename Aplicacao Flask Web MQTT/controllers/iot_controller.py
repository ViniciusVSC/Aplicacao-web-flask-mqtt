from flask import Blueprint, request, render_template,jsonify
from models.iot import atuador,sensor,microcontroller, leitura
from flask_login import current_user
from models.mqtt import mqtt_client

iot = Blueprint("iot",__name__,
                static_folder="./static/",
                template_folder="./views/")

@iot.route('/messages')
def check_messages():
    return render_template("list_reads.html", leituras=leitura.Leitura.query.all())


@iot.route('/publish', methods=['GET','POST'])
def publish_message():
    request_data = request.get_json()
    print(request_data)
    publish_result = mqtt_client.publish(request_data['topic'], request_data['message'])
    return jsonify(publish_result)