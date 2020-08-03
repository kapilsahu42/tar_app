import requests
import urllib.request 
import json
import pytest
import re

API_URL="http://localhost:5001/"
TOKEN_URL=API_URL+'auth'
username='bob'
password='abcd'
headers = {'Content-Type': 'application/json'}

def pytest_namespace():
    return {'token': None}

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def test_update_token():
    try:
        response = requests.post(TOKEN_URL,headers=headers,json={'username':username ,'password':password}) 
        assert response.status_code==200
        pytest.token = json.loads(response.text)['access_token']
        headers['Authorization'] = 'JWT'+" "+pytest.token
    except Exception as e:
        print(f"Exception while getting token, {e}")

def test_file_upload():
    with open('test.tar') as fp:
        content = fp.read()
    response = requests.post(
        f'{API_URL}/files/kapil1.tar',headers=headers, data=content
    )
    assert response.status_code==201

def test_file_download():
    filename='kapil.pdf'
    file_url=API_URL+f'files/{filename}'
    r = requests.get(file_url,headers=headers)
    print (r.headers.get('content-type'))
    returned_filename = get_filename_from_cd(r.headers.get('content-disposition'))
    assert filename==returned_filename

def test_list_files():
    response = requests.get('{}/files'.format(API_URL),headers=headers)
    print(response.text)
    assert response.status_code==200