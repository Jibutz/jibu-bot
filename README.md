# 🎓 JIBU — Tanzania's AI NECTA Tutor Bot

JIBU is a production-ready WhatsApp + SMS tutoring bot for Tanzanian Form 1–6 students. It delivers daily NECTA-style exam questions, tracks streaks, collects M-Pesa payments, and sends weekly parent reports — all powered by Claude AI.

---

## 🚀 Quick Start (Railway Deployment)

### 1. Fork / Clone the Repo

```bash
git clone https://github.com/your-org/jibu-bot.git
cd jibu-bot
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Set Up Environment Variables

Copy `.env.example` to `.env` and fill in all values:

```bash
cp .env.example .env
```

### 4. Deploy to Railway

1. Push to GitHub: `git push origin main`
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select your `jibu-bot` repo
4. Add all environment variables from `.env.example` in Railway's Variables tab
5. Railway auto-deploys. Your URL will be: `https://jibu-bot.railway.app`

---

## 🔧 Service Setup

### Airtable

1. Create a free account at [airtable.com](https://airtable.com)
2. Create a base named **Jibu**
3. Create a table named **Students** with these columns (all as Single line text unless noted):

| Field Name | Type |
|---|---|
| Student_Name | Single line text |
| Student_Phone | Single line text |
| Parent_Phone | Single line text |
| Subject | Single line text |
| Form_level | Single line text |
| Subjects | Single line text |
| Current_Streak | Number |
| Longest_Streak | Number |
| Last_Answer_Date | Date |
| Total_Points | Number |
| Rank_Title | Single line text |
| Freeze_Credits | Number |
| Weak_Topics | Long text |
| Strong_Topics | Long text |
| Todays_Correct_Answer | Single line text |
| Status | Single select (Trial, Active, Paused, Enrolling) |
| Subscription_Starts | Date |
| Next_Payment_Date | Date |
| Payment_Amount | Number |
| School_Name | Single line text |
| Days_Until_Exam | Number |
| Channel | Single select (whatsapp, sms) |
| Trial_End_Date | Date |
| Trial_Status | Single line text |
| Enrollment_Step | Number |

4. Get your API key: Account → Developer → Personal access tokens
5. Get your Base ID from the Airtable API page for your base (starts with `app`)

### 360dialog (WhatsApp)

1. Sign up at [360dialog.com](https://360dialog.com)
2. Get a WhatsApp Business API number
3. Copy your API key to `DIALOG360_API_KEY`
4. Set your webhook URL to: `https://jibu-bot.railway.app/webhook/whatsapp`

### Africa's Talking (SMS)

1. Sign up at [africastalking.com](https://africastalking.com)
2. Go to SMS → Shortcodes / Sender IDs
3. Register `JIBU` as a sender ID
4. Set your callback URL to: `https://jibu-bot.railway.app/webhook/sms`
5. Copy API key and username to `.env`

### ClickPesa (M-Pesa)

1. Sign up at [clickpesa.com](https://clickpesa.com)
2. Get your Consumer Key and Secret from the dashboard
3. Set your payment callback to: `https://jibu-bot.railway.app/webhook/payment`
4. Copy credentials to `.env`

### NECTA Results (Optional)

The NECTA results lookup feature requires you to connect a results data source. Edit `src/necta.js` → `fetchNectaResult()` function to integrate with:
- NECTA official API (if available)
- Your own results database
- A licensed data provider

---

## 📡 Webhook Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `GET /` | GET | Health check |
| `/webhook/whatsapp` | POST | Receive WhatsApp messages from 360dialog |
| `/webhook/sms` | POST | Receive SMS from Africa's Talking |
| `/webhook/payment` | POST | ClickPesa payment confirmations |

---

## ⏰ Scheduled Jobs (EAT = UTC+3)

| Job | Time (EAT) | Purpose |
|---|---|---|
| Daily questions | 16:00 | Send 3 NECTA questions to all active students |
| Streak check | 23:59 | Apply freeze credits or reset broken streaks |
| Parent reports | Sunday 09:00 | Weekly progress report to parents |
| Trial/payment check | 09:00 daily | Handle trial expiry and payment reminders |

---

## 📱 User Commands

| Command | Action |
|---|---|
| Any first message | Start enrollment |
| `A`, `B`, `C`, `D` | Answer today's question |
| `JIBU MATOKEO [index]` | Look up NECTA exam results |

---

## 💰 Pricing Model

- **7-day free trial** on signup
- **TZS 5,000/month** subscription
- **TZS 500** per NECTA results lookup
- Payments via M-Pesa through ClickPesa

---

## 🏆 Rank System

| Streak | Rank |
|---|---|
| 1–6 days | Mwanafunzi |
| 7 days | Msomi Mdogo |
| 14 days | Msomi |
| 30 days | Msomi Bora |
| 60 days | Msomi Mkuu |
| 90 days | Msomi wa Heshima |
| 180 days | Daktari Msomi |

---

## 🛠 Local Development

```bash
npm install
cp .env.example .env
# Fill in .env values
npm run dev
```

Use [ngrok](https://ngrok.com) to expose localhost for webhook testing:

```bash
ngrok http 3000
# Set your webhook URLs to: https://xxxx.ngrok.io/webhook/whatsapp
```

---

## 📁 Project Structure

```
jibu-bot/
├── index.js              # Main app, routes, cron jobs
├── package.json
├── railway.json          # Railway deployment config
├── .env.example
├── .gitignore
└── src/
    ├── airtable.js       # Database operations
    ├── claude.js         # AI question/feedback generation
    ├── whatsapp.js       # 360dialog WhatsApp client
    ├── sms.js            # Africa's Talking SMS client
    ├── payments.js       # ClickPesa M-Pesa integration
    ├── enrollment.js     # Multi-step signup flow
    ├── ranks.js          # Streak ranks & milestone messages
    └── necta.js          # NECTA results lookup
```

---

## 🐛 Troubleshooting

**Questions not sending?**
- Check cron job timezone (all times are UTC internally, EAT = UTC+3)
- Verify `DIALOG360_API_KEY` is set and active
- Check Airtable `Status` field — students must be `Active` or `Trial`

**Payments not confirming?**
- Verify ClickPesa callback URL is set to `/webhook/payment`
- Check `APP_URL` env var matches your Railway domain

**SMS splitting incorrectly?**
- SMS is capped at 159 chars per segment with part number
- Edit `src/sms.js` `splitSMS()` if needed

---

Built with ❤️ for Tanzanian students. Fuzu NECTA! 🇹🇿
