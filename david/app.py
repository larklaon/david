# Flask 웹 프레임워크와 필요한 모듈들을 가져옵니다.
from flask import Flask, request, Response, render_template
import os
import socket  # 추가된 import
from io import BytesIO
from gtts import gTTS
import base64
from datetime import datetime

# 기본 언어 설정 (환경변수에서 가져오거나 기본값 'ko' 사용)
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

# Flask 앱 생성
app = Flask(__name__)

# 지원하는 언어 목록 (보안을 위해 서버에서 검증)
SUPPORTED_LANGUAGES = ['ko', 'en', 'ja', 'es']

def log_user_input(text, lang):
    """
    사용자 입력을 로그 파일에 저장하는 함수
    """
    try:
        # 현재 시간 가져오기
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 로그 내용 작성
        log_entry = f"[{timestamp}] 언어: {lang}, 텍스트: {text}\n"
        
        # input_log.txt 파일에 추가로 저장
        with open('input_log.txt', 'a', encoding='utf-8') as f:
            f.write(log_entry)
            
    except Exception as e:
        # 로그 저장 실패해도 메인 기능은 계속 동작하도록 처리
        print(f"로그 저장 실패: {e}")

def create_audio_from_text(text, lang):
    """
    텍스트를 음성으로 변환하고 base64로 인코딩하는 함수
    """
    try:
        # BytesIO 객체 생성 (메모리에 바이트 데이터 저장)
        fp = BytesIO()
        
        # gTTS로 음성 생성하고 메모리에 저장
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.write_to_fp(fp)

        # 바이트 데이터를 base64로 인코딩
        audio_data = fp.getvalue()
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        
        return audio_base64
        
    except Exception as e:
        # 음성 변환 실패시 None 반환
        print(f"음성 변환 실패: {e}")
        return None

@app.route("/", methods=['GET', 'POST'])
def home():
    """
    메인 페이지 처리 함수
    GET: 입력 폼 표시  
    POST: 음성 변환 처리
    """
    
    # 호스트네임 설정 (render_template 호출 이전에 추가)
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    
    # GET 요청일 때
    if request.method == 'GET':
        return render_template('index.html', computername=hostname)
    
    # POST 요청일 때
    if request.method == 'POST':
        try:
            # 폼 데이터 가져오기
            input_text = request.form.get('input_text', '').strip()
            selected_lang = request.form.get('lang', DEFAULT_LANG)
            
            # 입력 검증
            if not input_text:
                raise ValueError("텍스트를 입력해주세요.")
            
            if selected_lang not in SUPPORTED_LANGUAGES:
                raise ValueError("지원하지 않는 언어입니다.")
            
            # 로그 저장
            log_user_input(input_text, selected_lang)
            
            # 음성 변환
            audio_base64 = create_audio_from_text(input_text, selected_lang)
            
            if audio_base64 is None:
                raise RuntimeError("음성 변환에 실패했습니다.")
            
            # 성공시 결과 반환 (computername 추가)
            return render_template('index.html', 
                                 computername=hostname,
                                 audio=audio_base64,
                                 success=f"'{input_text}' 음성이 생성되었습니다!")
        
        # 사용자 입력 오류 처리
        except ValueError as e:
            return render_template('index.html', computername=hostname, error=str(e))
        
        # 시스템 오류 처리  
        except RuntimeError as e:
            return render_template('index.html', computername=hostname, error=f"{str(e)} 다시 시도해주세요.")
        
        # 예상하지 못한 오류 처리
        except Exception as e:
            print(f"예상하지 못한 오류: {e}")
            return render_template('index.html', 
                                 computername=hostname,
                                 error="시스템 오류가 발생했습니다. 잠시 후 다시 시도해주세요.")

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')

# 메인 실행 부분
if __name__ == '__main__':
    # debug=True 설정
    app.run('0.0.0.0', 80, debug=True)
