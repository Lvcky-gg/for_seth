# from flask_app import app
# import json

# def test_index_route():
#     response = app.test_client().get('/')

#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Hello World'


# def test_example_by_id():
#     response = app.test_client().get('/examples/1')
#     res = json.loads(response.data.decode('utf-8')).get("examples")
#     assert res["example_text"] == "THIS IS A TEST"