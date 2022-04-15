# 설치가 막히면 https://www.daleseo.com/python-venv/ 참고하기
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(
    '/Users/junyounglee/Dropbox/PyCharmProjectForDropbox/pythonProject3/koreanki-firebase-adminsdk-ft7zn-19bfdc233c.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'product')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
