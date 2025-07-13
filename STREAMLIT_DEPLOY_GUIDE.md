# 🚀 Streamlit Cloud 배포 가이드

## 📋 사전 준비사항

1. **GitHub 계정** (무료)
2. **Streamlit Cloud 계정** (무료)
3. **현재 프로젝트 파일들**

## 🔧 1단계: GitHub 저장소 생성

### 1.1 GitHub에서 새 저장소 생성
1. [GitHub.com](https://github.com)에 로그인
2. 우측 상단의 **"+"** 버튼 클릭 → **"New repository"** 선택
3. 저장소 이름: `lotto-recommender` (또는 원하는 이름)
4. **Public** 선택 (무료 배포를 위해 필수)
5. **"Create repository"** 클릭

### 1.2 로컬에서 Git 초기화
```bash
# 현재 디렉토리에서
git init
git add .
git commit -m "Initial commit: Lotto recommender app"
git branch -M main
git remote add origin https://github.com/[YOUR_USERNAME]/lotto-recommender.git
git push -u origin main
```

## 🌐 2단계: Streamlit Cloud 배포

### 2.1 Streamlit Cloud 가입
1. [share.streamlit.io](https://share.streamlit.io) 방문
2. **"Sign in"** 클릭
3. **"Continue with GitHub"** 선택
4. GitHub 계정으로 로그인

### 2.2 앱 배포
1. **"New app"** 버튼 클릭
2. 설정 입력:
   - **Repository**: `[YOUR_USERNAME]/lotto-recommender`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
3. **"Deploy!"** 버튼 클릭

### 2.3 배포 완료
- 배포가 완료되면 자동으로 URL이 생성됩니다
- 예: `https://lotto-recommender-[username].streamlit.app`

## 📁 필요한 파일 구조

```
lotto-recommender/
├── streamlit_app.py          # 메인 앱 파일
├── requirements.txt          # 패키지 의존성
├── .streamlit/
│   └── config.toml          # Streamlit 설정
├── README.md                # 프로젝트 설명
└── STREAMLIT_DEPLOY_GUIDE.md # 이 가이드
```

## 🔍 문제 해결

### 배포 실패 시
1. **requirements.txt 확인**: 모든 패키지가 정확히 명시되어 있는지 확인
2. **파일 경로 확인**: `streamlit_app.py`가 루트 디렉토리에 있는지 확인
3. **GitHub 저장소 공개**: Private 저장소는 무료 배포가 불가능

### 로컬 테스트
```bash
streamlit run streamlit_app.py
```

## 🎯 성공적인 배포 후

1. **URL 공유**: 생성된 Streamlit URL을 노션에 추가
2. **스크린샷 촬영**: 배포된 앱의 스크린샷을 노션에 업로드
3. **README 업데이트**: GitHub 저장소에 프로젝트 설명 추가

## 💡 팁

- **무료 플랜**: 월 1,000시간 무료 (충분함)
- **자동 배포**: GitHub에 코드를 푸시하면 자동으로 재배포
- **실시간 로그**: Streamlit Cloud에서 실시간 로그 확인 가능
- **커스텀 도메인**: 유료 플랜에서 가능

## 🆘 도움이 필요하면

1. **Streamlit 문서**: [docs.streamlit.io](https://docs.streamlit.io)
2. **Streamlit 커뮤니티**: [discuss.streamlit.io](https://discuss.streamlit.io)
3. **GitHub Issues**: 프로젝트 저장소에서 이슈 생성

---

**🎉 축하합니다! 이제 전 세계 누구나 접근할 수 있는 로또 추천 시스템을 만들었습니다!** 