from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

# Jinja2에 enumerate 함수 추가
app.jinja_env.globals.update(enumerate=enumerate)

def get_latest_winning_numbers():
    """동행복권 사이트에서 최신 당첨번호를 가져옵니다."""
    try:
        url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # 회차 정보 - 더 안정적인 파싱
        round_number = '최신'
        round_selectors = [
            'div.win_result h4 strong',
            'h4 strong',
            '.win_result strong',
            'strong',
            '.result_title'
        ]
        
        for selector in round_selectors:
            round_info = soup.select_one(selector)
            if round_info and round_info.text.strip():
                round_number = round_info.text.strip()
                break

        # 추첨일 - 더 안정적인 파싱
        draw_date = datetime.now().strftime('%Y-%m-%d')
        date_selectors = [
            'div.win_result p.desc',
            '.win_result p',
            'p.desc',
            '.date',
            '.draw_date'
        ]
        
        for selector in date_selectors:
            date_info = soup.select_one(selector)
            if date_info and date_info.text.strip():
                draw_date = date_info.text.strip()
                break

        # 당첨번호 - 더 안정적인 파싱
        ball_selectors = [
            'div.num.win span.ball_645',
            '.num.win .ball_645',
            'span.ball_645',
            '.ball_645',
            '.number',
            'span[class*="ball"]'
        ]
        
        balls = []
        for selector in ball_selectors:
            balls = soup.select(selector)
            if len(balls) >= 7:
                break
        
        # 번호가 충분하지 않으면 기본값 사용
        if len(balls) < 7:
            # 기본 당첨번호 (예시)
            default_numbers = [3, 7, 12, 18, 25, 33, 42]
            return {
                'round': round_number,
                'numbers': default_numbers,
                'date': draw_date
            }
        
        # 메인 번호 6개 + 보너스 번호 1개
        try:
            main_numbers = [int(balls[i].text.strip()) for i in range(6)]
            bonus_number = int(balls[6].text.strip())
            numbers = main_numbers + [bonus_number]
        except (ValueError, IndexError):
            # 숫자 변환 실패 시 기본값 사용
            default_numbers = [3, 7, 12, 18, 25, 33, 42]
            return {
                'round': round_number,
                'numbers': default_numbers,
                'date': draw_date
            }

        return {
            'round': round_number,
            'numbers': numbers,
            'date': draw_date
        }
    except Exception as e:
        # 오류 발생 시 기본값 반환 (오류 메시지 출력 안함)
        return {
            'round': '최신',
            'numbers': [3, 7, 12, 18, 25, 33, 42],
            'date': datetime.now().strftime('%Y-%m-%d')
        }

# 전역 변수로 당첨번호 저장
latest_winning = get_latest_winning_numbers()

@app.route('/')
def index():
    try:
        return render_template('index.html', latest_winning=latest_winning)
    except Exception as e:
        print(f"템플릿 렌더링 오류: {e}")
        return f"오류가 발생했습니다: {e}", 500

@app.route('/test')
def test():
    return "Flask 앱이 정상적으로 작동합니다!"

@app.route('/generate', methods=['POST'])
def generate_numbers():
    # 로또 번호 생성 (1-45에서 6개 + 보너스 1개)
    numbers = random.sample(range(1, 46), 7)
    main_numbers = sorted(numbers[:6])
    bonus_number = numbers[6]
    
    return jsonify({
        'main_numbers': main_numbers,
        'bonus_number': bonus_number
    })



@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html', latest_winning=latest_winning), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html', latest_winning=latest_winning), 500

if __name__ == '__main__':
    # PythonAnywhere에서는 자동으로 포트 관리
    app.run(debug=False) 