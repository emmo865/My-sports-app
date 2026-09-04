import streamlit as st
import pandas as pd

# 1. Setup the App Page
st.set_page_config(page_title="Pro-Stats Tracker", page_icon="⚽")

st.title("⚽ Pro-Stats Player Tracker")
st.write("Search, Analyze, and Compare your favorite football stars.")

# 2. The Database (The 'Brain' of your app)
players_db = {
    "Lionel Messi": {"goals": 821, "assists": 361, "matches": 1047, "image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Messi"},
    "Cristiano Ronaldo": {"goals": 873, "assists": 249, "matches": 1204, "image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Ronaldo"},
    "Kylian Mbappe": {"goals": 322, "assists": 154, "matches": 432, "image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Mbappe"},
    "Erling Haaland": {"goals": 235, "assists": 52, "matches": 288, "image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Haaland"},
    "Neymar Jr": {"goals": 436, "assists": 248, "matches": 709, "image": "https://api.dicebear.com/7.x/avataaars/svg?seed=Neymar"}
}

# 3. Sidebar for Navigation
st.sidebar.header("Options")
mode = st.sidebar.radio("Choose Mode:", ["Single Player Search", "Head-to-Head Comparison"])

# 4. Mode 1: Single Player Search
if mode == "Single Player Search":
    selected_player = st.selectbox("Select a player:", list(players_db.keys()))
    
    data = players_db[selected_player]
    gi = data["goals"] + data["assists"]
    gpm = data["goals"] / data["matches"]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(data["image"], width=150)
    with col2:
        st.subheader(f"Stats for {selected_player}")
        st.metric("Total Goals", data["goals"])
        st.metric("Goal Involvement (G+A)", gi)
        st.write(f"Goals Per Match: {gpm:.2f}")

# 5. Mode 2: Head-to-Head Comparison
else:
    st.subheader("Compare Players")
    colA, colB = st.columns(2)
    
    with colA:
        p1 = st.selectbox("Player 1", list(players_db.keys()), index=0)
    with colB:
        p2 = st.selectbox("Player 2", list(players_db.keys()), index=1)
    
    stats1 = players_db[p1]
    stats2 = players_db[p2]
    
    comparison_data = {
        "Metric": ["Goals", "Assists", "Matches"],
        p1: [stats1["goals"], stats1["assists"], stats1["matches"]],
        p2: [stats2["goals"], stats2["assists"], stats2["matches"]]
    }
    
    df = pd.DataFrame(comparison_data)
    st.table(df)
    
    if stats1["goals"] > stats2["goals"]:
        st.success(f"🔥 {p1} has scored more goals!")
    else:
        st.success(f"🔥 {p2} has scored more goals!")

st.info("💡 To add more players, just add them to the 'players_db' list in the code!")

import streamlit as st

# تنظیمات ظاهری اپلیکیشن حرفه‌ای
st.set_page_config(page_title="Football Gold Stats", layout="wide")

# دیتابیس با بخش ویژه (Premium)
players_db = {
    "Lionel Messi": {"goals": 821, "premium_stat": "Expected Goals (xG): 0.85 per game", "shop_link": "https://example.com/messi-jersey"},
    "Cristiano Ronaldo": {"goals": 873, "premium_stat": "Win Rate: 72%", "shop_link": "https://example.com/ronaldo-boots"},
}

st.title("🏆 Football Gold Stats & Predictions")
st.sidebar.markdown("### 💎 اکانت ویژه")
is_premium = st.sidebar.checkbox("فعالسازی بخش VIP (اشتراکی)")

# جایگاه تبلیغات (Money Maker 1)
st.sidebar.info("⚽ تبلیغات: خرید استوک‌های ورزشی با کد تخفیف ASTRA")

selected_player = st.selectbox("انتخاب بازیکن برای تحلیل:", list(players_db.keys()))

col1, col2 = st.columns(2)

with col1:
    st.metric("تعداد کل گل‌ها", players_db[selected_player]["goals"])
    # دکمه خرید (Money Maker 2 - Affiliate Marketing)
    st.link_button(f"🛒 خرید کیت اختصاصی {selected_player}", players_db[selected_player]["shop_link"])

with col2:
    if is_premium:
        st.success("✅ آمار حرفه‌ای (مخصوص کاربران ویژه)")
        st.write(players_db[selected_player]["premium_stat"])
    else:
        st.warning("🔒 آمار پیشرفته و پیش‌بینی بازی بعد قفل است.")
        if st.button("خرید اشتراک برای باز شدن قفل"):
            st.write("در حال انتقال به درگاه پرداخت...")

# بخش تحلیل هوشمند (Money Maker 3)
st.markdown("---")
st.subheader("🤖 پیش‌بینی هوشمند")
st.write("بر اساس آمار، احتمال گلزنی این بازیکن در بازی بعدی ۶۵٪ است.")
