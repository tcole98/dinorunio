from app import app, db
from flask import request, jsonify
from .models import User, datetime
from datetime import timedelta
from sqlalchemy import desc

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    user = User(nickname = data['nickname'], score = int(data['score']))
    db.session.add(user)
    db.session.commit()

    return jsonify('success')

@app.route('/getdata', methods=['GET'])
def leaderboard():
    # get leaderboard
    user_data_list = []

    user_object_list = User.query.order_by(desc(User.score)).limit(20).all()
    for user_object in user_object_list:
     user_details = {'nickname': user_object.nickname[0: 15], 'score': user_object.score}
     user_data_list.append(user_details)

    return jsonify(user_data_list)

@app.route('/getdata2', methods=['GET'])
def leaderboard2():
    # get last 24 hours leaderboard
    user_data_list = []

    current_time = datetime.datetime.utcnow()
    twentyfour_hours_ago = current_time - datetime.timedelta(days=1)

    user_object_list = User.query.filter(User.date.between(twentyfour_hours_ago, current_time)).order_by(desc(User.score)).limit(20).all()
    for user_object in user_object_list:
     user_details = {'nickname': user_object.nickname[0: 15], 'score': user_object.score}
     user_data_list.append(user_details)

    return jsonify(user_data_list)

@app.route('/getdata3', methods=['GET'])
def leaderboard3():
    # get weekly leaderboard
    user_data_list = []

    current_time = datetime.datetime.utcnow()
    week_ago = current_time - datetime.timedelta(days=7)

    user_object_list = User.query.filter(User.date.between(week_ago, current_time)).order_by(desc(User.score)).limit(20).all()
    for user_object in user_object_list:
     user_details = {'nickname': user_object.nickname[0: 15], 'score': user_object.score}
     user_data_list.append(user_details)

    return jsonify(user_data_list)


@app.route('/getrecent', methods=['GET'])
def leaderboard4():
    user_data_list = []

    user_object_list = User.query.order_by(desc(User.date)).limit(3).all()
    for user_object in user_object_list:
        user_details = {'nickname': user_object.nickname[0: 15], 'score': user_object.score}
        user_data_list.append(user_details)

    return jsonify(user_data_list)

