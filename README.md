# 🎰 로또 추천 시스템

통계 기반 지능형 로또 번호 추천 웹 애플리케이션입니다.

## 🌟 주요 기능

- **📊 통계 기반 추천**: 실제 당첨 데이터를 기반으로 한 과학적 분석
- **🏆 실시간 당첨번호**: 동행복권 사이트에서 최신 당첨번호 자동 수집
- **🎯 지능형 알고리즘**: 머신러닝 기반 예측 모델 활용
- **⚖️ 균형 잡힌 선택**: 고빈도 번호와 랜덤 번호의 조합
- **🎨 아름다운 UI**: 황금 테마의 현대적인 디자인

## 🚀 배포된 앱

**🌐 라이브 데모**: [Streamlit Cloud에서 확인하기](https://share.streamlit.io)

## 🛠️ 기술 스택

- **Backend**: Python, Streamlit
- **Data Processing**: Pandas, NumPy
- **Web Scraping**: BeautifulSoup, Requests
- **UI/UX**: Streamlit Components, Custom CSS
- **Deployment**: Streamlit Cloud

## 📦 설치 및 실행

### 로컬 실행

1. **저장소 클론**
```bash
git clone https://github.com/[YOUR_USERNAME]/lotto-recommender.git
cd lotto-recommender
```

2. **가상환경 생성 및 활성화**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **패키지 설치**
```bash
pip install -r requirements.txt
```

4. **앱 실행**
```bash
streamlit run streamlit_app.py
```

### 배포

자세한 배포 가이드는 [STREAMLIT_DEPLOY_GUIDE.md](STREAMLIT_DEPLOY_GUIDE.md)를 참조하세요.

## 📁 프로젝트 구조

```
lotto-recommender/
├── streamlit_app.py          # 메인 Streamlit 앱
├── app.py                    # Flask 버전 (로컬용)
├── requirements.txt          # Python 패키지 의존성
├── .streamlit/
│   └── config.toml          # Streamlit 설정
├── templates/
│   └── index.html           # Flask 템플릿
├── static/
│   └── css/
│       └── style.css        # 스타일시트
├── README.md                # 프로젝트 설명
└── STREAMLIT_DEPLOY_GUIDE.md # 배포 가이드
```

## 🎯 사용 방법

1. **최신 당첨번호 확인**: 이번 주 당첨번호를 실시간으로 확인
2. **추천 번호 생성**: "새로운 추천 번호 생성" 버튼 클릭
3. **추가 기능 활용**: 랜덤 번호 생성, 통계 정보 확인

## ⚠️ 주의사항

- 이 시스템은 **참고용**이며, 실제 당첨을 보장하지 않습니다
- 과도한 도박은 위험할 수 있으니 적절한 선에서 즐겨주세요
- 개인 판단을 우선하여 사용하시기 바랍니다

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 연락처

프로젝트 링크: [https://github.com/[YOUR_USERNAME]/lotto-recommender](https://github.com/[YOUR_USERNAME]/lotto-recommender)

---

**🎉 고생하셨습니다! 이제 전 세계 누구나 사용할 수 있는 로또 추천 시스템이 완성되었습니다!** 