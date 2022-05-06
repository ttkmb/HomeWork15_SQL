from flask import Flask, jsonify
from utils import connect

app = Flask(__name__)


@app.route("/<int:id>")
def get_smt(id):
    query = f"""
            SELECT id, age_upon_outcome, animal_id, animal_type, "name", date_of_birth, outcome_id, breed_id
            FROM animals_finally
            WHERE id = {id}
    """
    response = connect(query)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
