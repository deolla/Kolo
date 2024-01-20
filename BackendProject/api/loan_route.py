from flask import jsonify, request, Blueprint
from models.loan import Loan
from models.user import User
from datetime import datetime
from models import db

loan_routes = Blueprint('loan_routes', __name__, url_prefix='/loans')

@loan_routes.route('/users/<user_id>/apply_loan', methods=['POST'])
def apply_loan(user_id):
    """Apply for a loan."""
    data = request.json
    loan_type = data.get('loan_type')
    amount = data.get('amount')
    interest = data.get('interest')
    term = data.get('term')

    # Check if the user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Create and store the loan application
    loan = Loan(
        user_id=user_id,
        loan_type=loan_type,
        amount=amount,
        loan_date=datetime.utcnow(),
        interest=interest,
        term=term,
        status='pending'  # Set the initial status to pending
    )

    db.session.add(loan)
    db.session.commit()

    return jsonify({'message': 'Loan application submitted successfully', 'loan': loan.serialize()}), 200

@loan_routes.route('/users/<user_id>/loan_status', methods=['GET'])
def loan_status(user_id):
    """Get the status of a user's loan."""
    loan = Loan.query.filter_by(user_id=user_id).order_by(Loan.loan_date.desc()).first()

    if not loan:
        return jsonify({'message': 'No loan found for the user'}), 404

    return jsonify({'loan_status': loan.status}), 200

@loan_routes.route('/users/<user_id>/loan_history', methods=['GET'])
def loan_history(user_id):
    """Get the loan history for a user."""
    loans = Loan.query.filter_by(user_id=user_id).order_by(Loan.loan_date.desc()).all()

    return jsonify({'loan_history': [loan.serialize() for loan in loans]}), 200

@loan_routes.route('/loans/<loan_id>', methods=['GET'])
def get_loan(loan_id):
    """Get a single loan."""
    loan = Loan.query.filter_by(id=loan_id).first()
    if loan:
        return jsonify(loan.serialize()), 200
    return jsonify({'message': 'Loan not found'}), 404


