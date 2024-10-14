import joblib
from flask import Flask, request, jsonify
import yaml
import pandas as pd

model = joblib.load('./models/model.pkl')

app = Flask('predict_nba')

def get_data_fields():
        with open('./data/features_names.yaml', 'r') as file:
                features_names = yaml.safe_load(file)
        return features_names['features_names']

@app.route('/predict', methods=['POST'])
def predict():
        nba_player = request.get_json()
        nba_player = pd.DataFrame(nba_player, columns=nba_player.keys(), index=[0])
        features_names = get_data_fields()

        # vérification des données
        for feature in features_names:
                if feature not in nba_player:
                        return jsonify({'Erreur': f'Donnée Manquante: {feature}'}), 400
                
        # prédiction
        prediction = model.predict(nba_player[features_names])
        return jsonify({'prediction': prediction[0]})

if __name__=='__main__':
        app.run(debug=True, host='0.0.0.0', port=1717)