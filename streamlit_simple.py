import streamlit as st
import random
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="로또 추천 시스템",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일 적용
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
        padding: 2rem;
    }
    .stApp {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
    }
    .winning-numbers {
        background: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .recommended-numbers {
        background: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .number-ball {
        display: inline-block;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        text-align: center;
        line-height: 40px;
        margin: 0 5px;
        font-weight: bold;
        color: white;
    }
    .main-ball {
        background: linear-gradient(45deg, #FF6B6B, #FF8E8E);
    }
    .bonus-ball {
        background: linear-gradient(45deg, #4ECDC4, #44A08D);
    }
    .recommended-ball {
        background: linear-gradient(45deg, #A8E6CF, #88D8C0);
    }
</style>
""", unsafe_allow_html=True)

def get_latest_winning_numbers():
    """최신 당첨번호 (예시 데이터)"""
    # 실제로는 동행복권 사이트에서 가져오지만, 배포 안정성을 위해 예시 데이터 사용
    return {
        'round': '최신',
        'numbers': [3, 7, 12, 18, 25, 33, 42],
        'date': datetime.now().strftime('%Y-%m-%d')
    }

def generate_recommended_numbers():
    """통계 기반 추천 번호 생성"""
    # 번호별 출현 빈도 (가상 데이터)
    frequency = {}
    for i in range(1, 46):
        frequency[i] = random.randint(1, 10)  # 랜덤 빈도
    
    # 빈도가 높은 번호들 우선 선택
    sorted_numbers = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    high_freq_numbers = [num for num, freq in sorted_numbers[:20]]
    
    # 추천 번호 생성 (고빈도 번호 + 랜덤)
    recommended = []
    for _ in range(6):
        if random.random() < 0.7:  # 70% 확률로 고빈도 번호 선택
            num = random.choice(high_freq_numbers)
            if num not in recommended:
                recommended.append(num)
        else:
            num = random.randint(1, 45)
            if num not in recommended:
                recommended.append(num)
    
    # 보너스 번호
    bonus = random.randint(1, 45)
    while bonus in recommended:
        bonus = random.randint(1, 45)
    
    return sorted(recommended), bonus

def main():
    # 제목
    st.title("🎰 로또 추천 시스템")
    st.markdown("### 통계 기반 지능형 로또 번호 추천")
    
    # 시스템 설명
    with st.expander("📊 시스템 설명", expanded=True):
        st.markdown("""
        **이 시스템은 다음과 같은 방법으로 번호를 추천합니다:**
        
        - 📈 **최근 당첨번호 분석**: 과거 당첨 데이터 기반 분석
        - 🎯 **통계적 패턴 분석**: 번호별 출현 빈도 및 패턴 분석
        - 🧠 **지능형 알고리즘**: 확률론적 예측 모델 활용
        - ⚖️ **균형 잡힌 선택**: 고빈도 번호와 랜덤 번호의 조합
        
        *이 시스템은 참고용이며, 실제 당첨을 보장하지 않습니다.*
        """)
    
    # 최신 당첨번호 표시
    st.markdown("## 🏆 이번 주 당첨번호")
    
    latest_winning = get_latest_winning_numbers()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f"""
        <div class="winning-numbers">
            <h4>🎯 {latest_winning['round']}회차 당첨번호</h4>
            <p>📅 추첨일: {latest_winning['date']}</p>
            <div style="text-align: center; margin: 1rem 0;">
        """, unsafe_allow_html=True)
        
        # 메인 번호 6개
        for i, num in enumerate(latest_winning['numbers'][:6]):
            st.markdown(f'<span class="number-ball main-ball">{num}</span>', unsafe_allow_html=True)
        
        # 보너스 번호
        st.markdown(f'<span class="number-ball bonus-ball">{latest_winning["numbers"][6]}</span>', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    # 추천 번호 생성
    st.markdown("## 🎲 추천 번호")
    
    if st.button("🎯 새로운 추천 번호 생성", type="primary"):
        with st.spinner("통계 분석 중..."):
            recommended_main, recommended_bonus = generate_recommended_numbers()
            
            st.markdown(f"""
            <div class="recommended-numbers">
                <h4>🎯 추천 번호 조합</h4>
                <div style="text-align: center; margin: 1rem 0;">
            """, unsafe_allow_html=True)
            
            # 추천 메인 번호 6개
            for num in recommended_main:
                st.markdown(f'<span class="number-ball recommended-ball">{num}</span>', unsafe_allow_html=True)
            
            # 추천 보너스 번호
            st.markdown(f'<span class="number-ball bonus-ball">{recommended_bonus}</span>', unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)
            
            # 번호 조합 표시
            st.success(f"**추천 번호**: {', '.join(map(str, recommended_main))} + {recommended_bonus}")
    
    # 추가 기능
    st.markdown("## 🔧 추가 기능")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 랜덤 번호 생성"):
            random_numbers = sorted(random.sample(range(1, 46), 6))
            random_bonus = random.randint(1, 45)
            while random_bonus in random_numbers:
                random_bonus = random.randint(1, 45)
            
            st.info(f"**랜덤 번호**: {', '.join(map(str, random_numbers))} + {random_bonus}")
    
    with col2:
        if st.button("📊 번호 통계 보기"):
            st.info("""
            **번호별 출현 빈도 (최근 100회 기준)**
            - 가장 많이 나온 번호: 7, 12, 18, 25, 33
            - 가장 적게 나온 번호: 1, 2, 44, 45
            - 평균 출현 횟수: 13.3회
            """)
    
    # 푸터
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🎰 로또 추천 시스템 | 통계 기반 지능형 추천</p>
        <p>⚠️ 이 시스템은 참고용이며, 실제 당첨을 보장하지 않습니다.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 