from flask import Flask,jsonify, request
from flask_restx import Resource, Api, reqparse
import openai
from gpt import GPT, Example

openai.api_key = "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"

app=Flask(__name__)
api=Api(app)
app.config['DEBUG']=True

@app.route('/dd')
def index():
        return 'hello nice to meet you'

@api.route('/test')
class testAPI(Resource):
        def get(self):
                return jsonify({"result":"연결 성공 from flask"})
        def post(self):
                #prompt값 노드에서 받아와야 됨
                parsed_request=request.json.get('content')
                print(parsed_request)
                gpt = GPT(engine="davinci",temperature=0.5,max_tokens=200)
                gpt.add_example(Example(
                        "싹트네 싹터요\n\n##\n\n",
                        " 싹트네 싹터요 내 마음에 사랑이\n싹트네 싹터요 내 마음에 사랑이\n 밀려오는 파도처럼 내 마음에 사랑이 \n싹트네 싹터요 내 마음에 사랑이END"))
                gpt.add_example(Example(
                        "요리 보고 조리 봐도\n\n##\n\n",
                        " 요리 보고 조리 봐도 음 알 수 없는 둘리 둘리\n빙하 타고 내려와 음 친구를 만났지만 \n일억년 전 옛날이 너무나 그리워 \n보고픈 엄마 찾아 모두 함께 나가자 아 아 \n 외로운 둘리는 귀여운 아기 공룡 호이! 호이!\n둘리는 초능력 내 친구\n외로운 둘리는 귀여운 아기 공룡 호이! 호이!\n둘리는 초능력 재주꾼END"))
                gpt.add_example(Example(
                        "쪼로로롱 산새가\n\n##\n\n",
                        " 쪼로로롱 산새가 노래하는 숲 속에\n예쁜 아기 다람쥐가 살고 있었어요\n울창한 숲속 푸른 나무 위에서 \n아기 다람쥐 또미가 살고 있었어요\n야호! 랄라 노래부르자\n야호! 숲속의 아침을\n야호! 트랄라 귀여운 아기 다람쥐또미END"))
                gpt.add_example(Example(
                        "토실토실 아기돼지\n\n##\n\n",
                        " 토실토실 아기돼지 젖달라고 꿀꿀꿀\n엄마돼지 오냐오냐 알았다고 꿀꿀꿀\n꿀꿀 꿀꿀 꿀꿀 꿀꿀\n꿀꿀꿀꿀 꿀꿀꿀꿀 꿀꿀꿀꿀꿀\n아기돼지 바깥으로 나가자고 꿀꿀꿀\n엄마돼지 비가와서 안된다고 꿀꿀꿀END"))
                gpt.add_example(Example(
                        "허수아비 아저씨\n\n##\n\n",
                        "하루종일 우뚝 서 있는\n성난 허수아비 아저씨\n짹짹짹짹짹 어이 무서워\n새들이 달아납니다\n하루종일 우뚝 서 있는\n 성난 허수아비 아저씨END"))
                gpt.add_example(Example(
                        "혼자서도 잘할 거야\n\n##\n\n",
                        " 거야 거야 할 거야 혼자서도 잘할 거야\n예쁜 짓 고운 짓 혼자서도 잘할 거야\n엄마는 잘한다고 호호호 호호호호\n아빠는 귀엽다고 하하하하 하하하\n거야거야 할 거야 혼자서도 잘할 거야\n 예쁜 짓 고운 짓 혼자서도 잘할 거야END"))
                
                str="\n\n##\n\n"
                prompt = parsed_request+str
                output = gpt.submit_request(prompt)
                return output.choices[0]['text'];

if __name__=='__main__':
        app.run(debug=True)
        



