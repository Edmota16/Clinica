from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/api/paciente", methods=['GET'])
def obterPacientes():
    data = supabase.table("paciente").select("*").execute()
    return jsonify(data.data)

@app.route("/api/paciente/<int:id>", methods=['GET'])
def obterPacienteId(id):
    data = supabase.table("paciente").select("*").eq("id", id).execute()
    return jsonify(data.data)

@app.route("/api/paciente", methods=['POST'])
def adicionarPaciente():  
    paciente = request.json

    if "id" in paciente:
        paciente.pop("id")
        
    data = supabase.table("paciente").insert(paciente).execute()
    return jsonify(data.data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)