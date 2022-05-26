from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse
import openai
from gpt import GPT, Example
#태영 - cors 오류 해결하기 위해 $pip install flask_cors 해줌
from flask_cors import CORS

openai.api_key = "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"

app=Flask(__name__)

#태영 - cors 추가 : 모든 곳에서 호출하는 것을 허용하게 함.
CORS(app)

api=Api(app)
app.config['DEBUG']=True


@api.route('/gpt')
class testAPI(Resource):
        def get(self):
                return jsonify({"result":"연결 성공 from flask"})
        def post(self):
                #prompt값 노드에서 받아와야 됨
                parsed_request=request.json.get('content')
                
                print(parsed_request)
                gpt = GPT(engine="davinci",temperature=0.3,max_tokens=200)
                gpt.add_example(Example(
                        "흰 눈이 펄펄 내린다\n\n###\n\n",
                        " 싹트네 싹터요 내 마음에 사랑이\n싹트네 싹터요 내 마음에 사랑이\n 밀려오는 파도처럼 내 마음에 사랑이 \n싹트네 싹터요 내 마음에 사랑이\n"))
                gpt.add_example(Example(
                        "나는 눈이 좋아서\n\n###\n\n",
                        " 나는 눈이 좋아서\n 꿈에 눈이 오나 봐\n 온 세상이 모두 하얀 나라였지\n 어젯밤 꿈 속에\n 썰매를 탔죠 눈싸움 했죠\n 커다란 눈사람도 만들었죠\n 나는 눈이 좋아서\n"))
                gpt.add_example(Example(
                        "눈은 어디있나 요기 여기\n\n###\n\n",
                        " 눈은 어디있나 요기 코는 어디있나 요기\n 귀는 어디있나 요기 입은 어디 있을까 요기\n 엄마눈은 어디있나 여기 엄마 코는 어디있나 여기\n 엄마귀는 어디있나 여기 입은 어디 있을까 여기\n"))
                gpt.add_example(Example(
                        "토실토실 아기 돼지\n\n##\n\n",
                        " 토실토실 아기돼지 젖달라고 꿀꿀꿀\n엄마돼지 오냐오냐 알았다고 꿀꿀꿀\n꿀꿀 꿀꿀 꿀꿀 꿀꿀\n꿀꿀꿀꿀 꿀꿀꿀꿀 꿀꿀꿀꿀꿀\n아기돼지 바깥으로 나가자고 꿀꿀꿀\n엄마돼지 비가와서 안된다고 꿀꿀꿀"))
                gpt.add_example(Example(
                        "아기 돼지 형제 \n\n##\n\n",
                        " 첫 번째 돼지가 집을 짓는데\n짚으로 짚으로 집을 짓는데\n늑대가 나타나 후~~~~~~~~~~~~~\n날아가버렸데요 \n뿅!!!!\n두 번째 돼지가 집을 짓는데\n짚으로 짚으로 집을 짓는데\n늑대가 나타나 후~~~~~~~~~~~~~\n날아가버렸데요 \n뿅!!!!"))
                gpt.add_example(Example(
                        "통통한 아기돼지 \n\n##\n\n",
                        " 통통한 아기돼지 젖달라고 꿀꿀꿀\n엄마돼지 오냐오냐 알았다고 꿀꿀꿀\n꿀꿀 꿀꿀 꿀꿀 꿀꿀\n꿀꿀꿀꿀 꿀꿀꿀꿀 꿀꿀꿀꿀꿀\n통통한 아귀돼지 배고파서 꿀꿀꿀\n엄마돼지 비가와서 안된다고 꿀꿀꿀"))
                gpt.add_example(Example(
                        "귀여운 아기돼지\n\n##\n\n",
                        " 귀여운 아기돼지 배고파서 꿀꿀꿀\n엄마돼지 오냐오냐 알았다고 꿀꿀꿀\n꿀꿀 꿀꿀 꿀꿀 꿀꿀\n꿀꿀꿀꿀 꿀꿀꿀꿀 꿀꿀꿀꿀꿀\n귀여운 아기돼지 나가자고 꿀꿀꿀\n엄마돼지 비가와서 안된다고 꿀꿀꿀"))
                gpt.add_example(Example(
                        "작은 동물원\n\n###\n\n",
                        " 삐약삐약 병아리 음메음메 송아지\n 따당따당 사냥꾼 뒤뚱뒤뚱 물오리\n 푸푸 개구리 집게집게집게 가재\n 푸르르르르르르 물풀 하나 둘 셋 넷 소라\n "))
                gpt.add_example(Example(
                        "코끼리 아저씨는\n\n###\n\n",
                        " 코끼리 아저씨는 코가 손이래\n 과자를 주면은 코로 받지요\n 코끼리 아저씨는 소방소래요\n 불이 나면 빨리와 모셔가지요\n 코끼리 아저씨는 코가 손이래\n 과자를 주면은 코로 받지요\n"))
                
                str="\n\n##\n\n"
                prompt = parsed_request+str
                output = gpt.submit_request(prompt)
                return output.choices[0]['text'];

if __name__=='__main__':
        app.run(debug=True)
        
