# 설치가 막히면 https://www.daleseo.com/python-venv/ 참고하기
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(
    '/Users/junyounglee/Dropbox/PyCharmProjectForDropbox/pythonProject3/koreanki-firebase-adminsdk-ft7zn-19bfdc233c.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
}

card_type = db.collection(u'card type').document(
    u'cloze').collection(u'Field').document('3').set(data)
