from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# PostgreSQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_db_user:your_db_password@your_db_host/your_db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Seat Model
class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(10), unique=True, nullable=False)
    is_booked = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    return jsonify({"message": "Shree Samarth Krupa Tours and Travels API is running!"})

@app.route('/seats', methods=['GET'])
def get_seats():
    seats = Seat.query.all()
    seat_data = [{"seat_number": seat.seat_number, "is_booked": seat.is_booked} for seat in seats]
    return jsonify(seat_data)

@app.route('/book-seat', methods=['POST'])
def book_seat():
    data = request.json
    seat_number = data.get('seat_number')

    seat = Seat.query.filter_by(seat_number=seat_number).first()
    if seat and not seat.is_booked:
        seat.is_booked = True
        db.session.commit()
        return jsonify({"message": "Seat booked successfully!"})
    return jsonify({"error": "Seat already booked or does not exist"}), 400

if __name__ == '__main__':
    app.run(debug=True)
