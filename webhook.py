from flask import Flask, request, jsonify
import json
import base64

app = Flask(__name__)

@app.route('/mutate', methods=['POST'])
def mutate():
    admission_review = request.get_json()

    # Extract the UID to send back
    uid = admission_review['request']['uid']

    # Set the environment label
    environment_label = "production"  # Customize as needed

    # Create the JSON patch
    patch = [
        {
            "op": "add",
            "path": "/metadata/labels/environment",
            "value": environment_label
        }
    ]

    # Encode patch to base64
    patch_bytes = json.dumps(patch).encode('utf-8')
    patch_base64 = base64.b64encode(patch_bytes).decode('utf-8')

    # Create the AdmissionReview response
    response = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": uid,
            "allowed": True,
            "patchType": "JSONPatch",
            "patch": patch_base64
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=443,
        ssl_context=('/etc/webhook-certs/tls.crt', '/etc/webhook-certs/tls.key')
    )

