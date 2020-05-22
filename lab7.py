from flask import Flask, request, jsonify, abort, make_response
from datetime import datetime
import sqlite3

app=Flask(__name__)

conn = sqlite3.connect('data.db')
c = conn.cursor()
conn.commit()
c.execute('SELECT * FROM students')
ids = c.fetchall()
print(ids)

@app.route('/')
def start():
	return 'Start'

@app.route('/students',methods=['GET'])
def get_students():
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	c.execute('SELECT * FROM students')
	ids = c.fetchall()
	print(ids)
	return jsonify(ids)
	c.close()
	conn.close()
		
@app.route('/students/<student_id>',methods=['GET'])
def get_student(student_id):
	a=student_id
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	c.execute('SELECT s.first_name,s.last_name,g.name FROM students s JOIN gruppi g ON s.groupId=g.id  WHERE s.groupId=? and s.id=?',(a,a))
	ids=c.fetchall()
	return jsonify(ids)
	c.close()
	conn.close()
		
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}),404)

@app.route('/students',methods=['POST'])
def create_student():
	if not request.json or not 'firstName' or not 'lastName' or not 'group' in request.json:
		abort(400)
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	a=request.json.get('firstName')
	b=request.json.get('lastName')
	f=request.json.get('group')
	c.execute('INSERT INTO students(first_name,last_name,groupId) VALUES(?, ?, ? )',(a,b,f))
	conn.commit()
	return "Готово!"
	c.close()
	conn.close()

@app.route('/students/<student_id>',methods=['PUT'])
def update_student(student_id):
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	student=student_id
	if len(student)==0:
		abort(404)
	if not request.json:
		abort(404)
	if 'firstName' in request.json:
		a=request.json.get('firstName')
		c.execute('UPDATE students SET first_name=? WHERE id=? ',(a,student))
		conn.commit()
	if 'lastName' in request.json:
		b=request.json.get('lastName')
		c.execute('UPDATE students SET last_name=? WHERE id=? ',(b,student))
		conn.commit()
	if 'group' in request.json:
		f=request.json.get('groupId')
		c.execute('UPDATE students SET groupId=? WHERE id=? ',(f,gruppa))
		conn.commit()
	return "Готово!"
	c.close()
	conn.close()

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
	student =student_id
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	c.execute('DELETE FROM students WHERE id=? ', (student))
	conn.commit()
	return "Готово!"
	c.close()
	conn.close()

@app.route('/groups',methods=['GET'])
def get_groups():
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	c.execute('SELECT * FROM gruppi')
	ids = c.fetchall()
	print(ids)
	return jsonify(ids)
	c.close()
	conn.close()

@app.route('/groups/<group_id>', methods=['DELETE'])
def delete_group(group_id):
	groupz =group_id
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	c.execute('DELETE FROM gruppi WHERE id=? ', (groupz))
	conn.commit()
	return "Готово!"
	c.close()
	conn.close()


@app.route('/groups',methods=['POST'])
def create_group():
	if not request.json or not 'name' in request.json:
		abort(400)
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	conn.commit()
	a=request.json.get('name')
	c.execute('INSERT INTO gruppi(name) VALUES(?)',(a))
	conn.commit()
	return "Готово!"
	c.close()
	conn.close()	

if __name__=='__main__':
	app.run()