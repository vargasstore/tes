from flask import Flask, jsonify
from scraper import get_kuota_prices, get_diamond_ml, get_diamond_ff

app = Flask(__name__)

@app.route("/api/kuota", methods=["GET"])
def kuota_data():
    url_kuota = "https://orderkuota.com/harga/kuota-axis/axis-mini-voucher-1-3-hari#collapse_kuota_axis"
    data = get_kuota_prices(url_kuota, margin_percentage=10)
    return jsonify(data)

@app.route("/api/diamond/ml", methods=["GET"])
def diamond_ml_data():
    url_ml = "https://example.com/harga/diamond-ml"  # Ganti dengan URL asli untuk diamond ML
    data = get_diamond_ml(url_ml, margin_percentage=10)
    return jsonify(data)

@app.route("/api/diamond/ff", methods=["GET"])
def diamond_ff_data():
    url_ff = "https://example.com/harga/diamond-ff"  # Ganti dengan URL asli untuk diamond FF
    data = get_diamond_ff(url_ff, margin_percentage=10)
    return jsonify(data)

# Untuk endpoint gabungan, misalnya:
@app.route("/api/all", methods=["GET"])
def all_data():
    url_kuota = "https://orderkuota.com/harga/kuota-axis/axis-mini-voucher-1-3-hari#collapse_kuota_axis"
    url_ml = "https://example.com/harga/diamond-ml"
    url_ff = "https://example.com/harga/diamond-ff"
    
    kuota = get_kuota_prices(url_kuota, margin_percentage=10)
    ml = get_diamond_ml(url_ml, margin_percentage=10)
    ff = get_diamond_ff(url_ff, margin_percentage=10)
    
    data = {
        "kuota": kuota,
        "diamond_ml": ml,
        "diamond_ff": ff
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)