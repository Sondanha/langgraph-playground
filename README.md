# LangGraph Playground

<p align="center">
  <img src="https://github.com/user-attachments/assets/4b5a6716-6db6-4621-8949-aaafd3b9dd6a" width="500" alt="LangGraph Logo"/>
</p>

This repository is a practice project for learning [LangGraph](https://www.langchain.com/langgraph).  
It demonstrates a simple **multi-turn chatbot** flow using `LangChain` + `LangGraph`.

---

## 📂 Project Structure
```yaml
.
├─ .env # contains OPEN_API_KEY (never commit this)
├─ main.py # CLI entry point
├─ requirements.txt # dependencies
├─ graph/
│ ├─ graph.py # StateGraph definition
│ ├─ nodes/
│ │ └─ chatbot_node.py
│ └─ state/
│ └─ state.py
└─ utils/ # (optional) helper scripts
```

---

## 🚀 How to Run

1. **Clone the repository**
  
  ```bash
  git clone https://github.com/<your-id>/langgraph-playground.git
  cd langgraph-playground
  ```

2. **Create virtual environment**
  ```bash
  python -m venv venv
  source venv/bin/activate   # macOS/Linux
  venv\Scripts\activate      # Windows
  ```

3. **Install dependencies**
   
  ```bash
  pip install -r requirements.txt
  ```

4. **Set your API key**
- Create a .env file in the project root:
  ```ini
  OPEN_API_KEY=sk-xxxxxx
  ```

5. **Run the chatbot**
  ```bash
  python main.py
  ```

---

## 💬 Example
```css
코드 복사
quit/exit/q to quit, reset to clear history.

>> Hello
Hi! How can I help you today?

>> Who created you?
I was built with LangChain + LangGraph for demo purposes.
```

⚠️ Notes
- Do not commit your .env file.
- Free credits expire quickly; check your OpenAI usage dashboard.


---
